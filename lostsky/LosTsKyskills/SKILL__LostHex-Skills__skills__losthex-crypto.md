---
name: losthex-crypto
description: >-
  Crypto attacks — RSA, hash length extension, lattice, symmetric ciphers, classical ciphers. Triggers: RSA attack, hash length extension, lattice, symmetric cipher, classical cipher, cryptanalysis, padding oracle.
---
# LostHex-CRYPTO

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
# need: sage (optional), hashcat, openssl
```

## RSA (ดู RSA_ATTACK_CATALOG.md)

```bash
# common: small e, common modulus, Hastad, Franklin-Reiter, Wiener, Boneh-Durfee
openssl rsa -in key.pem -text -noout
# factor
python -c "import math; print(math.gcd(n1,n2))"
# lattice: coppersmith
```

## Hash

```bash
hashcat -m 0 hashes.txt wordlist  # md5
hashcat -m 1400 hashes.txt wordlist  # sha256
# length extension: hash_extender / hashpump
hashpump -s 'hash' -d 'data' -a 'append' -k 16
```

## Symmetric (ดู BLOCK_CIPHER_ATTACKS.md)

- Padding oracle, BEAST, Lucky13, Sweet32 — ตาม cipher/mode

## Classical

```bash
# caesar, vigenere, substitution — ดู classical-cipher-analysis
```

Ponytail: ตัด lattice full automation — ceiling = known attacks with params, upgrade เมื่อมี sage + CTF toolkit.