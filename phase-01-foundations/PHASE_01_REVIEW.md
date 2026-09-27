# 🦅 PHASE 1 REVIEW — Core Foundations (Weeks 1–6 / Days 001–030)

> **Phase:** Phase 01 — Core Foundations: Networking + Linux + Windows + Web  
> **Status:** 🟢 **Completed & Reviewed**  
> **Deliverable:** [Deliverable 1: Multi-OS Security Lab Environment](../../projects/project-01-security-lab-environment/README.md)  
> **Next Milestone:** Phase 02 — Web Application Security + Reconnaissance (Week 07 / Day 031)

---

## 🧭 The Big Picture

Phase 1 answers one central question: **What actually happens when a person uses a computer on a network, and where can it go wrong?** Each week added one layer to that answer.

```text
Week 1: Networking      → How messages travel between machines
Week 2: Linux           → How a server is organized, run, and investigated
Week 3: Windows         → The same questions on the system most enterprises use
Weeks 4–5: Web Security → How websites remember you and decide what you can do
Week 6: Tooling         → The workbench used for everything after this
```

> **The Core Rule of Phase 1:**  
> Every system has to decide **who you are** and **what you're allowed to do**, and it **records what happened**. Security work is checking those decisions and reading those records.

---

## 🌐 Week 1 — Networking & Protocols

### What it is
Networking is how computers agree on rules (protocols) to send data to each other. The internet runs on TCP/IP, and we describe it with the OSI model, a seven-layer map used to say where a problem lives.

### How it works, in one story
When your laptop joins Wi-Fi, **DHCP** gives it an IP address (its home address), a gateway, and a DNS server. You type a website name and **DNS** turns it into an IP address. **ARP** finds the MAC address of your router on the local network. **TCP** opens a reliable connection with a three-way handshake (`SYN` → `SYN-ACK` → `ACK`) to a port (a numbered door, like 443 for HTTPS), while **UDP** is used when speed matters more than reliability. Your router uses **NAT** to swap your private address for its public one, **routing** carries the packets hop by hop, and **ICMP** reports errors. **HTTP** is what the browser and server actually say, and **TLS** wraps it in encryption and checks the server's certificate so it becomes HTTPS. **Firewalls** allow or block traffic by rules, and **proxies** sit in the middle. **CIDR** and **subnetting** divide address space into sections, so you can place firewalls between them.

### Why it matters for security
Many of these protocols trust answers without proof, which is why **ARP spoofing**, **rogue DHCP**, and **fake DNS answers** are possible. Open ports are the machine's attack surface, and segmentation limits how far an intruder can move. Packet capture with `tcpdump` and `Wireshark` shows the ground truth: plain HTTP is fully readable, while HTTPS hides the content but still reveals where you went through DNS and SNI.

> **Remember it like this:**  
> DHCP gives you an address, DNS finds the name, ARP finds the neighbour, TCP opens the door, TLS locks it, and the firewall decides whether you get in.

---

## 🐧 Week 2 — Linux Fundamentals

### What it is
Linux organizes everything as files in one tree starting at `/`. Every file has an owner, a group, and permissions (read, write, execute for owner, group, and others), and every running program is a process owned by some user. **Root** (UID 0) bypasses permission checks entirely.

### How it works
Background programs are services, managed by **systemd** through unit files and controlled with `systemctl`. **Cron** runs jobs on a schedule. **Environment variables** are the settings each process inherits, and `PATH` decides where commands are found. `/proc` is a live view of every process, including its program file, working folder, and open connections, and `/sys` shows hardware and kernel settings, which you change with `sysctl`. Logs in `/var/log` and the systemd journal record the past, with `auth.log` holding logins and `sudo` use. **Bash** ties it together with pipes, redirection, conditions, loops, and scripts.

The security model is layered: users and permissions (DAC), process isolation, least privilege through `sudo`, AppArmor or SELinux (MAC, which limits even root-owned processes), the firewall, patching, and `auditd`.

### Why it matters for security
Most Linux problems are simple misconfigurations: a world-writable file, a script run by root that others can edit, a service running as root without needing to, or an overly broad `sudo` rule. In an investigation, you follow the order of volatility: capture processes and connections first, trace a suspicious PID through `/proc`, check services, cron, users, `/tmp`, `/etc/hosts`, and logs, then hash your evidence and build a timeline. We also created `baseline_check.sh`, which automates many of these checks.

> **Remember it like this:**  
> On Linux, check who owns it, who can write to it, what runs it, and what the logs say.

---

## 🪟 Week 3 — Windows Internals & PowerShell

### What it is
Windows answers the same questions as Linux with different names. **SYSTEM** is the most powerful local account, similar to root. Core programs live in `C:\Windows\System32`, and user files live in `C:\Users\<name>`.

### How it works
Every process has a PID, parent, path, command line, and user, and knowing normal is the key skill: exactly one `lsass.exe`, `svchost.exe` always started by `services.exe` from `System32`, and no Office apps launching command shells. Services are managed by `services.exe` (the Service Control Manager), each with a program path, start type, and account, often `LocalSystem`. The **registry** is Windows' central settings database, organized into hives (`HKLM` for the machine, `HKCU` for the user), keys, and values. **ACLs** are guest lists on every file, folder, and registry key, where each entry says who, allow or deny, and which rights. **Scheduled tasks** are made of a trigger, an action, and the account that runs them. Event logs record the past, and **Sysmon** adds much richer detail, such as process hashes, network connections, and DNS queries per process.

### Why it matters for security
A trusted name in the wrong place isn't trusted. Services, tasks, and Run keys are the places things set themselves to start automatically. Key events to recognize are:
* `4624` & `4625`: Logon success and failure
* `4720` & `4732`: Account created and added to a privileged group
* `4688`: Process created (command-line auditing)
* `7045`: Service installed
* `106`: Scheduled task registered
* `4104`: PowerShell Script Block Logging
* `1102`: Security audit log cleared

Good evidence must be switched on before an incident, through audit policy, command-line logging, Script Block Logging, and Sysmon.

> **Remember it like this:**  
> On Windows, check the name, path, parent, and account, then let the event logs and Sysmon tell you when it appeared.

---

## 🌐 Weeks 4–5 — Web Architecture & Security

### What it is
Websites are built on HTTP, which forgets you after every request. Everything else in these weeks exists to handle that.

### How it works
The server gives your browser a cookie carrying a random session ID, while the real information stays on the server. **Authentication** proves who you are at login, and **authorization** checks every request to see whether you're allowed to do that specific thing (`401` means "who are you?", `403` means "no"). The browser's **Same-Origin Policy (SOP)** stops one site from reading another's data, **CORS** lets a server carefully relax that, and **CSRF** abuses the fact that cookies travel automatically, which is why `SameSite` cookies and CSRF tokens exist. **JWTs** are signed, readable tokens that carry claims, and **OAuth** gives an app a limited, revocable "valet key" to your account, with **OIDC** adding login on top. Front ends talk to back ends through REST APIs, GraphQL queries, and WebSockets for live two-way messages. In front of it all, **reverse proxies** handle TLS, load balancing, and hiding servers, and **CDNs** keep copies worldwide for speed and DDoS protection.

### Why it matters for security
Everything the client sends can be changed, so every important check must happen on the server. **Broken access control** is the top web risk, and **BOLA/IDOR** is the top API risk; both are the same mistake of checking login without checking ownership. Many other problems are configuration mistakes: missing cookie flags, CORS that trusts any origin, JWTs whose signature isn't properly verified, loose OAuth redirect addresses, trusting `X-Forwarded-For`, or an origin server reachable around its CDN. In our Flask lab, a single missing check exposed another user's note.

> **Remember it like this:**  
> HTTP forgets you, cookies remind it, authentication asks who you are, and authorization asks, on every request, whether you're allowed.

---

## 🛠️ Week 6 — Security Tooling Foundation

### What it is
Week 6 is the workbench: **Kali Linux** as a VM with security tools, set up on a host-only network so lab work can't leak onto real networks, and snapshotted before big changes. The rest of the week (Nmap, Burp Suite, Git, Python, shell scripting, networking utilities, and evidence collection) builds the operational execution skills for Phase 2.

```text
Kali Linux           → The workbench where most tools live
Networking utilities → Small everyday tools (ip, ss, ping, traceroute, dig, curl, tcpdump)
Nmap                 → Finds which machines and services exist
Burp Suite           → Sits in the middle of web traffic so you can study and tamper with it
Python basics        → Write your own small custom tools and automation scripts
Shell scripting      → Automate repeated command-line investigation workflows
Git                  → Save, track, and secure your work (B.L.A.D.E repository)
Evidence collection  → Prove what you did, maintain chain of custody, and hash artifacts
```

> **Remember it like this:**  
> Build the lab first, test only what you're allowed to, and save cryptographic proof of everything you do.

---

## 🔗 How the Whole Phase Connects

```text
Network (Week 1)
       │  A packet reaches a port
       ▼
Host (Weeks 2–3)
       │  A service behind that port runs as some user, on Linux or Windows
       ▼
Application (Weeks 4–5)
       │  The service is a web app that must authenticate and authorize every request
       ▼
Evidence (All Weeks)
       │  Packets, /proc, event logs, Sysmon, auth.log, web logs record what happened
       ▼
Tools (Week 6)
          The workbench to observe, test, and document all of the above
```

**In plain words:**  
Traffic crosses the network to a port. Behind that port is a service on a Linux or Windows host, running as some account. Often that service is a web application, which must decide who you are and what you're allowed to do. At every layer, something is recorded, and your tools let you see it. Phase 2 builds straight on this: recon finds the ports and web applications, and web security tests their authentication and authorization.

---

## 📚 Self-Study Gaps to Review Before Phase 2

| Week | Topic | Where to Study | Primary Focus |
| :---: | :--- | :--- | :--- |
| **2** | **SUID/SGID** | `man chmod` (SETUID AND SETGID BITS) | How binaries execute under owner/group credentials and why GTFOBins exist |
| **2** | **SSH Hardening** | `man ssh`, `man sshd_config` | Disabling password authentication, enforcing public key auth, PermitRootLogin no |
| **3** | **PowerShell** | Microsoft Learn: "PowerShell 101" | Pipeline object passing, `Get-CimInstance`, execution policies, and script blocks |
| **3** | **Registry Internals** | Microsoft Learn: "Windows registry information" | HKLM vs HKCU, Run/RunOnce persistence keys, and SAM hive offline storage |
| **3** | **Security Model, Tokens, UAC, WMI** | Microsoft Learn: "Access tokens", "UAC", "WMI" | Primary vs Impersonation tokens, Integrity levels, and WMI event subscriptions |
| **6** | **Nmap, Burp, Git, Python** | Nmap Book, PortSwigger Academy, Pro Git, Python docs | TCP SYN scan flags, intercept proxy CA setup, .gitignore hygiene, socket scripts |

---

## 🧠 Quick Self-Test Assessment

1. **Walk through what happens on the network when you open https://example.com on a laptop that just joined Wi-Fi.**  
   *Answer:* DHCP allocates IP, subnet mask, default gateway, and DNS server. DNS queries resolve `example.com` to an IP address. ARP resolves the local gateway's IP to its MAC address. TCP completes the 3-way handshake (`SYN` → `SYN-ACK` → `ACK`) on port 443. TLS performs cryptographic negotiation (certificate verification, key exchange, symmetric session key agreement). Encrypted HTTP GET request is transmitted; server processes it and returns encrypted HTTP 200 OK response with HTML payload.

2. **Why is a script that root runs from cron, but that anyone can edit, dangerous?**  
   *Answer:* Any standard unprivileged user can modify the script's contents. When the cron daemon triggers the scheduled job, it executes the modified script in root's security context (UID 0), allowing an instant local privilege escalation to full root control.

3. **How would you tell a fake svchost.exe from a real one?**  
   *Answer:* Check the file path, parent process, and command-line arguments: A legitimate `svchost.exe` must live strictly in `C:\Windows\System32\`, must always have `services.exe` as its parent process, and must be invoked with the `-k` service group flag. Any `svchost.exe` running from `C:\Users\`, `C:\Temp\`, spawned by an Office application or `cmd.exe`, or lacking `-k` is malicious.

4. **What's the difference between authentication and authorization? Give a 401 and a 403 example.**  
   *Answer:* Authentication verifies identity ("Who are you?"), returning HTTP `401 Unauthorized` when credentials are missing or invalid (e.g. attempting to view a profile without logging in). Authorization verifies permissions ("What are you allowed to do?"), returning HTTP `403 Forbidden` when identity is verified but the user lacks permission to access that specific resource (e.g. a regular employee trying to access `/admin/payroll`).

5. **Why must important security checks happen on the server rather than in the browser?**  
   *Answer:* The client environment is entirely under the user's/attacker's control. Attackers can bypass client-side validation, modify JavaScript code, intercept and tamper with HTTP requests via Burp Suite, or craft raw API requests directly. Only server-side enforcement guarantees security boundaries.

6. **Name one Linux log and one Windows event ID you'd check to see whether a new admin account was created.**  
   *Answer:* On Linux, check `/var/log/auth.log` (or `journalctl -u systemd-logind` / `useradd` entries). On Windows, check Security Event Log **Event ID 4720** (A user account was created) and **Event ID 4732** / **4728** (A member was added to a security-enabled local or global administrative group).
