---
name: losthex-forensics
description: >-
  Memory forensics, volatility, pcap analysis, stego. Triggers: memory forensics, Volatility, pcap analysis, steganography, disk image, event logs, deleted file recovery.
---
# LostHex-FORENSICS

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
```

## Volatility (ดู VOLATILITY_CHEATSHEET.md)

```bash
vol.py -f mem.raw windows.info
vol.py -f mem.raw windows.pslist
vol.py -f mem.raw windows.netscan
vol.py -f mem.raw windows.hashdump
vol.py -f mem.raw windows.malfind
```

## PCAP

```bash
tshark -r capture.pcap -Y http -T fields -e http.host -e http.request.uri
wireshark capture.pcap
# extract files: File -> Export Objects -> HTTP
```

## Stego (ดู STEGO_TOOLS_GUIDE.md)

```bash
steghide info stego.jpg
binwalk -e stego.png
zsteg -a stego.png
exiftool stego.jpg
```

Ponytail: ตัด timeline reconstruction แบบ full — ceiling = tool output triage, upgrade เมื่อมี case context.