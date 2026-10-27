---
name: losthex-binary
description: >-
  Binary exploitation — stack overflow/ROP, heap, format string, kernel, sandbox escape, VM reversal. Triggers: stack overflow, ROP, heap exploitation, format string, kernel exploit, sandbox escape, VM bytecode reversal, pwn.
---
# LostHex-BINARY

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
# need: pwntools, gdb+gef/pwndbg, ropper/ROPgadget
pip install pwntools
```

## 1) Stack Overflow + ROP

```bash
checksec --file ./vuln
# NX? PIE? Canary? RELRO?
cyclic 200 > in; ./vuln < in; # offset
# ROP chain
ROPgadget --binary ./vuln | grep "pop rdi"
ropper --file ./vuln --search "pop rdi"
# pwntools
python exploit.py  # p = process('./vuln'); p.sendline(b'A'*offset + rop)
```

Pattern: offset -> ret2libc / ret2system / SROP (ดู ROP_ADVANCED_TECHNIQUES.md)

## 2) Heap

```bash
# glibc version matters
ldd ./vuln | grep libc
# techniques by version: House of *, tcache, fastbin
# IO_FILE exploitation -> _IO_FILE_plus
# ดู HOUSE_OF_TECHNIQUES.md + IO_FILE_EXPLOITATION.md
```

## 3) Format String

```bash
# leak
./vuln <<< "%x.%x.%x.%x"
./vuln <<< "%p."*20
# write
./vuln <<< "%7$n"  # write to 7th arg
# pwntools FmtStr
from pwn import FmtStr; fmt = FmtStr(execute_fmt)
```

## 4) Kernel

```bash
# mitigations
cat /proc/sys/kernel/kptr_restrict
cat /proc/sys/kernel/dmesg_restrict
# SMEP/SMAP/KASLR/KPTI check
# techniques: ret2usr -> SMEP bypass -> ROP -> commit_creds
# ดู KERNEL_HEAP_TECHNIQUES.md + KERNEL_MITIGATION_BYPASS.md
```

## 5) Sandbox / Seccomp

```bash
seccomp-tools dump ./vuln
# bypass: open/read/write linear vs orw chain
# python sandbox: __class__.__mro__[1].__subclasses__()
# ดู PYTHON_SANDBOX_ESCAPE.md + SECCOMP_BYPASS.md
```

## 6) VM / Bytecode Reverse

```bash
# identify VM: strings, handler table, dispatch loop
# trace -> reconstruct opcode map
# ดู vm-and-bytecode-reverse/SKILL.md
```

Every exploit leaves `exploit/exploit.py` runnable + `exploit/README.md` with offsets

Ponytail: ตัด kernel heap feng shui แบบ full — ceiling = basic UAF + cred overwrite, upgrade เมื่อมี heap layout control.