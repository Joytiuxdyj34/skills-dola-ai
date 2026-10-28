#!/usr/bin/env bash
# LostHex — bring the HexStrike API server up inside Kali WSL. One owner, always.
#
# THE BUG THIS FIXES
# ------------------
# /etc/systemd/system/hexstrike.service is installed AND enabled
# (multi-user.target.wants symlink), and /etc/wsl.conf has systemd=true. So the
# service starts on every WSL boot and takes 0.0.0.0:8888. The old script then
# tried `systemctl start` as the default (non-root) user, was refused, printed
# "systemctl start unavailable", and launched a SECOND server with nohup. That
# second server lost the race against the service's Restart=on-failure retries
# and died with "Address already in use" -- every single time. Two owners, one
# port.
#
# So: if the unit exists, systemd is the only thing allowed to run the server.
# This script just drives it. The nohup path survives only for distros with no
# unit installed.
#
# Controlling a system unit needs root. start-hexstrike.bat invokes this with
# `wsl -u root`, which needs no password in WSL.
set -euo pipefail

export HEXSTRIKE_REPO="${HEXSTRIKE_REPO:-/mnt/c/Users/${WINUSER:-$USER}/hexstrike-ai}"
export HEXSTRIKE_HOST="${HEXSTRIKE_HOST:-0.0.0.0}"
export HEXSTRIKE_PORT="${HEXSTRIKE_PORT:-8888}"
export HEXSTRIKE_COMMAND_TIMEOUT="${HEXSTRIKE_COMMAND_TIMEOUT:-240}"
export HEXSTRIKE_HEALTH_TTL="${HEXSTRIKE_HEALTH_TTL:-300}"

SERVER_DIR="$HEXSTRIKE_REPO"
SERVER_PY="$SERVER_DIR/hexstrike_server.py"
PID_FILE="/tmp/hexstrike-server.pid"
LOG_FILE="/tmp/hexstrike-server.log"
LOG_MAX_BYTES=$((8 * 1024 * 1024))
UNIT="hexstrike.service"
UNIT_FILE="/etc/systemd/system/$UNIT"

# 0.0.0.0 is a bind address, not a connect address -- always probe loopback.
PROBE_HOST="$HEXSTRIKE_HOST"
if [[ "$PROBE_HOST" == "0.0.0.0" || "$PROBE_HOST" == "::" ]]; then
  PROBE_HOST="127.0.0.1"
fi

port_open() { timeout 1 bash -c ": >/dev/tcp/$PROBE_HOST/$HEXSTRIKE_PORT" 2>/dev/null; }

api_healthy() {
  # A live HexStrike answers /health with JSON. Anything else on the port (relay,
  # unrelated service, half-dead server) fails this test.
  timeout 4 curl -fsS "http://$PROBE_HOST:$HEXSTRIKE_PORT/health" 2>/dev/null \
    | grep -q '"status"'
}

# --- already serving? never restart a healthy server -------------------------
if port_open && api_healthy; then
  echo "HexStrike API already answers on $PROBE_HOST:$HEXSTRIKE_PORT"
  exit 0
fi

# =============================================================================
# A) systemd unit present -> systemd is the single owner
# =============================================================================
if [[ -f "$UNIT_FILE" ]]; then
  if [[ "$(id -u)" -ne 0 ]]; then
    echo "FAILED: $UNIT owns port $HEXSTRIKE_PORT but controlling it needs root." >&2
    echo "        Run start-hexstrike.bat, or:" >&2
    echo "        wsl -d ${WSL_DISTRO_NAME:-kali-linux} -u root -- bash $0" >&2
    exit 1
  fi

  echo "Managing $UNIT (systemd owns port $HEXSTRIKE_PORT)..."
  if systemctl restart "$UNIT" 2>/dev/null; then
    :
  elif systemctl start "$UNIT" 2>/dev/null; then
    :
  else
    echo "FAILED: systemctl could not start $UNIT." >&2
    systemctl status "$UNIT" --no-pager -l 2>&1 | tail -15 >&2 || true
    exit 1
  fi

  for _ in $(seq 1 40); do
    if port_open && api_healthy; then
      echo "HexStrike ready via $UNIT on $PROBE_HOST:$HEXSTRIKE_PORT"
      exit 0
    fi
    sleep 1
  done

  echo "FAILED: $UNIT is not answering /health. Why it died:" >&2
  systemctl status "$UNIT" --no-pager -l 2>&1 | tail -12 >&2 || true
  echo "--- journal ---" >&2
  journalctl -u "$UNIT" -n 30 --no-pager 2>&1 | tail -30 >&2 || true
  exit 1
fi

# =============================================================================
# B) no unit installed -> managed nohup fallback
# =============================================================================
if [[ ! -f "$SERVER_PY" ]]; then
  echo "FAILED: no server at $SERVER_PY" >&2
  echo "        Set HEXSTRIKE_REPO to your hexstrike-ai checkout (WSL path)." >&2
  exit 1
fi

holder_pids() {
  # Same-user PIDs only; this script never escalates.
  ss -tlnpH "sport = :$HEXSTRIKE_PORT" 2>/dev/null \
    | grep -oE 'pid=[0-9]+' | cut -d= -f2 | sort -u || true
}

reap_holder() {
  local pids
  pids="$(holder_pids)"
  if [[ -n "$pids" ]]; then
    echo "reaping unhealthy holder on $HEXSTRIKE_PORT: $(echo "$pids" | tr '\n' ' ')" >&2
    # shellcheck disable=SC2086
    kill -TERM $pids 2>/dev/null || true
    sleep 1
    pids="$(holder_pids)"
    # shellcheck disable=SC2086
    if [[ -n "$pids" ]]; then kill -KILL $pids 2>/dev/null || true; fi
  fi
  pkill -f "$SERVER_PY" 2>/dev/null || true
  rm -f "$PID_FILE"
  for _ in $(seq 1 10); do
    port_open || return 0
    sleep 1
  done
  return 1
}

# log rotation: the log silently grew past 8 MB
if [[ -f "$LOG_FILE" ]]; then
  log_size="$(stat -c%s "$LOG_FILE" 2>/dev/null || echo 0)"
  if (( log_size > LOG_MAX_BYTES )); then
    mv -f "$LOG_FILE" "$LOG_FILE.1"
  fi
fi

if port_open; then
  echo "Port $HEXSTRIKE_PORT is held but /health does not answer -- taking it over." >&2
  if ! reap_holder; then
    echo "FAILED: port $HEXSTRIKE_PORT is still held by something this user cannot kill." >&2
    echo "        From Windows run:  wsl --shutdown   then start HexStrike again." >&2
    ss -tlnp "sport = :$HEXSTRIKE_PORT" >&2 2>/dev/null || true
    exit 1
  fi
fi

if [[ -f "$PID_FILE" ]]; then
  old_pid="$(cat "$PID_FILE" 2>/dev/null || true)"
  if [[ "$old_pid" =~ ^[0-9]+$ ]] && kill -0 "$old_pid" 2>/dev/null; then
    old_cmd="$(tr '\0' ' ' < "/proc/$old_pid/cmdline" 2>/dev/null || true)"
    if [[ "$old_cmd" == *"$SERVER_PY"* ]]; then
      echo "HexStrike WSL server already running (pid $old_pid)"
      exit 0
    fi
  fi
  rm -f "$PID_FILE"
fi

cd "$SERVER_DIR"
nohup python3 "$SERVER_PY" >>"$LOG_FILE" 2>&1 </dev/null &
server_pid=$!
echo "$server_pid" > "$PID_FILE"

for _ in $(seq 1 45); do
  if ! kill -0 "$server_pid" 2>/dev/null; then
    echo "HexStrike server exited; last 40 log lines:" >&2
    tail -40 "$LOG_FILE" >&2 || true
    exit 1
  fi
  if port_open && api_healthy; then
    echo "HexStrike WSL server ready (pid $server_pid) on $PROBE_HOST:$HEXSTRIKE_PORT"
    exit 0
  fi
  sleep 1
done

echo "HexStrike server did not become ready; last 40 log lines:" >&2
tail -40 "$LOG_FILE" >&2 || true
exit 1
