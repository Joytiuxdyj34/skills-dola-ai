# CyberStrike — MITRE ATT&CK Skill Index

Sources (read-only):
- `./references/upstream/mitre_attack\` — **691** SKILL.md (Enterprise v18.1)
- `./references/upstream/mitre_attack_mobile\` — **124** SKILL.md (Mobile v18.1)
- `./references/upstream/mitre_attack_ics\` — **83** SKILL.md (ICS v18.1)

Combined MITRE source bytes: **4,733,863**

## Organization

Two-level tree: `TA####_<tactic-slug>/T####[.###]_<technique-slug>/SKILL.md`.
One `SKILL.md` per technique **or** sub-technique. Sub-technique dirs carry the dotted ID
(e.g. `T1566.001_spearphishing-attachment`). Each file = YAML frontmatter
(`technique_id`, `tactic`, `all_tactics`, `platforms`, `mitre_url`, `cwe_ids`, `chains_with`,
`prerequisites`, `severity_boost`) + body sections: High-Level Description, Kill Chain Phase,
Platforms, What to Check, How to Test (commands/scripts).
A technique appears under its **primary tactic** dir only; `all_tactics` in frontmatter lists the rest.

Root also holds `generate_skills.py`, `generate_skills_with_art.py` (Enterprise), `generate_skills.py` (Mobile/ICS), `README.md`.

## Representative samples read

- `TA0002_execution/T1059.001_powershell` — PowerShell abuse for exec/download (sub-technique of T1059).
- `TA0005_defense-evasion/T1027_obfuscated-files-or-information` — encrypt/encode/archive payloads to evade.
- `TA0006_credential-access/T1003.001_lsass-memory` — LSASS dump (procdump, mimikatz sekurlsa, comsvcs.dll).
- `TA0043_reconnaissance/T1595_active-scanning` — active network probing of victim infra.
- `TA0011_command-and-control/T1071.001_web-protocols` — C2 over HTTP/S/WebSocket to blend traffic.

---

## MITRE ATT&CK Enterprise — tactic index (691 skills, 14 tactics)

| Tactic dir | Skills |
|---|---|
| `TA0001_initial-access` | 15 |
| `TA0002_execution` | 45 |
| `TA0003_persistence` | 80 |
| `TA0004_privilege-escalation` | 25 |
| `TA0005_defense-evasion` | 183 |
| `TA0006_credential-access` | 62 |
| `TA0007_discovery` | 43 |
| `TA0008_lateral-movement` | 17 |
| `TA0009_collection` | 36 |
| `TA0010_exfiltration` | 19 |
| `TA0011_command-and-control` | 41 |
| `TA0040_impact` | 33 |
| `TA0042_resource-development` | 47 |
| `TA0043_reconnaissance` | 45 |

### TA0001_initial-access (15)
- `T1189` — Adversaries may gain access to a system through a user visiting a website over the normal course of browsing.
- `T1190` — Adversaries may attempt to exploit a weakness in an Internet-facing host or system to initially access a netwo
- `T1195` — Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for th
- `T1195.001` — Adversaries may manipulate software dependencies and development tools prior to receipt by a final consumer fo
- `T1195.002` — Adversaries may manipulate application software prior to receipt by a final consumer for the purpose of data o
- `T1195.003` — Adversaries may manipulate hardware components in products prior to receipt by a final consumer for the purpos
- `T1199` — Adversaries may breach or otherwise leverage organizations who have access to intended victims.
- `T1200` — Adversaries may physically introduce computer accessories, networking hardware, or other computing devices int
- `T1566` — Adversaries may send phishing messages to gain access to victim systems.
- `T1566.001` — Adversaries may send spearphishing emails with a malicious attachment in an attempt to gain access to victim s
- `T1566.002` — Adversaries may send spearphishing emails with a malicious link in an attempt to gain access to victim systems
- `T1566.003` — Adversaries may send spearphishing messages via third-party services in an attempt to gain access to victim sy
- `T1566.004` — Adversaries may use voice communications to ultimately gain access to victim systems.
- `T1659` — Adversaries may gain access and continuously communicate with victims by injecting malicious content into syst
- `T1669` — Adversaries may gain initial access to target systems by connecting to wireless networks.

### TA0002_execution (45)
- `T1047` — Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads.
- `T1053` — Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious 
- `T1053.002` — Adversaries may abuse the at utility to perform task scheduling for initial or recurring execution of maliciou
- `T1053.003` — Adversaries may abuse the <code>cron</code> utility to perform task scheduling for initial or recurring execut
- `T1053.005` — Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution
- `T1053.006` — Adversaries may abuse systemd timers to perform task scheduling for initial or recurring execution of maliciou
- `T1053.007` — Adversaries may abuse task scheduling functionality provided by container orchestration tools such as Kubernet
- `T1059` — Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries.
- `T1059.001` — Adversaries may abuse PowerShell commands and scripts for execution.
- `T1059.002` — Adversaries may abuse AppleScript for execution.
- `T1059.003` — Adversaries may abuse the Windows command shell for execution.
- `T1059.004` — Adversaries may abuse Unix shell commands and scripts for execution.
- `T1059.005` — Adversaries may abuse Visual Basic (VB) for execution.
- `T1059.006` — Adversaries may abuse Python commands and scripts for execution.
- `T1059.007` — Adversaries may abuse various implementations of JavaScript for execution.
- `T1059.008` — Adversaries may abuse scripting or built-in command line interpreters (CLI) on network devices to execute mali
- `T1059.009` — Adversaries may abuse cloud APIs to execute malicious commands.
- `T1059.010` — Adversaries may execute commands and perform malicious tasks using AutoIT and AutoHotKey automation scripts.
- `T1059.011` — Adversaries may abuse Lua commands and scripts for execution.
- `T1059.012` — Adversaries may abuse hypervisor command line interpreters (CLIs) to execute malicious commands.
- `T1059.013` — Adversaries may abuse built-in CLI tools or API calls to execute malicious commands in containerized environme
- `T1072` — Adversaries may gain access to and use centralized software suites installed within an enterprise to execute c
- `T1106` — Adversaries may interact with the native OS application programming interface (API) to execute behaviors.
- `T1129` — Adversaries may execute malicious payloads via loading shared modules.
- `T1203` — Adversaries may exploit software vulnerabilities in client applications to execute code.
- `T1204` — An adversary may rely upon specific actions by a user in order to gain execution.
- `T1204.001` — An adversary may rely upon a user clicking a malicious link in order to gain execution.
- `T1204.002` — An adversary may rely upon a user opening a malicious file in order to gain execution.
- `T1204.003` — Adversaries may rely on a user running a malicious image to facilitate execution.
- `T1204.004` — An adversary may rely upon a user copying and pasting code in order to gain execution.
- `T1204.005` — Adversaries may rely on a user installing a malicious library to facilitate execution.
- `T1559` — Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution.
- `T1559.001` — Adversaries may use the Windows Component Object Model (COM) for local code execution.
- `T1559.002` — Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands.
- `T1559.003` — Adversaries can provide malicious content to an XPC service daemon for local code execution.
- `T1569` — Adversaries may abuse system services or daemons to execute commands or programs.
- `T1569.001` — Adversaries may abuse launchctl to execute commands or programs.
- `T1569.002` — Adversaries may abuse the Windows service control manager to execute malicious commands or payloads.
- `T1569.003` — Adversaries may abuse systemctl to execute commands or programs.
- `T1609` — Adversaries may abuse a container administration service to execute commands within a container.
- `T1648` — Adversaries may abuse serverless computing, integration, and automation services to execute arbitrary code in 
- `T1651` — Adversaries may abuse cloud management services to execute commands within virtual machines.
- `T1674` — Adversaries may simulate keystrokes on a victim’s computer by various means to perform any type of action on b
- `T1675` — Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi
- `T1677` — Adversaries may manipulate continuous integration / continuous development (CI/CD) processes by injecting mali

### TA0003_persistence (80)
- `T1037` — Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.
- `T1037.001` — Adversaries may use Windows logon scripts automatically executed at logon initialization to establish persiste
- `T1037.002` — Adversaries may use a Login Hook to establish persistence executed upon user logon.
- `T1037.003` — Adversaries may use network logon scripts automatically executed at logon initialization to establish persiste
- `T1037.004` — Adversaries may establish persistence by modifying RC scripts, which are executed during a Unix-like system’s 
- `T1037.005` — Adversaries may use startup items automatically executed at boot initialization to establish persistence.
- `T1098` — Adversaries may manipulate accounts to maintain and/or elevate access to victim systems.
- `T1098.001` — Adversaries may add adversary-controlled credentials to a cloud account to maintain persistent access to victi
- `T1098.002` — Adversaries may grant additional permission levels to maintain persistent access to an adversary-controlled em
- `T1098.003` — An adversary may add additional roles or permissions to an adversary-controlled cloud account to maintain pers
- `T1098.004` — Adversaries may modify the SSH <code>authorized_keys</code> file to maintain persistence on a victim host.
- `T1098.005` — Adversaries may register a device to an adversary-controlled account.
- `T1098.006` — An adversary may add additional roles or permissions to an adversary-controlled user or service account to mai
- `T1098.007` — An adversary may add additional local or domain groups to an adversary-controlled account to maintain persiste
- `T1133` — Adversaries may leverage external-facing remote services to initially access and/or persist within a network.
- `T1136` — Adversaries may create an account to maintain access to victim systems.
- `T1136.001` — Adversaries may create a local account to maintain access to victim systems.
- `T1136.002` — Adversaries may create a domain account to maintain access to victim systems.
- `T1136.003` — Adversaries may create a cloud account to maintain access to victim systems.
- `T1137` — Adversaries may leverage Microsoft Office-based applications for persistence between startups.
- `T1137.001` — Adversaries may abuse Microsoft Office templates to obtain persistence on a compromised system.
- `T1137.002` — 'Adversaries may abuse the Microsoft Office "Office Test" Registry key to obtain persistence on a compromised 
- `T1137.003` — Adversaries may abuse Microsoft Outlook forms to obtain persistence on a compromised system.
- `T1137.004` — Adversaries may abuse Microsoft Outlook's Home Page feature to obtain persistence on a compromised system.
- `T1137.005` — Adversaries may abuse Microsoft Outlook rules to obtain persistence on a compromised system.
- `T1137.006` — Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system.
- `T1176` — Adversaries may abuse software extensions to establish persistent access to victim systems.
- `T1176.001` — Adversaries may abuse internet browser extensions to establish persistent access to victim systems.
- `T1176.002` — Adversaries may abuse an integrated development environment (IDE) extension to establish persistent access to 
- `T1505` — Adversaries may abuse legitimate extensible development features of servers to establish persistent access to 
- `T1505.001` — Adversaries may abuse SQL stored procedures to establish persistent access to systems.
- `T1505.002` — Adversaries may abuse Microsoft transport agents to establish persistent access to systems.
- `T1505.003` — Adversaries may backdoor web servers with web shells to establish persistent access to systems.
- `T1505.004` — Adversaries may install malicious components that run on Internet Information Services (IIS) web servers to es
- `T1505.005` — Adversaries may abuse components of Terminal Services to enable persistent access to systems.
- `T1505.006` — Adversaries may abuse vSphere Installation Bundles (VIBs) to establish persistent access to ESXi hypervisors.
- `T1525` — Adversaries may implant cloud or container images with malicious code to establish persistence after gaining a
- `T1542.001` — Adversaries may modify system firmware to persist on systems.The BIOS (Basic Input/Output System) and The Unif
- `T1542.002` — Adversaries may modify component firmware to persist on systems.
- `T1542.003` — Adversaries may use bootkits to persist on systems.
- `T1543` — Adversaries may create or modify system-level processes to repeatedly execute malicious payloads as part of pe
- `T1543.001` — Adversaries may create or modify launch agents to repeatedly execute malicious payloads as part of persistence
- `T1543.002` — Adversaries may create or modify systemd services to repeatedly execute malicious payloads as part of persiste
- `T1543.003` — Adversaries may create or modify Windows services to repeatedly execute malicious payloads as part of persiste
- `T1543.004` — Adversaries may create or modify Launch Daemons to execute malicious payloads as part of persistence.
- `T1543.005` — Adversaries may create or modify container or container cluster management tools that run as daemons, agents, 
- `T1546.017` — Adversaries may maintain persistence through executing malicious content triggered using udev rules.
- `T1546.018` — Adversaries may achieve persistence by leveraging Python’s startup mechanisms, including path configuration (`
- `T1547` — Adversaries may configure system settings to automatically execute a program during system boot or logon to ma
- `T1547.001` — Adversaries may achieve persistence by adding a program to a startup folder or referencing it with a Registry 
- `T1547.002` — Adversaries may abuse authentication packages to execute DLLs when the system boots.
- `T1547.003` — Adversaries may abuse time providers to execute DLLs when the system boots.
- `T1547.004` — Adversaries may abuse features of Winlogon to execute DLLs and/or executables when a user logs in.
- `T1547.005` — Adversaries may abuse security support providers (SSPs) to execute DLLs when the system boots.
- `T1547.006` — Adversaries may modify the kernel to automatically execute programs on system boot.
- `T1547.007` — Adversaries may modify plist files to automatically run an application when a user logs in.
- `T1547.008` — Adversaries may modify or add LSASS drivers to obtain persistence on compromised systems.
- `T1547.009` — Adversaries may create or modify shortcuts that can execute a program during system boot or user login.
- `T1547.010` — Adversaries may use port monitors to run an adversary supplied DLL during system boot for persistence or privi
- `T1547.012` — Adversaries may abuse print processors to run malicious DLLs during system boot for persistence and/or privile
- `T1547.013` — Adversaries may add or modify XDG Autostart Entries to execute malicious programs or commands when a user’s de
- `T1547.014` — Adversaries may achieve persistence by adding a Registry key to the Active Setup of the local machine.
- `T1547.015` — Adversaries may add login items to execute upon user login to gain persistence or escalate privileges.
- `T1554` — Adversaries may modify host software binaries to establish persistent access to systems.
- `T1574` — Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs.
- `T1574.001` — Adversaries may abuse dynamic-link library files (DLLs) in order to achieve persistence, escalate privileges, 
- `T1574.004` — Adversaries may execute their own payloads by placing a malicious dynamic library (dylib) with an expected nam
- `T1574.005` — Adversaries may execute their own malicious payloads by hijacking the binaries used by an installer.
- `T1574.006` — Adversaries may execute their own malicious payloads by hijacking environment variables the dynamic linker use
- `T1574.007` — Adversaries may execute their own malicious payloads by hijacking environment variables used to load libraries
- `T1574.008` — Adversaries may execute their own malicious payloads by hijacking the search order used to load other programs
- `T1574.009` — Adversaries may execute their own malicious payloads by hijacking vulnerable file path references.
- `T1574.010` — Adversaries may execute their own malicious payloads by hijacking the binaries used by services.
- `T1574.011` — Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services.
- `T1574.012` — Adversaries may leverage the COR_PROFILER environment variable to hijack the execution flow of programs that l
- `T1574.013` — Adversaries may abuse the <code>KernelCallbackTable</code> of a process to hijack its execution flow in order 
- `T1574.014` — Adversaries may execute their own malicious payloads by hijacking how the .NET `AppDomainManager` loads assemb
- `T1653` — Adversaries may impair a system's ability to hibernate, reboot, or shut down in order to extend access to infe
- `T1668` — Adversaries who successfully compromise a system may attempt to maintain persistence by “closing the door” beh
- `T1671` — Adversaries may achieve persistence by leveraging OAuth application integrations in a software-as-a-service en

### TA0004_privilege-escalation (25)
- `T1068` — Adversaries may exploit software vulnerabilities in an attempt to elevate privileges.
- `T1546` — Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution
- `T1546.001` — Adversaries may establish persistence by executing malicious content triggered by a file type association.
- `T1546.002` — Adversaries may establish persistence by executing malicious content triggered by user inactivity.
- `T1546.003` — Adversaries may establish persistence and elevate privileges by executing malicious content triggered by a Win
- `T1546.004` — Adversaries may establish persistence through executing malicious commands triggered by a user’s shell.
- `T1546.005` — Adversaries may establish persistence by executing malicious content triggered by an interrupt signal.
- `T1546.006` — Adversaries may establish persistence by executing malicious content triggered by the execution of tainted bin
- `T1546.007` — Adversaries may establish persistence by executing malicious content triggered by Netsh Helper DLLs.
- `T1546.008` — Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by ac
- `T1546.009` — Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by Ap
- `T1546.010` — Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by Ap
- `T1546.011` — Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by ap
- `T1546.012` — Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by Im
- `T1546.013` — Adversaries may gain persistence and elevate privileges by executing malicious content triggered by PowerShell
- `T1546.014` — Adversaries may gain persistence and elevate privileges by executing malicious content triggered by the Event 
- `T1546.015` — Adversaries may establish persistence by executing malicious content triggered by hijacked references to Compo
- `T1546.016` — Adversaries may establish persistence and elevate privileges by using an installer to trigger the execution of
- `T1548` — Adversaries may circumvent mechanisms designed to control elevate privileges to gain higher-level permissions.
- `T1548.001` — An adversary may abuse configurations where an application has the setuid or setgid bits set in order to get c
- `T1548.002` — Adversaries may bypass UAC mechanisms to elevate process privileges on system.
- `T1548.003` — Adversaries may perform sudo caching and/or use the sudoers file to elevate privileges.
- `T1548.004` — Adversaries may leverage the <code>AuthorizationExecuteWithPrivileges</code> API to escalate privileges by pro
- `T1548.005` — Adversaries may abuse permission configurations that allow them to gain temporarily elevated access to cloud r
- `T1611` — Adversaries may break out of a container or virtualized environment to gain access to the underlying host.

### TA0005_defense-evasion (183)
- `T1006` — Adversaries may directly access a volume to bypass file access controls and file system monitoring.
- `T1014` — Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, 
- `T1027` — Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding
- `T1027.001` — Adversaries may use binary padding to add junk data and change the on-disk representation of malware.
- `T1027.002` — Adversaries may perform software packing or virtual machine software protection to conceal their code.
- `T1027.003` — Adversaries may use steganography techniques in order to prevent the detection of hidden information.
- `T1027.004` — Adversaries may attempt to make payloads difficult to discover and analyze by delivering files to victims as u
- `T1027.005` — Adversaries may remove indicators from tools if they believe their malicious tool was detected, quarantined, o
- `T1027.006` — Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly b
- `T1027.007` — Adversaries may obfuscate then dynamically resolve API functions called by their malware in order to conceal m
- `T1027.008` — Adversaries may attempt to make a payload difficult to analyze by removing symbols, strings, and other human r
- `T1027.009` — Adversaries may embed payloads within other files to conceal malicious content from defenses.
- `T1027.010` — Adversaries may obfuscate content during command execution to impede detection.
- `T1027.011` — 'Adversaries may store data in "fileless" formats to conceal malicious activity from defenses.'
- `T1027.012` — Adversaries may smuggle commands to download malicious payloads past content filters by hiding them within oth
- `T1027.013` — Adversaries may encrypt or encode files to obfuscate strings, bytes, and other specific patterns to impede det
- `T1027.014` — Adversaries may utilize polymorphic code (also known as metamorphic or mutating code) to evade detection.
- `T1027.015` — Adversaries may use compression to obfuscate their payloads or files.
- `T1027.016` — Adversaries may use junk code / dead code to obfuscate a malware’s functionality.
- `T1027.017` — Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly b
- `T1036` — Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to 
- `T1036.001` — Adversaries may attempt to mimic features of valid code signatures to increase the chance of deceiving a user,
- `T1036.002` — Adversaries may abuse the right-to-left override (RTLO or RLO) character (U+202E) to disguise a string and/or 
- `T1036.003` — Adversaries may rename legitimate / system utilities to try to evade security mechanisms concerning the usage 
- `T1036.004` — Adversaries may attempt to manipulate the name of a task or service to make it appear legitimate or benign.
- `T1036.005` — Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resourc
- `T1036.006` — Adversaries can hide a program's true filetype by changing the extension of a file.
- `T1036.007` — Adversaries may abuse a double extension in the filename as a means of masquerading the true file type.
- `T1036.008` — Adversaries may masquerade malicious payloads as legitimate files through changes to the payload's formatting,
- `T1036.009` — An adversary may attempt to evade process tree-based analysis by modifying executed malware's parent process I
- `T1036.010` — Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign
- `T1036.011` — Adversaries may modify a process's in-memory arguments to change its name in order to appear as a legitimate o
- `T1036.012` — Adversaries may attempt to blend in with legitimate traffic by spoofing browser and system attributes like ope
- `T1055` — Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevat
- `T1055.001` — Adversaries may inject dynamic-link libraries (DLLs) into processes in order to evade process-based defenses a
- `T1055.002` — Adversaries may inject portable executables (PE) into processes in order to evade process-based defenses as we
- `T1055.003` — Adversaries may inject malicious code into hijacked processes in order to evade process-based defenses as well
- `T1055.004` — Adversaries may inject malicious code into processes via the asynchronous procedure call (APC) queue in order 
- `T1055.005` — Adversaries may inject malicious code into processes via thread local storage (TLS) callbacks in order to evad
- `T1055.008` — Adversaries may inject malicious code into processes via ptrace (process trace) system calls in order to evade
- `T1055.009` — Adversaries may inject malicious code into processes via the /proc filesystem in order to evade process-based 
- `T1055.011` — Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-bas
- `T1055.012` — Adversaries may inject malicious code into suspended and hollowed processes in order to evade process-based de
- `T1055.013` — Adversaries may inject malicious code into process via process doppelgänging in order to evade process-based d
- `T1055.014` — Adversaries may inject malicious code into processes via VDSO hijacking in order to evade process-based defens
- `T1055.015` — Adversaries may abuse list-view controls to inject malicious code into hijacked processes in order to evade pr
- `T1070` — Adversaries may delete or modify artifacts generated within systems to remove evidence of their presence or hi
- `T1070.001` — Adversaries may clear Windows Event Logs to hide the activity of an intrusion.
- `T1070.002` — Adversaries may clear system logs to hide evidence of an intrusion.
- `T1070.003` — In addition to clearing system logs, an adversary may clear the command history of a compromised account to co
- `T1070.004` — Adversaries may delete files left behind by the actions of their intrusion activity.
- `T1070.005` — Adversaries may remove share connections that are no longer useful in order to clean up traces of their operat
- `T1070.006` — Adversaries may modify file time attributes to hide new files or changes to existing files.
- `T1070.007` — Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their
- `T1070.008` — Adversaries may modify mail and mail application data to remove evidence of their activity.
- `T1070.009` — Adversaries may clear artifacts associated with previously established persistence on a host system to remove 
- `T1070.010` — Once a payload is delivered, adversaries may reproduce copies of the same malware on the victim system to remo
- `T1078` — Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persis
- `T1078.001` — Adversaries may obtain and abuse credentials of a default account as a means of gaining Initial Access, Persis
- `T1078.002` — Adversaries may obtain and abuse credentials of a domain account as a means of gaining Initial Access, Persist
- `T1078.003` — Adversaries may obtain and abuse credentials of a local account as a means of gaining Initial Access, Persiste
- `T1078.004` — Valid accounts in cloud environments may allow adversaries to perform actions to achieve Initial Access, Persi
- `T1112` — Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense 
- `T1127` — Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads.
- `T1127.001` — Adversaries may use MSBuild to proxy execution of code through a trusted Windows utility.
- `T1127.002` — Adversaries may use ClickOnce applications (.appref-ms and .application files) to proxy execution of code thro
- `T1127.003` — Adversaries may use `JamPlus` to proxy the execution of a malicious script.
- `T1134` — Adversaries may modify access tokens to operate under a different user or system security context to perform a
- `T1134.001` — Adversaries may duplicate then impersonate another user's existing token to escalate privileges and bypass acc
- `T1134.002` — Adversaries may create a new process with an existing token to escalate privileges and bypass access controls.
- `T1134.003` — Adversaries may make new tokens and impersonate users to escalate privileges and bypass access controls.
- `T1134.004` — Adversaries may spoof the parent process identifier (PPID) of a new process to evade process-monitoring defens
- `T1134.005` — Adversaries may use SID-History Injection to escalate privileges and bypass access controls.
- `T1140` — Adversaries may use Obfuscated Files or Information to hide artifacts of an intrusion from analysis.
- `T1197` — Adversaries may abuse BITS jobs to persistently execute code and perform various background tasks.
- `T1202` — Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit th
- `T1205` — Adversaries may use traffic signaling to hide open ports or other malicious functionality used for persistence
- `T1205.001` — Adversaries may use port knocking to hide open ports used for persistence or command and control.
- `T1205.002` — Adversaries may attach filters to a network socket to monitor then activate backdoors used for persistence or 
- `T1207` — Adversaries may register a rogue Domain Controller to enable manipulation of Active Directory data.
- `T1211` — Adversaries may exploit a system or application vulnerability to bypass security features.
- `T1216` — Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files
- `T1216.001` — Adversaries may use PubPrn to proxy execution of malicious remote files.
- `T1216.002` — Adversaries may abuse SyncAppvPublishingServer.vbs to proxy execution of malicious PowerShell commands.
- `T1218` — Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with
- `T1218.001` — Adversaries may abuse Compiled HTML files (.chm) to conceal malicious code.
- `T1218.002` — Adversaries may abuse control.exe to proxy execution of malicious payloads.
- `T1218.003` — Adversaries may abuse CMSTP to proxy execution of malicious code.
- `T1218.004` — Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility.
- `T1218.005` — Adversaries may abuse mshta.exe to proxy execution of malicious .hta files and Javascript or VBScript through 
- `T1218.007` — Adversaries may abuse msiexec.exe to proxy execution of malicious payloads.
- `T1218.008` — Adversaries may abuse odbcconf.exe to proxy execution of malicious payloads.
- `T1218.009` — Adversaries may abuse Regsvcs and Regasm to proxy execution of code through a trusted Windows utility.
- `T1218.010` — Adversaries may abuse Regsvr32.exe to proxy execution of malicious code.
- `T1218.011` — Adversaries may abuse rundll32.exe to proxy execution of malicious code.
- `T1218.012` — Adversaries may abuse verclsid.exe to proxy execution of malicious code.
- `T1218.013` — Adversaries may abuse mavinject.exe to proxy execution of malicious code.
- `T1218.014` — Adversaries may abuse mmc.exe to proxy execution of malicious .msc files.
- `T1218.015` — Adversaries may abuse components of the Electron framework to execute malicious code.
- `T1220` — Adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files
- `T1221` — Adversaries may create or modify references in user document templates to conceal malicious code or force auth
- `T1222` — Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and acces
- `T1222.001` — Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and acces
- `T1222.002` — Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and acces
- `T1480` — Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and env
- `T1480.001` — Adversaries may environmentally key payloads or other features of malware to evade defenses and constraint exe
- `T1480.002` — Adversaries may constrain execution or actions based on the presence of a mutex associated with malware.
- `T1484` — Adversaries may modify the configuration settings of a domain or identity tenant to evade defenses and/or esca
- `T1484.001` — Adversaries may modify Group Policy Objects (GPOs) to subvert the intended discretionary access controls for a
- `T1484.002` — Adversaries may add new domain trusts, modify the properties of existing domain trusts, or otherwise change th
- `T1497` — Adversaries may employ various means to detect and avoid virtualization and analysis environments.
- `T1497.001` — Adversaries may employ various system checks to detect and avoid virtualization and analysis environments.
- `T1497.002` — Adversaries may employ various user activity checks to detect and avoid virtualization and analysis environmen
- `T1497.003` — Adversaries may employ various time-based methods to detect virtualization and analysis environments, particul
- `T1535` — Adversaries may create cloud instances in unused geographic service regions in order to evade detection.
- `T1542` — Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system.
- `T1542.004` — Adversaries may abuse the ROM Monitor (ROMMON) by loading an unauthorized firmware with adversary code to prov
- `T1542.005` — Adversaries may abuse netbooting to load an unauthorized network device operating system from a Trivial File T
- `T1548.006` — Adversaries can manipulate or abuse the Transparency, Consent, & Control (TCC) service or database to grant ma
- `T1550` — Adversaries may use alternate authentication material, such as password hashes, Kerberos tickets, and applicat
- `T1550.001` — Adversaries may use stolen application access tokens to bypass the typical authentication process and access r
- `T1550.002` — Adversaries may “pass the hash” using stolen password hashes to move laterally within an environment, bypassin
- `T1550.003` — Adversaries may “pass the ticket” using stolen Kerberos tickets to move laterally within an environment, bypas
- `T1550.004` — Adversaries can use stolen session cookies to authenticate to web applications and services.
- `T1553` — Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execu
- `T1553.001` — Adversaries may modify file attributes and subvert Gatekeeper functionality to evade user prompts and execute 
- `T1553.002` — Adversaries may create, acquire, or steal code signing materials to sign their malware or tools.
- `T1553.003` — Adversaries may tamper with SIP and trust provider components to mislead the operating system and application 
- `T1553.004` — Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to advers
- `T1553.005` — Adversaries may abuse specific file formats to subvert Mark-of-the-Web (MOTW) controls.
- `T1553.006` — Adversaries may modify code signing policies to enable execution of unsigned or self-signed code.
- `T1562` — Adversaries may maliciously modify components of a victim environment in order to hinder or disable defensive 
- `T1562.001` — Adversaries may modify and/or disable security tools to avoid possible detection of their malware/tools and ac
- `T1562.002` — Adversaries may disable Windows event logging to limit data that can be leveraged for detections and audits.
- `T1562.003` — Adversaries may impair command history logging to hide commands they run on a compromised system.
- `T1562.004` — Adversaries may disable or modify system firewalls in order to bypass controls limiting network usage.
- `T1562.006` — An adversary may attempt to block indicators or events typically captured by sensors from being gathered and a
- `T1562.007` — Adversaries may disable or modify a firewall within a cloud environment to bypass controls that limit access t
- `T1562.008` — An adversary may disable or modify cloud logging capabilities and integrations to limit what data is collected
- `T1562.009` — Adversaries may abuse Windows safe mode to disable endpoint defenses.
- `T1562.010` — Adversaries may downgrade or use a version of system features that may be outdated, vulnerable, and/or does no
- `T1562.011` — Adversaries may spoof security alerting from tools, presenting false evidence to impair defenders’ awareness o
- `T1562.012` — Adversaries may disable or modify the Linux audit system to hide malicious activity and avoid detection.
- `T1562.013` — Adversaries may disable network device-based firewall mechanisms entirely or add, delete, or modify particular
- `T1564` — Adversaries may attempt to hide artifacts associated with their behaviors to evade detection.
- `T1564.001` — Adversaries may set files and directories to be hidden to evade detection mechanisms.
- `T1564.002` — Adversaries may use hidden users to hide the presence of user accounts they create or modify.
- `T1564.003` — Adversaries may use hidden windows to conceal malicious activity from the plain sight of users.
- `T1564.004` — Adversaries may use NTFS file attributes to hide their malicious data in order to evade detection.
- `T1564.005` — Adversaries may use a hidden file system to conceal malicious activity from users and security tools.
- `T1564.006` — Adversaries may carry out malicious operations using a virtual instance to avoid detection.
- `T1564.007` — Adversaries may hide malicious Visual Basic for Applications (VBA) payloads embedded within MS Office document
- `T1564.008` — Adversaries may use email rules to hide inbound emails in a compromised user's mailbox.
- `T1564.009` — Adversaries may abuse resource forks to hide malicious code or executables to evade detection and bypass secur
- `T1564.010` — Adversaries may attempt to hide process command-line arguments by overwriting process memory.
- `T1564.011` — Adversaries may evade defensive mechanisms by executing commands that hide from process interrupt signals.
- `T1564.012` — Adversaries may attempt to hide their file-based artifacts by writing them to specific folders or file names e
- `T1564.013` — Adversaries may abuse bind mounts on file structures to hide their activity and artifacts from native utilitie
- `T1564.014` — Adversaries may abuse extended attributes (xattrs) on macOS and Linux to hide their malicious data in order to
- `T1578` — An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses.
- `T1578.001` — An adversary may create a snapshot or data backup within a cloud account to evade defenses.
- `T1578.002` — An adversary may create a new instance or virtual machine (VM) within the compute service of a cloud account t
- `T1578.003` — An adversary may delete a cloud instance after they have performed malicious activities in an attempt to evade
- `T1578.004` — An adversary may revert changes made to a cloud instance after they have performed malicious activities in att
- `T1578.005` — Adversaries may modify settings that directly affect the size, locations, and resources available to cloud com
- `T1599` — Adversaries may bridge network boundaries by compromising perimeter network devices or internal devices respon
- `T1599.001` — Adversaries may bridge network boundaries by modifying a network device’s Network Address Translation (NAT) co
- `T1600` — Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would o
- `T1600.001` — Adversaries may reduce the level of effort required to decrypt data transmitted over the network by reducing t
- `T1600.002` — Adversaries disable a network device’s dedicated hardware encryption, which may enable them to leverage weakne
- `T1601` — Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provid
- `T1601.001` — Adversaries may modify the operating system of a network device to introduce new capabilities or weaken existi
- `T1601.002` — Adversaries may install an older version of the operating system of a network device to weaken security.
- `T1610` — Adversaries may deploy a container into an environment to facilitate execution or evade defenses.
- `T1612` — Adversaries may build a container image directly on a host to bypass defenses that monitor for the retrieval o
- `T1620` — Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads.
- `T1622` — Adversaries may employ various means to detect and avoid debuggers.
- `T1647` — Adversaries may modify property list files (plist files) to enable other malicious activity, while also potent
- `T1656` — Adversaries may impersonate a trusted person or organization in order to persuade and trick a target into perf
- `T1666` — Adversaries may attempt to modify hierarchical structures in infrastructure-as-a-service (IaaS) environments i
- `T1672` — Adversaries may fake, or spoof, a sender’s identity by modifying the value of relevant email headers in order 
- `T1678` — Adversaries may employ various time-based methods to evade detection and analysis.
- `T1679` — Adversaries may intentionally exclude certain files, folders, directories, file types, or system components fr

### TA0006_credential-access (62)
- `T1003` — Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the f
- `T1003.001` — Adversaries may attempt to access credential material stored in the process memory of the Local Security Autho
- `T1003.002` — Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either
- `T1003.003` — Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal c
- `T1003.004` — Adversaries with SYSTEM access to a host may attempt to access Local Security Authority (LSA) secrets, which c
- `T1003.005` — Adversaries may attempt to access cached domain credentials used to allow authentication to occur in the event
- `T1003.006` — Adversaries may attempt to access credentials and other sensitive information by abusing a Windows Domain Cont
- `T1003.007` — Adversaries may gather credentials from the proc filesystem or `/proc`.
- `T1003.008` — Adversaries may attempt to dump the contents of <code>/etc/passwd</code> and <code>/etc/shadow</code> to enabl
- `T1040` — Adversaries may passively sniff network traffic to capture information about an environment, including authent
- `T1110` — Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when passw
- `T1110.001` — Adversaries with no prior knowledge of legitimate credentials within the system or environment may guess passw
- `T1110.002` — Adversaries may use password cracking to attempt to recover usable credentials, such as plaintext passwords, w
- `T1110.003` — Adversaries may use a single or small list of commonly used passwords against many different accounts to attem
- `T1110.004` — Adversaries may use credentials obtained from breach dumps of unrelated accounts to gain access to target acco
- `T1111` — Adversaries may target multi-factor authentication (MFA) mechanisms, (i.e., smart cards, token generators, etc
- `T1187` — Adversaries may gather credential material by invoking or forcing a user to automatically provide authenticati
- `T1212` — Adversaries may exploit software vulnerabilities in an attempt to collect credentials.
- `T1528` — Adversaries can steal application access tokens as a means of acquiring credentials to access remote systems a
- `T1539` — An adversary may steal web application or service session cookies and use them to gain access to web applicati
- `T1552` — Adversaries may search compromised systems to find and obtain insecurely stored credentials.
- `T1552.001` — Adversaries may search local file systems and remote file shares for files containing insecurely stored creden
- `T1552.002` — Adversaries may search the Registry on compromised systems for insecurely stored credentials.
- `T1552.003` — Adversaries may search the command history on compromised systems for insecurely stored credentials.
- `T1552.004` — Adversaries may search for private key certificate files on compromised systems for insecurely stored credenti
- `T1552.005` — Adversaries may attempt to access the Cloud Instance Metadata API to collect credentials and other sensitive d
- `T1552.006` — Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP).
- `T1552.007` — Adversaries may gather credentials via APIs within a containers environment.
- `T1552.008` — Adversaries may directly collect unsecured credentials stored or passed through user communication services.
- `T1555` — Adversaries may search for common password storage locations to obtain user credentials.
- `T1555.001` — Adversaries may acquire credentials from Keychain.
- `T1555.002` — An adversary with root access may gather credentials by reading `securityd`’s memory.
- `T1555.003` — Adversaries may acquire credentials from web browsers by reading files specific to the target browser.
- `T1555.004` — Adversaries may acquire credentials from the Windows Credential Manager.
- `T1555.005` — Adversaries may acquire user credentials from third-party password managers.
- `T1555.006` — Adversaries may acquire credentials from cloud-native secret management solutions such as AWS Secrets Manager,
- `T1556` — Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise 
- `T1556.001` — Adversaries may patch the authentication process on a domain controller to bypass the typical authentication m
- `T1556.002` — Adversaries may register malicious password filter dynamic link libraries (DLLs) into the authentication proce
- `T1556.003` — Adversaries may modify pluggable authentication modules (PAM) to access user credentials or enable otherwise u
- `T1556.004` — Adversaries may use Patch System Image to hard code a password in the operating system, thus bypassing of nati
- `T1556.005` — An adversary may abuse Active Directory authentication encryption properties to gain access to credentials on 
- `T1556.006` — Adversaries may disable or modify multi-factor authentication (MFA) mechanisms to enable persistent access to 
- `T1556.007` — Adversaries may patch, modify, or otherwise backdoor cloud authentication processes that are tied to on-premis
- `T1556.008` — Adversaries may register malicious network provider dynamic link libraries (DLLs) to capture cleartext user cr
- `T1556.009` — Adversaries may disable or modify conditional access policies to enable persistent access to compromised accou
- `T1557` — Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the
- `T1557.001` — By responding to LLMNR/NBT-NS network traffic, adversaries may spoof an authoritative source for name resoluti
- `T1557.002` — Adversaries may poison Address Resolution Protocol (ARP) caches to position themselves between the communicati
- `T1557.003` — Adversaries may redirect network traffic to adversary-owned systems by spoofing Dynamic Host Configuration Pro
- `T1557.004` — Adversaries may host seemingly genuine Wi-Fi access points to deceive users into connecting to malicious netwo
- `T1558` — Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable P
- `T1558.001` — Adversaries who have the KRBTGT account password hash may forge Kerberos ticket-granting tickets (TGT), also k
- `T1558.002` — Adversaries who have the password hash of a target service account (e.g.
- `T1558.003` — Adversaries may abuse a valid Kerberos ticket-granting ticket (TGT) or sniff network traffic to obtain a ticke
- `T1558.004` — Adversaries may reveal credentials of accounts that have disabled Kerberos preauthentication by Password Crack
- `T1558.005` — Adversaries may attempt to steal Kerberos tickets stored in credential cache files (or ccache).
- `T1606` — Adversaries may forge credential materials that can be used to gain access to web applications or Internet ser
- `T1606.001` — Adversaries may forge web cookies that can be used to gain access to web applications or Internet services.
- `T1606.002` — An adversary may forge SAML tokens with any permissions claims and lifetimes if they possess a valid SAML toke
- `T1621` — Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by 
- `T1649` — Adversaries may steal or forge certificates used for authentication to access remote systems or resources.

### TA0007_discovery (43)
- `T1007` — Adversaries may try to gather information about registered local system services.
- `T1010` — Adversaries may attempt to get a listing of open application windows.
- `T1012` — Adversaries may interact with the Windows Registry to gather information about the system, configuration, and 
- `T1016` — Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses
- `T1016.001` — Adversaries may check for Internet connectivity on compromised systems.
- `T1016.002` — Adversaries may search for information about Wi-Fi networks, such as network names and passwords, on compromis
- `T1018` — Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier
- `T1033` — Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly use
- `T1046` — Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure 
- `T1049` — Adversaries may attempt to get a listing of network connections to or from the compromised system they are cur
- `T1057` — Adversaries may attempt to get information about running processes on a system.
- `T1069` — Adversaries may attempt to discover group and permission settings.
- `T1069.001` — Adversaries may attempt to find local system groups and permission settings.
- `T1069.002` — Adversaries may attempt to find domain-level groups and permission settings.
- `T1069.003` — Adversaries may attempt to find cloud groups and permission settings.
- `T1082` — An adversary may attempt to get detailed information about the operating system and hardware, including versio
- `T1083` — Adversaries may enumerate files and directories or may search in specific locations of a host or network share
- `T1087` — Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or withi
- `T1087.001` — Adversaries may attempt to get a listing of local system accounts.
- `T1087.002` — Adversaries may attempt to get a listing of domain accounts.
- `T1087.003` — Adversaries may attempt to get a listing of email addresses and accounts.
- `T1087.004` — Adversaries may attempt to get a listing of cloud accounts.
- `T1120` — Adversaries may attempt to gather information about attached peripheral devices and components connected to a 
- `T1124` — An adversary may gather the system time and/or time zone settings from a local or remote system.
- `T1135` — Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of info
- `T1201` — Adversaries may attempt to access detailed information about the password policy used within an enterprise net
- `T1217` — Adversaries may enumerate information about browsers to learn more about compromised environments.
- `T1482` — Adversaries may attempt to gather information on domain trust relationships that may be used to identify later
- `T1518` — Adversaries may attempt to get a listing of software and software versions that are installed on a system or i
- `T1518.001` — Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors th
- `T1518.002` — Adversaries may attempt to get a listing of backup software or configurations that are installed on a system.
- `T1526` — An adversary may attempt to enumerate the cloud services running on a system after gaining access.
- `T1538` — An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an 
- `T1580` — An adversary may attempt to discover infrastructure and resources that are available within an infrastructure-
- `T1613` — Adversaries may attempt to discover containers and other resources that are available within a containers envi
- `T1614` — Adversaries may gather information in an attempt to calculate the geographical location of a victim host.
- `T1614.001` — Adversaries may attempt to gather information about the system language of a victim in order to infer the geog
- `T1615` — Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, securi
- `T1619` — Adversaries may enumerate objects in cloud storage infrastructure.
- `T1652` — Adversaries may attempt to enumerate local device drivers on a victim host.
- `T1654` — Adversaries may enumerate system and service logs to find useful data.
- `T1673` — An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervi
- `T1680` — Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space an

### TA0008_lateral-movement (17)
- `T1021` — Adversaries may use Valid Accounts to log into a service that accepts remote connections, such as telnet, SSH,
- `T1021.001` — Adversaries may use Valid Accounts to log into a computer using the Remote Desktop Protocol (RDP).
- `T1021.002` — Adversaries may use Valid Accounts to interact with a remote network share using Server Message Block (SMB).
- `T1021.003` — Adversaries may use Valid Accounts to interact with remote machines by taking advantage of Distributed Compone
- `T1021.004` — Adversaries may use Valid Accounts to log into remote machines using Secure Shell (SSH).
- `T1021.005` — Adversaries may use Valid Accounts to remotely control machines using Virtual Network Computing (VNC).
- `T1021.006` — Adversaries may use Valid Accounts to interact with remote systems using Windows Remote Management (WinRM).
- `T1021.007` — Adversaries may log into accessible cloud services within a compromised environment using Valid Accounts that 
- `T1021.008` — Adversaries may leverage Valid Accounts to log directly into accessible cloud hosted compute infrastructure th
- `T1080` — Adversaries may deliver payloads to remote systems by adding content to shared storage locations, such as netw
- `T1091` — Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware t
- `T1210` — Adversaries may exploit remote services to gain unauthorized access to internal systems once inside of a netwo
- `T1534` — After they already have access to accounts or systems within the environment, adversaries may use internal spe
- `T1563` — Adversaries may take control of preexisting sessions with remote services to move laterally in an environment.
- `T1563.001` — Adversaries may hijack a legitimate user's SSH session to move laterally within an environment.
- `T1563.002` — Adversaries may hijack a legitimate user’s remote desktop session to move laterally within an environment.
- `T1570` — Adversaries may transfer tools or other files between systems in a compromised environment.

### TA0009_collection (36)
- `T1005` — Adversaries may search local system sources, such as file systems, configuration files, local databases, virtu
- `T1025` — Adversaries may search connected removable media on computers they have compromised to find files of interest.
- `T1039` — Adversaries may search network shares on computers they have compromised to find files of interest.
- `T1056` — Adversaries may use methods of capturing user input to obtain credentials or collect information.
- `T1056.001` — Adversaries may log user keystrokes to intercept credentials as the user types them.
- `T1056.002` — Adversaries may mimic common operating system GUI components to prompt users for credentials with a seemingly 
- `T1056.003` — Adversaries may install code on externally facing portals, such as a VPN login page, to capture and transmit c
- `T1056.004` — Adversaries may hook into Windows application programming interface (API) functions and Linux system functions
- `T1074` — Adversaries may stage collected data in a central location or directory prior to Exfiltration.
- `T1074.001` — Adversaries may stage collected data in a central location or directory on the local system prior to Exfiltrat
- `T1074.002` — Adversaries may stage data collected from multiple systems in a central location or directory on one system pr
- `T1113` — Adversaries may attempt to take screen captures of the desktop to gather information over the course of an ope
- `T1114` — Adversaries may target user email to collect sensitive information.
- `T1114.001` — Adversaries may target user email on local systems to collect sensitive information.
- `T1114.002` — Adversaries may target an Exchange server, Office 365, or Google Workspace to collect sensitive information.
- `T1114.003` — Adversaries may setup email forwarding rules to collect sensitive information.
- `T1115` — Adversaries may collect data stored in the clipboard from users copying information within or between applicat
- `T1119` — Once established within a system or network, an adversary may use automated techniques for collecting internal
- `T1123` — An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g
- `T1125` — An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or application
- `T1185` — Adversaries may take advantage of security vulnerabilities and inherent functionality in browser software to c
- `T1213` — Adversaries may leverage information repositories to mine valuable information.
- `T1213.001` — Adversaries may leverage Confluence repositories to mine valuable information.
- `T1213.002` — Adversaries may leverage the SharePoint repository as a source to mine valuable information.
- `T1213.003` — Adversaries may leverage code repositories to collect valuable information.
- `T1213.004` — Adversaries may leverage Customer Relationship Management (CRM) software to mine valuable information.
- `T1213.005` — Adversaries may leverage chat and messaging applications, such as Microsoft Teams, Google Chat, and Slack, to 
- `T1213.006` — Adversaries may leverage databases to mine valuable information.
- `T1530` — Adversaries may access data from cloud storage.
- `T1560` — An adversary may compress and/or encrypt data that is collected prior to exfiltration.
- `T1560.001` — Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration.
- `T1560.002` — An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party libraries.
- `T1560.003` — An adversary may compress or encrypt data that is collected prior to exfiltration using a custom method.
- `T1602` — Adversaries may collect data related to managed devices from configuration repositories.
- `T1602.001` — Adversaries may target the Management Information Base (MIB) to collect and/or mine valuable information in a 
- `T1602.002` — Adversaries may access network configuration files to collect sensitive data about the device and the network.

### TA0010_exfiltration (19)
- `T1011` — Adversaries may attempt to exfiltrate data over a different network medium than the command and control channe
- `T1011.001` — Adversaries may attempt to exfiltrate data over Bluetooth rather than the command and control channel.
- `T1020` — Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after be
- `T1020.001` — Adversaries may leverage traffic mirroring in order to automate data exfiltration over compromised infrastruct
- `T1029` — Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain interval
- `T1030` — An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certa
- `T1041` — Adversaries may steal data by exfiltrating it over an existing command and control channel.
- `T1048` — Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and 
- `T1048.001` — Adversaries may steal data by exfiltrating it over a symmetrically encrypted network protocol other than that 
- `T1048.002` — Adversaries may steal data by exfiltrating it over an asymmetrically encrypted network protocol other than tha
- `T1048.003` — Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the exi
- `T1052` — Adversaries may attempt to exfiltrate data via a physical medium, such as a removable drive.
- `T1052.001` — Adversaries may attempt to exfiltrate data over a USB connected physical device.
- `T1537` — Adversaries may exfiltrate data by transferring the data, including through sharing/syncing and creating backu
- `T1567` — Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary 
- `T1567.001` — Adversaries may exfiltrate data to a code repository rather than over their primary command and control channe
- `T1567.002` — Adversaries may exfiltrate data to a cloud storage service rather than over their primary command and control 
- `T1567.003` — Adversaries may exfiltrate data to text storage sites instead of their primary command and control channel.
- `T1567.004` — Adversaries may exfiltrate data to a webhook endpoint rather than over their primary command and control chann

### TA0011_command-and-control (41)
- `T1001` — Adversaries may obfuscate command and control traffic to make it more difficult to detect.
- `T1001.001` — Adversaries may add junk data to protocols used for command and control to make detection more difficult.
- `T1001.002` — Adversaries may use steganographic techniques to hide command and control traffic to make detection efforts mo
- `T1001.003` — Adversaries may impersonate legitimate protocols or web service traffic to disguise command and control activi
- `T1008` — Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inac
- `T1071` — Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blen
- `T1071.001` — Adversaries may communicate using application layer protocols associated with web traffic to avoid detection/n
- `T1071.002` — Adversaries may communicate using application layer protocols associated with transferring files to avoid dete
- `T1071.003` — Adversaries may communicate using application layer protocols associated with electronic mail delivery to avoi
- `T1071.004` — Adversaries may communicate using the Domain Name System (DNS) application layer protocol to avoid detection/n
- `T1071.005` — Adversaries may communicate using publish/subscribe (pub/sub) application layer protocols to avoid detection/n
- `T1090` — Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for
- `T1090.001` — Adversaries may use an internal proxy to direct command and control traffic between two or more systems in a c
- `T1090.002` — Adversaries may use an external proxy to act as an intermediary for network communications to a command and co
- `T1090.003` — Adversaries may chain together multiple proxies to disguise the source of malicious traffic.
- `T1090.004` — Adversaries may take advantage of routing schemes in Content Delivery Networks (CDNs) and other services which
- `T1092` — Adversaries can perform command and control between compromised hosts on potentially disconnected networks usi
- `T1095` — Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or amon
- `T1102` — Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compro
- `T1102.001` — Adversaries may use an existing, legitimate external Web service to host information that points to additional
- `T1102.002` — Adversaries may use an existing, legitimate external Web service as a means for sending commands to and receiv
- `T1102.003` — Adversaries may use an existing, legitimate external Web service as a means for sending commands to a compromi
- `T1104` — Adversaries may create multiple stages for command and control that are employed under different conditions or
- `T1105` — Adversaries may transfer tools or other files from an external system into a compromised environment.
- `T1132` — Adversaries may encode data to make the content of command and control traffic more difficult to detect.
- `T1132.001` — Adversaries may encode data with a standard data encoding system to make the content of command and control tr
- `T1132.002` — Adversaries may encode data with a non-standard data encoding system to make the content of command and contro
- `T1219` — An adversary may use legitimate remote access tools to establish an interactive command and control channel wi
- `T1219.001` — Adversaries may abuse Integrated Development Environment (IDE) software with remote development features to es
- `T1219.002` — An adversary may use legitimate desktop support software to establish an interactive command and control chann
- `T1219.003` — An adversary may use legitimate remote access hardware to establish an interactive command and control channel
- `T1568` — Adversaries may dynamically establish connections to command and control infrastructure to evade common detect
- `T1568.001` — Adversaries may use Fast Flux DNS to hide a command and control channel behind an array of rapidly changing IP
- `T1568.002` — Adversaries may make use of Domain Generation Algorithms (DGAs) to dynamically identify a destination domain f
- `T1568.003` — Adversaries may perform calculations on addresses returned in DNS results to determine which port and IP addre
- `T1571` — Adversaries may communicate using a protocol and port pairing that are typically not associated.
- `T1572` — Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid 
- `T1573` — Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on a
- `T1573.001` — Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic rather th
- `T1573.002` — Adversaries may employ a known asymmetric encryption algorithm to conceal command and control traffic rather t
- `T1665` — Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure.

### TA0040_impact (33)
- `T1485` — Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt avail
- `T1485.001` — Adversaries may modify the lifecycle policies of a cloud storage bucket to destroy all objects stored within.
- `T1486` — Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availa
- `T1489` — Adversaries may stop or disable services on a system to render those services unavailable to legitimate users.
- `T1490` — Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corr
- `T1491` — Adversaries may modify visual content available internally or externally to an enterprise network, thus affect
- `T1491.001` — An adversary may deface systems internal to an organization in an attempt to intimidate or mislead users, thus
- `T1491.002` — An adversary may deface systems external to an organization in an attempt to deliver messaging, intimidate, or
- `T1495` — Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices att
- `T1496` — Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may imp
- `T1496.001` — Adversaries may leverage the compute resources of co-opted systems to complete resource-intensive tasks, which
- `T1496.002` — Adversaries may leverage the network bandwidth resources of co-opted systems to complete resource-intensive ta
- `T1496.003` — Adversaries may leverage messaging services for SMS pumping, which may impact system and/or hosted service ava
- `T1496.004` — Adversaries may leverage compromised software-as-a-service (SaaS) applications to complete resource-intensive 
- `T1498` — Adversaries may perform Network Denial of Service (DoS) attacks to degrade or block the availability of target
- `T1498.001` — Adversaries may attempt to cause a denial of service (DoS) by directly sending a high-volume of network traffi
- `T1498.002` — Adversaries may attempt to cause a denial of service (DoS) by reflecting a high-volume of network traffic to a
- `T1499` — Adversaries may perform Endpoint Denial of Service (DoS) attacks to degrade or block the availability of servi
- `T1499.001` — Adversaries may launch a denial of service (DoS) attack targeting an endpoint's operating system (OS).
- `T1499.002` — Adversaries may target the different network services provided by systems to conduct a denial of service (DoS)
- `T1499.003` — Adversaries may target resource intensive features of applications to cause a denial of service (DoS), denying
- `T1499.004` — Adversaries may exploit software vulnerabilities that can cause an application or system to crash and deny ava
- `T1529` — Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems.
- `T1531` — Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utiliz
- `T1561` — Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrup
- `T1561.001` — Adversaries may erase the contents of storage devices on specific systems or in large numbers in a network to 
- `T1561.002` — Adversaries may corrupt or wipe the disk data structures on a hard drive necessary to boot a system; targeting
- `T1565` — Adversaries may insert, delete, or manipulate data in order to influence external outcomes or hide activity, t
- `T1565.001` — Adversaries may insert, delete, or manipulate data at rest in order to influence external outcomes or hide act
- `T1565.002` — Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hi
- `T1565.003` — Adversaries may modify systems in order to manipulate the data as it is accessed and displayed to an end user,
- `T1657` — Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, 
- `T1667` — Adversaries may flood targeted email addresses with an overwhelming volume of messages.

### TA0042_resource-development (47)
- `T1583` — Adversaries may buy, lease, rent, or obtain infrastructure that can be used during targeting.
- `T1583.001` — Adversaries may acquire domains that can be used during targeting.
- `T1583.002` — Adversaries may set up their own Domain Name System (DNS) servers that can be used during targeting.
- `T1583.003` — Adversaries may rent Virtual Private Servers (VPSs) that can be used during targeting.
- `T1583.004` — Adversaries may buy, lease, rent, or obtain physical servers that can be used during targeting.
- `T1583.005` — Adversaries may buy, lease, or rent a network of compromised systems that can be used during targeting.
- `T1583.006` — Adversaries may register for web services that can be used during targeting.
- `T1583.007` — Adversaries may purchase and configure serverless cloud infrastructure, such as Cloudflare Workers, AWS Lambda
- `T1583.008` — Adversaries may purchase online advertisements that can be abused to distribute malware to victims.
- `T1584` — Adversaries may compromise third-party infrastructure that can be used during targeting.
- `T1584.001` — Adversaries may hijack domains and/or subdomains that can be used during targeting.
- `T1584.002` — Adversaries may compromise third-party DNS servers that can be used during targeting.
- `T1584.003` — Adversaries may compromise third-party Virtual Private Servers (VPSs) that can be used during targeting.
- `T1584.004` — Adversaries may compromise third-party servers that can be used during targeting.
- `T1584.005` — Adversaries may compromise numerous third-party systems to form a botnet that can be used during targeting.
- `T1584.006` — Adversaries may compromise access to third-party web services that can be used during targeting.
- `T1584.007` — Adversaries may compromise serverless cloud infrastructure, such as Cloudflare Workers, AWS Lambda functions, 
- `T1584.008` — Adversaries may compromise third-party network devices that can be used during targeting.
- `T1585` — Adversaries may create and cultivate accounts with services that can be used during targeting.
- `T1585.001` — Adversaries may create and cultivate social media accounts that can be used during targeting.
- `T1585.002` — Adversaries may create email accounts that can be used during targeting.
- `T1585.003` — Adversaries may create accounts with cloud providers that can be used during targeting.
- `T1586` — Adversaries may compromise accounts with services that can be used during targeting.
- `T1586.001` — Adversaries may compromise social media accounts that can be used during targeting.
- `T1586.002` — Adversaries may compromise email accounts that can be used during targeting.
- `T1586.003` — Adversaries may compromise cloud accounts that can be used during targeting.
- `T1587` — Adversaries may build capabilities that can be used during targeting.
- `T1587.001` — Adversaries may develop malware and malware components that can be used during targeting.
- `T1587.002` — Adversaries may create self-signed code signing certificates that can be used during targeting.
- `T1587.003` — Adversaries may create self-signed SSL/TLS certificates that can be used during targeting.
- `T1587.004` — Adversaries may develop exploits that can be used during targeting.
- `T1588` — Adversaries may buy and/or steal capabilities that can be used during targeting.
- `T1588.001` — Adversaries may buy, steal, or download malware that can be used during targeting.
- `T1588.002` — Adversaries may buy, steal, or download software tools that can be used during targeting.
- `T1588.003` — Adversaries may buy and/or steal code signing certificates that can be used during targeting.
- `T1588.004` — Adversaries may buy and/or steal SSL/TLS certificates that can be used during targeting.
- `T1588.005` — Adversaries may buy, steal, or download exploits that can be used during targeting.
- `T1588.006` — Adversaries may acquire information about vulnerabilities that can be used during targeting.
- `T1588.007` — Adversaries may obtain access to generative artificial intelligence tools, such as large language models (LLMs
- `T1608` — Adversaries may upload, install, or otherwise set up capabilities that can be used during targeting.
- `T1608.001` — Adversaries may upload malware to third-party or adversary controlled infrastructure to make it accessible dur
- `T1608.002` — Adversaries may upload tools to third-party or adversary controlled infrastructure to make it accessible durin
- `T1608.003` — Adversaries may install SSL/TLS certificates that can be used during targeting.
- `T1608.004` — Adversaries may prepare an operational environment to infect systems that visit a website over the normal cour
- `T1608.005` — Adversaries may put in place resources that are referenced by a link that can be used during targeting.
- `T1608.006` — Adversaries may poison mechanisms that influence search engine optimization (SEO) to further lure staged capab
- `T1650` — Adversaries may purchase or otherwise acquire an existing access to a target system or network.

### TA0043_reconnaissance (45)
- `T1589` — Adversaries may gather information about the victim's identity that can be used during targeting.
- `T1589.001` — Adversaries may gather credentials that can be used during targeting.
- `T1589.002` — Adversaries may gather email addresses that can be used during targeting.
- `T1589.003` — Adversaries may gather employee names that can be used during targeting.
- `T1590` — Adversaries may gather information about the victim's networks that can be used during targeting.
- `T1590.001` — Adversaries may gather information about the victim's network domain(s) that can be used during targeting.
- `T1590.002` — Adversaries may gather information about the victim's DNS that can be used during targeting.
- `T1590.003` — Adversaries may gather information about the victim's network trust dependencies that can be used during targe
- `T1590.004` — Adversaries may gather information about the victim's network topology that can be used during targeting.
- `T1590.005` — Adversaries may gather the victim's IP addresses that can be used during targeting.
- `T1590.006` — Adversaries may gather information about the victim's network security appliances that can be used during targ
- `T1591` — Adversaries may gather information about the victim's organization that can be used during targeting.
- `T1591.001` — Adversaries may gather the victim's physical location(s) that can be used during targeting.
- `T1591.002` — Adversaries may gather information about the victim's business relationships that can be used during targeting
- `T1591.003` — Adversaries may gather information about the victim's business tempo that can be used during targeting.
- `T1591.004` — Adversaries may gather information about identities and roles within the victim organization that can be used 
- `T1592` — Adversaries may gather information about the victim's hosts that can be used during targeting.
- `T1592.001` — Adversaries may gather information about the victim's host hardware that can be used during targeting.
- `T1592.002` — Adversaries may gather information about the victim's host software that can be used during targeting.
- `T1592.003` — Adversaries may gather information about the victim's host firmware that can be used during targeting.
- `T1592.004` — Adversaries may gather information about the victim's client configurations that can be used during targeting.
- `T1593` — Adversaries may search freely available websites and/or domains for information about victims that can be used
- `T1593.001` — Adversaries may search social media for information about victims that can be used during targeting.
- `T1593.002` — Adversaries may use search engines to collect information about victims that can be used during targeting.
- `T1593.003` — Adversaries may search public code repositories for information about victims that can be used during targetin
- `T1594` — Adversaries may search websites owned by the victim for information that can be used during targeting.
- `T1595` — Adversaries may execute active reconnaissance scans to gather information that can be used during targeting.
- `T1595.001` — Adversaries may scan victim IP blocks to gather information that can be used during targeting.
- `T1595.002` — Adversaries may scan victims for vulnerabilities that can be used during targeting.
- `T1595.003` — Adversaries may iteratively probe infrastructure using brute-forcing and crawling techniques.
- `T1596` — Adversaries may search freely available technical databases for information about victims that can be used dur
- `T1596.001` — Adversaries may search DNS data for information about victims that can be used during targeting.
- `T1596.002` — Adversaries may search public WHOIS data for information about victims that can be used during targeting.
- `T1596.003` — Adversaries may search public digital certificate data for information about victims that can be used during t
- `T1596.004` — Adversaries may search content delivery network (CDN) data about victims that can be used during targeting.
- `T1596.005` — Adversaries may search within public scan databases for information about victims that can be used during targ
- `T1597` — Adversaries may search and gather information about victims from closed (e.g., paid, private, or otherwise not
- `T1597.001` — Adversaries may search private data from threat intelligence vendors for information that can be used during t
- `T1597.002` — Adversaries may purchase technical information about victims that can be used during targeting.
- `T1598` — Adversaries may send phishing messages to elicit sensitive information that can be used during targeting.
- `T1598.001` — Adversaries may send spearphishing messages via third-party services to elicit sensitive information that can 
- `T1598.002` — Adversaries may send spearphishing messages with a malicious attachment to elicit sensitive information that c
- `T1598.003` — Adversaries may send spearphishing messages with a malicious link to elicit sensitive information that can be 
- `T1598.004` — Adversaries may use voice communications to elicit sensitive information that can be used during targeting.
- `T1681` — Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about t

---

## MITRE ATT&CK Mobile — tactic index (124 skills, 12 tactics)

| Tactic dir | Skills |
|---|---|
| `TA0027_initial-access` | 11 |
| `TA0028_persistence` | 7 |
| `TA0029_privilege-escalation` | 3 |
| `TA0030_defense-evasion` | 32 |
| `TA0031_credential-access` | 5 |
| `TA0032_discovery` | 10 |
| `TA0033_lateral-movement` | 1 |
| `TA0034_impact` | 9 |
| `TA0035_collection` | 23 |
| `TA0036_exfiltration` | 3 |
| `TA0037_command-and-control` | 16 |
| `TA0041_execution` | 4 |

### TA0027_initial-access (11)
- `T1451` — Adversaries may gain access to mobile devices through transfers or swaps from victims’ phone numbers to advers
- `T1456` — Adversaries may gain access to a system through a user visiting a website over the normal course of browsing.
- `T1458` — Adversaries may move onto devices by exploiting or copying malware to devices connected via USB.
- `T1461` — An adversary with physical access to a mobile device may seek to bypass the device’s lockscreen.
- `T1474` — Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for th
- `T1474.001` — Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for th
- `T1474.002` — Adversaries may manipulate hardware components in products prior to receipt by a final consumer for the purpos
- `T1474.003` — Adversaries may manipulate application software prior to receipt by a final consumer for the purpose of data o
- `T1660` — Adversaries may send malicious content to users in order to gain access to their mobile devices.
- `T1661` — An adversary may push an update to a previously benign application to add malicious code.
- `T1664` — Adversaries may exploit software vulnerabilities to gain initial access to a mobile device.

### TA0028_persistence (7)
- `T1398` — Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.
- `T1577` — Adversaries may modify applications installed on a device to establish persistent access to a victim.
- `T1624` — Adversaries may establish persistence using system mechanisms that trigger execution based on specific events.
- `T1624.001` — Adversaries may establish persistence using system mechanisms that trigger execution based on specific events.
- `T1625` — Adversaries may execute their own malicious payloads by hijacking the way operating systems run applications.
- `T1625.001` — Adversaries may execute their own malicious payloads by hijacking the way an operating system runs application
- `T1645` — Adversaries may modify system software binaries to establish persistent access to devices.

### TA0029_privilege-escalation (3)
- `T1404` — Adversaries may exploit software vulnerabilities in order to elevate privileges.
- `T1626` — Adversaries may circumvent mechanisms designed to control elevated privileges to gain higher-level permissions
- `T1626.001` — Adversaries may abuse Android’s device administration API to obtain a higher degree of control over the device

### TA0030_defense-evasion (32)
- `T1406` — Adversaries may attempt to make a payload or file difficult to discover or analyze by encrypting, encoding, or
- `T1406.001` — Adversaries may use steganography techniques in order to prevent the detection of hidden information.
- `T1406.002` — Adversaries may perform software packing to conceal their code.
- `T1407` — Adversaries may download and execute dynamic code not included in the original application package after insta
- `T1516` — A malicious application can inject input to the user interface to mimic user interaction through the abuse of 
- `T1541` — Adversaries may abuse Android's `startForeground()` API method to maintain continuous sensor access.
- `T1575` — Adversaries may use Android’s Native Development Kit (NDK) to write native functions that can achieve executio
- `T1604` — Adversaries may use a compromised device as a proxy server to the Internet.
- `T1617` — Adversaries may utilize hooking to hide the presence of artifacts associated with their behaviors to evade det
- `T1627` — Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and env
- `T1627.001` — Adversaries may use a device’s geographical location to limit certain malicious behaviors.
- `T1628` — Adversaries may attempt to hide artifacts associated with their behaviors to evade detection.
- `T1628.001` — A malicious application could suppress its icon from being displayed to the user in the application launcher.
- `T1628.002` — Adversaries may attempt to avoid detection by hiding malicious behavior from the user.
- `T1628.003` — Adversaries may attempt to hide multimedia files from the user.
- `T1629` — Adversaries may maliciously modify components of a victim environment in order to hinder or disable defensive 
- `T1629.001` — Adversaries may abuse the Android device administration API to prevent the user from uninstalling a target app
- `T1629.002` — An adversary may seek to inhibit user interaction by locking the legitimate user out of the device.
- `T1629.003` — Adversaries may disable security tools to avoid potential detection of their tools and activities.
- `T1630` — Adversaries may delete, alter, or hide generated artifacts on a device, including files, jailbreak status, or 
- `T1630.001` — Adversaries may include functionality in malware that uninstalls the malicious application from the device.
- `T1630.002` — Adversaries may wipe a device or delete individual files in order to manipulate external outcomes or hide acti
- `T1630.003` — An adversary could use knowledge of the techniques used by security software to evade detection.
- `T1631` — Adversaries may inject code into processes in order to evade process-based defenses or even elevate privileges
- `T1631.001` — Adversaries may inject malicious code into processes via ptrace (process trace) system calls in order to evade
- `T1632` — Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execu
- `T1632.001` — Adversaries may modify code signing policies to enable execution of applications signed with unofficial or unk
- `T1633` — Adversaries may employ various means to detect and avoid virtualization and analysis environments.
- `T1633.001` — Adversaries may employ various system checks to detect and avoid virtualization and analysis environments.
- `T1655` — Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to 
- `T1655.001` — Adversaries may match or approximate the name or location of legitimate files or resources when naming/placing
- `T1670` — Adversaries may carry out malicious operations using virtualization solutions to escape from Android sandboxes

### TA0031_credential-access (5)
- `T1417.002` — Adversaries may mimic common operating system GUI components to prompt users for sensitive information with a 
- `T1634` — Adversaries may search common password storage locations to obtain user credentials.
- `T1634.001` — Adversaries may collect keychain data from an iOS device to acquire credentials.
- `T1635` — Adversaries can steal user application access tokens as a means of acquiring credentials to access remote syst
- `T1635.001` — Adversaries may register Uniform Resource Identifiers (URIs) to intercept sensitive data.

### TA0032_discovery (10)
- `T1418` — Adversaries may attempt to get a listing of applications that are installed on a device.
- `T1418.001` — Adversaries may attempt to get a listing of security applications and configurations that are installed on a d
- `T1420` — Adversaries may enumerate files and directories or search in specific device locations for desired information
- `T1421` — Adversaries may attempt to get a listing of network connections to or from the compromised device they are cur
- `T1422` — Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses
- `T1422.001` — Adversaries may check for Internet connectivity on compromised systems.
- `T1422.002` — Adversaries may search for information about Wi-Fi networks, such as network names and passwords, on compromis
- `T1423` — Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vuln
- `T1424` — Adversaries may attempt to get information about running processes on a device.
- `T1426` — Adversaries may attempt to get detailed information about a device’s operating system and hardware, including 

### TA0033_lateral-movement (1)
- `T1428` — Adversaries may exploit remote services of enterprise servers, workstations, or other resources to gain unauth

### TA0034_impact (9)
- `T1464` — Adversaries may perform Network Denial of Service (DoS) attacks to degrade or block the availability of target
- `T1471` — An adversary may encrypt files stored on a mobile device to prevent the user from accessing them.
- `T1582` — Adversaries may delete, alter, or send SMS messages without user authorization.
- `T1640` — Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utiliz
- `T1641` — Adversaries may insert, delete, or alter data in order to manipulate external outcomes or hide activity.
- `T1641.001` — Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hi
- `T1642` — Adversaries may perform Endpoint Denial of Service (DoS) attacks to degrade or block the availability of servi
- `T1643` — Adversaries may generate outbound traffic from devices.
- `T1662` — Adversaries may destroy data and files on specific devices or in large numbers to interrupt availability to sy

### TA0035_collection (23)
- `T1409` — Adversaries may try to access and collect application data resident on the device.
- `T1414` — Adversaries may abuse clipboard manager APIs to obtain sensitive information copied to the device clipboard.
- `T1417` — Adversaries may use methods of capturing user input to obtain credentials or collect information.
- `T1417.001` — Adversaries may log user keystrokes to intercept credentials or other information from the user as the user ty
- `T1429` — Adversaries may capture audio to collect information by leveraging standard operating system APIs of a mobile 
- `T1430` — Adversaries may track a device’s physical location through use of standard operating system APIs via malicious
- `T1430.001` — An adversary may use access to cloud services (e.g.
- `T1430.002` — Adversaries may exploit the lack of authentication in signaling system network nodes to track the location of 
- `T1453` — Adversaries may abuse accessibility features in Android devices to steal sensitive data and to spread malware 
- `T1512` — An adversary can leverage a device’s cameras to gather information by capturing video recordings.
- `T1513` — Adversaries may use screen capture to collect additional information about a target device, such as applicatio
- `T1517` — Adversaries may collect data within notifications sent by the operating system or other applications.
- `T1532` — Adversaries may compress and/or encrypt data that is collected prior to exfiltration.
- `T1533` — Adversaries may search local system sources, such as file systems or local databases, to find files of interes
- `T1616` — Adversaries may make, forward, or block phone calls without user authorization.
- `T1636` — Adversaries may utilize standard operating system APIs to collect data from permission-backed data stores on a
- `T1636.001` — Adversaries may utilize standard operating system APIs to gather calendar entry data.
- `T1636.002` — Adversaries may utilize standard operating system APIs to gather call log data.
- `T1636.003` — Adversaries may utilize standard operating system APIs to gather contact list data.
- `T1636.004` — Adversaries may utilize standard operating system APIs to gather SMS messages.
- `T1636.005` — Adversaries may utilize standard operating system APIs to gather account data.
- `T1638` — Adversaries may attempt to position themselves between two or more networked devices to support follow-on beha
- `T1676` — Adversaries may abuse the “linked devices” feature on messaging applications, such as Signal and WhatsApp, to 

### TA0036_exfiltration (3)
- `T1639` — Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and 
- `T1639.001` — Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the exi
- `T1646` — Adversaries may steal data by exfiltrating it over an existing command and control channel.

### TA0037_command-and-control (16)
- `T1437` — Adversaries may communicate using application layer protocols to avoid detection/network filtering by blending
- `T1437.001` — Adversaries may communicate using application layer protocols associated with web protocols traffic to avoid d
- `T1481` — Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compro
- `T1481.001` — Adversaries may use an existing, legitimate external Web service to host information that points to additional
- `T1481.002` — Adversaries may use an existing, legitimate external Web service channel as a means for sending commands to an
- `T1481.003` — Adversaries may use an existing, legitimate external Web service channel as a means for sending commands to a 
- `T1509` — Adversaries may generate network traffic using a protocol and port pairing that are typically not associated.
- `T1521` — Adversaries may explicitly employ a known encryption algorithm to conceal command and control traffic rather t
- `T1521.001` — Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic, rather t
- `T1521.002` — Adversaries may employ a known asymmetric encryption algorithm to conceal command and control traffic, rather 
- `T1521.003` — Adversaries may use SSL Pinning to protect the C2 traffic from being intercepted and analyzed.
- `T1544` — Adversaries may transfer tools or other files from an external system onto a compromised device to facilitate 
- `T1637` — Adversaries may dynamically establish connections to command and control infrastructure to evade common detect
- `T1637.001` — Adversaries may use Domain Generation Algorithms (DGAs) to procedurally generate domain names for uses such as
- `T1644` — Adversaries may communicate with compromised devices using out of band data streams.
- `T1663` — Adversaries may use legitimate remote access software, such as `VNC`, `TeamViewer`, `AirDroid`, `AirMirror`, e

### TA0041_execution (4)
- `T1603` — Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious 
- `T1623` — Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries.
- `T1623.001` — Adversaries may abuse Unix shell commands and scripts for execution.
- `T1658` — Adversaries may exploit software vulnerabilities in client applications to execute code.

---

## MITRE ATT&CK ICS — tactic index (83 skills, 12 tactics)

| Tactic dir | Skills |
|---|---|
| `TA0100_collection` | 10 |
| `TA0101_command-and-control` | 3 |
| `TA0102_discovery` | 5 |
| `TA0103_evasion` | 6 |
| `TA0104_execution` | 10 |
| `TA0105_impact` | 12 |
| `TA0106_impair-process-control` | 3 |
| `TA0107_inhibit-response-function` | 12 |
| `TA0108_initial-access` | 12 |
| `TA0109_lateral-movement` | 4 |
| `TA0110_persistence` | 5 |
| `TA0111_privilege-escalation` | 1 |

### TA0100_collection (10)
- `T0801` — Adversaries may gather information about the physical process state.
- `T0802` — Adversaries may automate collection of industrial environment information using tools or scripts.
- `T0811` — Adversaries may target and collect data from information repositories.
- `T0830` — Adversaries with privileged network access may seek to modify network traffic in real time using adversary-in-
- `T0845` — Adversaries may attempt to upload a program from a PLC to gather information about an industrial process.
- `T0852` — Adversaries may attempt to perform screen capture of devices in the control system environment.
- `T0861` — Adversaries may collect point and tag values to gain a more comprehensive understanding of the process environ
- `T0868` — Adversaries may gather information about a PLCs or controllers current operating mode.
- `T0877` — Adversaries may seek to capture process values related to the inputs and outputs of a PLC.
- `T0893` — Adversaries may target and collect data from local system sources, such as file systems, configuration files, 

### TA0101_command-and-control (3)
- `T0869` — Adversaries may establish command and control capabilities over commonly used application layer protocols such
- `T0884` — Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for
- `T0885` — Adversaries may communicate over a commonly used port to bypass firewalls or network detection systems and to 

### TA0102_discovery (5)
- `T0840` — Adversaries may perform network connection enumeration to discover information about device communication patt
- `T0842` — Network sniffing is the practice of using a network interface on a computer system to monitor or capture infor
- `T0846` — Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier
- `T0887` — Adversaries may seek to capture radio frequency (RF) communication used for remote control and reporting in di
- `T0888` — An adversary may attempt to get detailed information about remote systems and their peripherals, such as make/

### TA0103_evasion (6)
- `T0820` — Adversaries may exploit a software vulnerability to take advantage of a programming error in a program, servic
- `T0849` — Adversaries may use masquerading to disguise a malicious application or executable as another file, to avoid o
- `T0851` — Adversaries may deploy rootkits to hide the presence of programs, files, network connections, services, driver
- `T0856` — Adversaries may spoof reporting messages in control system environments for evasion and to impair process cont
- `T0872` — Adversaries may attempt to remove indicators of their presence on a system in an effort to cover their tracks.
- `T0894` — Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with

### TA0104_execution (10)
- `T0807` — Adversaries may utilize command-line interfaces (CLIs) to interact with systems and execute commands.
- `T0821` — Adversaries may modify the tasking of a controller to allow for the execution of their own programs.
- `T0823` — Adversaries may attempt to gain access to a machine via a Graphical User Interface (GUI) to enhance execution 
- `T0834` — Adversaries may directly interact with the native OS application programming interface (API) to access system 
- `T0853` — Adversaries may use scripting languages to execute arbitrary code in the form of a pre-written script or in th
- `T0858` — Adversaries may change the operating mode of a controller to gain additional access to engineering functions s
- `T0863` — Adversaries may rely on a targeted organizations user interaction for the execution of malicious code.
- `T0871` — Adversaries may attempt to leverage Application Program Interfaces (APIs) used for communication between contr
- `T0874` — Adversaries may hook into application programming interface (API) functions used by processes to redirect call
- `T0895` — Adversaries may leverage AutoRun functionality or scripts to execute malicious code.

### TA0105_impact (12)
- `T0813` — Adversaries may cause a denial of control to temporarily prevent operators and engineers from interacting with
- `T0815` — Adversaries may cause a denial of view in attempt to disrupt and prevent operator oversight on the status of a
- `T0826` — Adversaries may attempt to disrupt essential components or systems to prevent owner and operator from deliveri
- `T0827` — Adversaries may seek to achieve a sustained loss of control or a runaway condition in which operators cannot i
- `T0828` — Adversaries may cause loss of productivity and revenue through disruption and even damage to the availability 
- `T0829` — Adversaries may cause a sustained or permanent loss of view where the ICS equipment will require local, hands-
- `T0831` — Adversaries may manipulate physical process control within the industrial environment.
- `T0832` — Adversaries may attempt to manipulate the information reported back to operators or controllers.
- `T0837` — Adversaries may compromise protective system functions designed to prevent the effects of faults and abnormal 
- `T0879` — Adversaries may cause damage and destruction of property to infrastructure, equipment, and the surrounding env
- `T0880` — Adversaries may compromise safety system functions designed to maintain safe operation of a process when unacc
- `T0882` — Adversaries may steal operational information on a production environment as a direct mission outcome for pers

### TA0106_impair-process-control (3)
- `T0806` — Adversaries may repetitively or successively change I/O point values to perform an action.
- `T0836` — Adversaries may modify parameters used to instruct industrial control system devices.
- `T0855` — Adversaries may send unauthorized command messages to instruct control system assets to perform actions outsid

### TA0107_inhibit-response-function (12)
- `T0800` — Adversaries may activate firmware update mode on devices to prevent expected response functions from engaging 
- `T0803` — Adversaries may block a command message from reaching its intended target to prevent command execution.
- `T0804` — Adversaries may block or prevent a reporting message from reaching its intended target.
- `T0805` — Adversaries may block access to serial COM to prevent instructions or configurations from reaching target devi
- `T0809` — Adversaries may perform data destruction over the course of an operation.
- `T0814` — Adversaries may perform Denial-of-Service (DoS) attacks to disrupt expected device functionality.
- `T0816` — Adversaries may forcibly restart or shutdown a device in an ICS environment to disrupt and potentially negativ
- `T0835` — Adversaries may manipulate the I/O image of PLCs through various means to prevent them from functioning as exp
- `T0838` — Adversaries may modify alarm settings to prevent alerts that may inform operators of their presence or to prev
- `T0878` — Adversaries may target protection function alarms to prevent them from notifying operators of critical conditi
- `T0881` — Adversaries may stop or disable services on a system to render those services unavailable to legitimate users.
- `T0892` — Adversaries may modify software and device credentials to prevent operator and responder access.

### TA0108_initial-access (12)
- `T0817` — Adversaries may gain access to a system during a drive-by compromise, when a user visits a website as part of 
- `T0819` — Adversaries may leverage weaknesses to exploit internet-facing software for initial access into an industrial 
- `T0822` — Adversaries may leverage external remote services as a point of initial access into your network.
- `T0847` — Adversaries may move onto systems, such as those separated from the enterprise network, by copying malware to 
- `T0848` — Adversaries may setup a rogue master to leverage control server functions to communicate with outstations.
- `T0860` — Adversaries may perform wireless compromise as a method of gaining communications and unauthorized access to a
- `T0862` — Adversaries may perform supply chain compromise to gain control systems environment access by means of infecte
- `T0864` — Adversaries may target devices that are transient across ICS networks and external networks.
- `T0865` — Adversaries may use a spearphishing attachment, a variant of spearphishing, as a form of a social engineering 
- `T0866` — Adversaries may exploit a software vulnerability to take advantage of a programming error in a program, servic
- `T0883` — Adversaries may gain access into industrial environments through systems exposed directly to the internet for 
- `T0886` — Adversaries may leverage remote services to move between assets and network segments.

### TA0109_lateral-movement (4)
- `T0812` — Adversaries may leverage manufacturer or supplier set default credentials on control system devices.
- `T0843` — Adversaries may perform a program download to transfer a user program to a controller.
- `T0867` — Adversaries may transfer tools or other files from one system to another to stage adversary tools or other fil
- `T0891` — Adversaries may leverage credentials that are hardcoded in software or firmware to gain an unauthorized intera

### TA0110_persistence (5)
- `T0839` — Adversaries may install malicious or vulnerable firmware onto modular hardware devices.
- `T0857` — System firmware on modern assets is often designed with an update feature.
- `T0859` — Adversaries may steal the credentials of a specific user or service account using credential access techniques
- `T0873` — Adversaries may attempt to infect project files with malicious code.
- `T0889` — Adversaries may modify or add a program on a controller to affect how it interacts with the physical process, 

### TA0111_privilege-escalation (1)
- `T0890` — Adversaries may exploit software vulnerabilities in an attempt to elevate privileges.
