---
name: losthex-mobile
description: >-
  Android/iOS pentest, SSL pinning bypass, runtime tricks. Triggers: Android pentest, iOS pentest, SSL pinning bypass, Frida, runtime hooking, mobile app security.
---
# LostHex-MOBILE

## Gate

```bash
python "$HOME/.workbuddy-ai/skills/losthex-hack/scripts/gate.py"   # bundled gate = HexStrike health check
# need: adb, frida, objection, apktool, jadx
```

## Android

```bash
adb devices
adb shell pm list packages | grep target
adb pull /data/app/target.apk
apktool d target.apk -o out
jadx -d jadx_out target.apk
# dynamic
frida-ps -U
objection -g com.target.app explore
# pinning bypass — ดู FRIDA_SCRIPTS.md
frida -U -f com.target.app -l frida_pinning_bypass.js --no-pause
```

## iOS

```bash
# check plist, keychain, ATS
# frida + objection on jailbroken device
# ดู IOS_RUNTIME_TRICKS.md
```

## SSL Pinning Bypass matrix

| App | Bypass |
|---|---|
| OkHttp | frida hook CertificatePinner |
| Flutter | frida + ssl pinning script v2 |
| Cordova | hook cordova plugin |

Verify ด้วย Burp intercept หลัง bypass ต้องเห็น plaintext

Ponytail: ตัด iOS kernel chain — ceiling = app layer, upgrade เมื่อมี jailbreak + kernel exploit.