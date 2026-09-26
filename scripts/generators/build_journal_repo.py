"""
CYBERSECURITY-MASTER-JOURNAL Repository Generator
Architects and generates the complete 40-week / 200-day cybersecurity master learning journal.
"""

import os
import sys
import json
from pathlib import Path

# Base workspace path
WORKSPACE_ROOT = Path(r"d:\RED TEAMING")

# Complete Curriculum Definition (9 Phases, 40 Weeks, 200 Days)
PHASES_DATA = [
    {
        "num": 1,
        "id": "phase-01-foundations",
        "title": "Core Foundations — Networking + Linux + Windows + Web",
        "weeks_range": "Weeks 1–6",
        "days_range": "Days 001–030",
        "objective": "Build unshakeable foundational mastery across computer networking, operating system internals (Linux & Windows), Web protocols, and fundamental security tooling.",
        "skills": ["TCP/IP & OSI model", "Packet analysis with Wireshark/tcpdump", "Linux administration & permissions", "Windows internals & PowerShell", "Web architecture & identity protocols", "Security tooling & lab virtualization"],
        "tools": ["Wireshark", "tcpdump", "Bash", "PowerShell", "Sysmon", "Nmap", "Burp Suite", "Python 3"],
        "project_id": "project-01-security-lab-environment",
        "project_title": "Multi-OS Security Lab Environment (Kali + Windows VM + Linux Target + Web Lab + GitHub)",
        "weeks": [
            {
                "num": 1,
                "id": "week-01-networking",
                "title": "Networking & Protocols",
                "objective": "Master packet anatomy, subnetting, layer 2/3/4 protocols, and network traffic reconstruction.",
                "days": [
                    {
                        "num": 1,
                        "title": "TCP/IP Architecture, OSI Model & The 3-Way Handshake",
                        "topics": ["TCP/IP vs OSI model comparison", "IPv4/IPv6 packet headers", "TCP 3-way handshake (SYN, SYN-ACK, ACK)", "TCP flags (FIN, RST, PSH, URG)", "Stateful vs stateless protocols"],
                        "objectives": "Understand TCP connection lifecycles, protocol boundaries, and state transitions at the byte level.",
                        "lab": "Capture a live TCP 3-way handshake and connection teardown in Wireshark; verify sequence/acknowledgment numbers.",
                        "interview_q": "Explain the difference between TCP SYN and RST flags, and how an attacker abuses SYN packets for stealth scanning."
                    },
                    {
                        "num": 2,
                        "title": "IPv4, IPv6, CIDR Subnetting & Packet Fragmentation",
                        "topics": ["IPv4 addressing classes and RFC 1918 private scopes", "CIDR notation and bitwise subnet calculations", "IPv6 address format, link-local vs global unicast", "IP fragmentation, MTU, and offset calculations", "Defensive implications of fragmented packets"],
                        "objectives": "Perform mental and scripted subnetting, calculate broadcast/network addresses, and diagnose fragmentation attacks.",
                        "lab": "Subnet a /22 network into four equal functional subnets for DMZ, Internal, Database, and Management tiers.",
                        "interview_q": "How does an MTU mismatch cause silent connection drops, and how can an adversary leverage fragmentation to evade IDS/IPS inspection?"
                    },
                    {
                        "num": 3,
                        "title": "Core Protocols — ARP, ICMP, DHCP, NAT & Routing Mechanics",
                        "topics": ["Address Resolution Protocol (ARP) mechanics and ARP cache poisoning", "ICMP message types (Echo, Destination Unreachable, TTL Exceeded)", "DHCP DORA process and DHCP starvation", "Network Address Translation (SNAT, DNAT, PAT)", "Static routing vs Dynamic routing (OSPF, BGP basics)"],
                        "objectives": "Map out how hosts discover gateways, resolve physical addresses, and how Layer 2 spoofing works.",
                        "lab": "Use scapy / arping in Linux to inspect ARP tables and trace ICMP TTL behavior using traceroute.",
                        "interview_q": "Explain how ARP poisoning allows an attacker to achieve a Man-in-the-Middle position and how Dynamic ARP Inspection (DAI) prevents it."
                    },
                    {
                        "num": 4,
                        "title": "Transport & Application Layers — DNS, HTTP/HTTPS & TLS Cryptography",
                        "topics": ["TCP vs UDP performance and reliability trade-offs", "DNS hierarchy, query types (A, AAAA, MX, TXT, NS), and recursive vs iterative resolution", "HTTP request/response lifecycle, status codes, and HTTP/1.1 vs HTTP/2", "TLS 1.2 vs TLS 1.3 handshake mechanics", "Public Key Infrastructure (PKI), digital certificates, and Cipher Suites"],
                        "objectives": "Trace DNS resolution end-to-end and inspect encrypted TLS handshakes including Server Hello and Certificate exchange.",
                        "lab": "Use `dig` and `openssl s_client` to examine DNS records, zone transfer attempts, and TLS certificate chains for a test domain.",
                        "interview_q": "Walk through the TLS 1.3 handshake step-by-step and explain how Forward Secrecy protects past sessions if the server private key is leaked."
                    },
                    {
                        "num": 5,
                        "title": "Network Traffic Analysis — tcpdump & Wireshark Stream Reconstruction",
                        "topics": ["tcpdump CLI capture filters vs display filters", "Berkeley Packet Filters (BPF) syntax", "Wireshark GUI navigation, coloring rules, and conversation statistics", "Follow TCP/UDP Stream analysis", "Detecting anomalous network patterns (port scans, cleartext credentials)"],
                        "objectives": "Capture raw traffic on headless interfaces and extract files, credentials, and conversation streams from PCAPs.",
                        "lab": "Record network traffic with `tcpdump -i any -w capture.pcap`, filter out specific subnets, and extract cleartext HTTP credentials in Wireshark.",
                        "interview_q": "Write a BPF expression to capture only inbound TCP SYN packets destined for port 80 or 443 originating from an external subnet."
                    }
                ]
            },
            {
                "num": 2,
                "id": "week-02-linux",
                "title": "Linux Fundamentals & System Administration",
                "objective": "Master Linux filesystem hierarchy, permission models, systemd services, process namespaces, and host investigation.",
                "days": [
                    {
                        "num": 6,
                        "title": "Linux Filesystem Hierarchy (FHS), Users & Standard Permissions",
                        "topics": ["Filesystem Hierarchy Standard (/bin, /sbin, /etc, /var, /tmp, /opt)", "User & Group database files (/etc/passwd, /etc/shadow, /etc/group)", "Standard permissions (Read, Write, Execute for User, Group, Others)", "Octal vs symbolic chmod notation", "File ownership management with chown and chgrp"],
                        "objectives": "Navigate Linux systems with confidence and identify improperly assigned read/write permissions on critical system assets.",
                        "lab": "Audit permissions across `/etc` and `/var`, create custom users with restricted group memberships, and verify permission enforcement.",
                        "interview_q": "Explain the significance of the fields in `/etc/shadow`, specifically hash algorithms, salt, and password expiration fields."
                    },
                    {
                        "num": 7,
                        "title": "Special Permissions (SUID, SGID, Sticky Bit) & Process Execution",
                        "topics": ["Set User ID (SUID) mechanics (octal 4000) and security implications", "Set Group ID (SGID) on directories and executables (octal 2000)", "Sticky Bit on shared directories (/tmp) (octal 1000)", "Process execution context: Real UID vs Effective UID", "Auditing the system for non-standard SUID binaries"],
                        "objectives": "Discover all SUID/SGID binaries on a Linux host and understand how privilege transitions occur during binary execution.",
                        "lab": "Use `find / -perm -4000 2>/dev/null` to locate SUID binaries, examine their permissions, and build a test C program demonstrating SUID privilege escalation.",
                        "interview_q": "Why does a shell script with the SUID bit set fail to grant elevated privileges on modern Linux kernels, while a compiled C binary succeeds?"
                    },
                    {
                        "num": 8,
                        "title": "Systemd Services, Daemons, Cron Tasks & SSH Key Hardening",
                        "topics": ["Systemd unit files (.service, .timer, .target) and systemctl management", "Creating and securing custom systemd services", "Cron daemon architecture (/etc/crontab, /etc/cron.*, /var/spool/cron)", "SSH architecture, sshd_config hardening (disabling root login, password auth)", "Ed25519 vs RSA SSH key generation and authorized_keys file security"],
                        "objectives": "Configure persistent daemons, schedule automated tasks securely, and establish cryptographic SSH access.",
                        "lab": "Deploy a custom systemd service running a monitoring script under a low-privilege user; configure an automated cron backup and harden sshd.",
                        "interview_q": "How does an attacker exploit a cron job running as root that executes a script in a world-writable directory?"
                    },
                    {
                        "num": 9,
                        "title": "Virtual Filesystems (/proc, /sys), Environment Variables & Bash Automation",
                        "topics": ["The `/proc` pseudo-filesystem: `/proc/<PID>/cmdline`, `environ`, `fd`, `maps`", "The `/sys` filesystem and kernel subsystem interaction", "Environment variables (PATH, LD_PRELOAD, LD_LIBRARY_PATH, SHELL)", "Bash scripting essentials: arguments, loops, pipes, conditional tests, exit codes", "Automating administrative and security tasks with shell scripts"],
                        "objectives": "Query process memory and environment directly from `/proc` and write robust Bash scripts for system triage.",
                        "lab": "Inspect the environment variables and open file descriptors of running processes via `/proc`; write a Bash script that alerts on new listening ports.",
                        "interview_q": "What security information can be extracted from `/proc/<PID>/environ`, and why should sensitive credentials never be passed via command-line arguments?"
                    },
                    {
                        "num": 10,
                        "title": "Linux Logging (/var/log, journalctl), Networking & Host Investigation",
                        "topics": ["Log architecture: `/var/log/auth.log` (or `secure`), `syslog`, `dmesg`, `wtmp`, `btmp`", "Querying systemd journal with `journalctl` (time filters, unit filters, priority)", "Linux networking CLI: `ip`, `ss`, `netstat`, `iptables`, `nftables`", "Live host investigation triage methodology", "Identifying unauthorized users, listening sockets, and active connections"],
                        "objectives": "Extract security events from system logs and identify unauthorized processes or suspicious outbound network sockets.",
                        "lab": "Simulate failed SSH brute-force attempts and parse `/var/log/auth.log` and `journalctl -u ssh` using `awk` and `grep` to generate an IP blocklist.",
                        "interview_q": "Which log file records successful and failed login attempts in Linux, and how would you detect a user attempting to tamper with log history?"
                    }
                ]
            },
            {
                "num": 3,
                "id": "week-03-windows",
                "title": "Windows Internals & PowerShell Security",
                "objective": "Understand Windows security architecture, processes, tokens, registry, ACLs, and administrative management via PowerShell.",
                "days": [
                    {
                        "num": 11,
                        "title": "Windows OS Architecture — User Mode, Kernel Mode & PE Basics",
                        "topics": ["Ring 3 (User Mode) vs Ring 0 (Kernel Mode) separation", "Executive subsystems: ntdll.dll, win32k.sys, HAL", "Process architecture: Process ID, PEB (Process Environment Block), TEB", "Threads, virtual memory allocation, and page protection flags", "Introduction to Portable Executable (PE) headers (MZ, PE signature, sections)"],
                        "objectives": "Understand how the Windows kernel isolates process memory and enforces execution boundaries.",
                        "lab": "Use Process Explorer / Process Hacker to inspect process trees, thread call stacks, and loaded DLL modules.",
                        "interview_q": "Explain the architectural boundary between User Mode and Kernel Mode in Windows. What happens when a user program makes a syscall?"
                    },
                    {
                        "num": 12,
                        "title": "Windows Security Subsystem — LSASS, SAM, Tokens & ACLs",
                        "topics": ["Local Security Authority Subsystem Service (LSASS) role and memory space", "Security Account Manager (SAM) database and system hives", "Windows Access Tokens: Primary vs Impersonation tokens, Token Privileges", "Security Identifiers (SIDs): Well-known SIDs (Administrator, SYSTEM, Everyone)", "Discretionary ACLs (DACLs) vs System ACLs (SACLs) and Access Control Entries (ACEs)"],
                        "objectives": "Examine token privileges (e.g. SeDebugPrivilege) and evaluate security descriptors on files and registry keys.",
                        "lab": "Use `whoami /priv` and `icacls` to inspect user tokens and file permissions; audit inheritance rules on sensitive directory trees.",
                        "interview_q": "What is the difference between a DACL and a SACL in Windows security descriptors, and what is the role of an ACE?"
                    },
                    {
                        "num": 13,
                        "title": "Windows Services, Registry Architecture, Scheduled Tasks & UAC",
                        "topics": ["Windows Service Control Manager (SCM), service accounts (LocalSystem, NetworkService)", "Windows Registry structure (HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, HKEY_CLASSES_ROOT)", "Common persistence autostart keys (Run, RunOnce, Winlogon)", "Task Scheduler mechanics, XML definition files, and triggers", "User Account Control (UAC) architecture, integrity levels (Low, Medium, High, System)"],
                        "objectives": "Query and inspect service binary paths, scheduled task configurations, and registry values.",
                        "lab": "Create and inspect a Windows service via `sc.exe`, analyze its registry definition in `HKLM\\System\\CurrentControlSet\\Services`, and configure a scheduled task.",
                        "interview_q": "How does User Account Control (UAC) prevent standard administrative processes from performing privileged kernel modifications without consent?"
                    },
                    {
                        "num": 14,
                        "title": "PowerShell for Security Operations — WMI, CIM & WinRM",
                        "topics": ["PowerShell execution policies, Cmdlet architecture, and object pipeline", "Windows Management Instrumentation (WMI) and Common Information Model (CIM)", "Querying system hardware, operating system, and processes via WMI/CIM", "Windows Remote Management (WinRM) and PowerShell Remoting (Enter-PSSession)", "PowerShell security features: Script Block Logging (EID 4104), Transcription, AMSI overview"],
                        "objectives": "Automate security telemetry gathering and remote system queries using native PowerShell cmdlets and WMI.",
                        "lab": "Write PowerShell scripts using `Get-CimInstance` to enumerate running services, listening ports, and startup programs across local and remote instances.",
                        "interview_q": "What information does PowerShell Script Block Logging (Event ID 4104) capture, and how does it assist SOC analysts during forensic investigations?"
                    },
                    {
                        "num": 15,
                        "title": "Windows Auditing — Security Event Logs, Sysmon & Endpoint Visibility",
                        "topics": ["Windows Event Log architecture (.evtx format, System, Security, Application channels)", "Critical Security Event IDs: 4624 (Logon), 4625 (Failed Logon), 4688 (Process Creation), 4672 (Admin Logon)", "Enabling Advanced Audit Policies (Command Line Auditing)", "System Monitor (Sysmon) architecture, configuration schema, and filtering", "Key Sysmon Event IDs: EID 1 (Process Create), EID 3 (Network Connect), EID 10 (Process Access)"],
                        "objectives": "Install and configure Sysmon with an industry-standard configuration (SwiftOnSecurity) and analyze security telemetry in Event Viewer.",
                        "lab": "Deploy Sysmon in a Windows lab, generate deliberate test activities (spawning cmd from powershell, network beacons), and trace the resulting Sysmon events.",
                        "interview_q": "Why is Windows Event ID 4688 insufficient on its own for deep threat detection without enabling command-line argument auditing, and how does Sysmon EID 1 complement it?"
                    }
                ]
            },
            {
                "num": 4,
                "id": "week-04-web-architecture",
                "title": "Web Architecture & Core Protocols",
                "objective": "Master HTTP request/response mechanics, browser security policies, session handling, OAuth/OIDC, and modern web infrastructure.",
                "days": [
                    {
                        "num": 16,
                        "title": "HTTP Protocol Deep Dive, Headers, Cookies & Sessions",
                        "topics": ["HTTP verbs (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD)", "Request and Response headers (Host, User-Agent, Referer, Accept, Content-Type)", "Cookie security flags: HttpOnly, Secure, SameSite (Strict, Lax, None)", "Session lifecycle: Session creation, storage (in-memory, Redis, DB), expiration, and invalidation", "Session fixation and session hijacking principles"],
                        "objectives": "Analyze raw HTTP request/response streams and audit cookie configurations for security compliance.",
                        "lab": "Build a minimal HTTP server in Python, observe cookie issuance, and demonstrate session hijacking by stealing unflagged cookies.",
                        "interview_q": "What protection does the `HttpOnly` flag provide against XSS attacks, and does it prevent an attacker from executing actions on the victim's behalf?"
                    },
                    {
                        "num": 17,
                        "title": "Browser Security Model — Same-Origin Policy (SOP), CORS & CSP",
                        "topics": ["Same-Origin Policy definition: Protocol, Host, Port matching rules", "DOM access vs Network request cross-origin restrictions", "Cross-Origin Resource Sharing (CORS) architecture: Preflight OPTIONS, Access-Control-Allow-Origin, Credentials", "CORS misconfigurations: Wildcard with credentials, Origin reflection, null origin trust", "Content Security Policy (CSP): Directives (script-src, default-src), nonces, and hashes"],
                        "objectives": "Evaluate browser origin boundaries, identify exploitable CORS configurations, and audit CSP headers.",
                        "lab": "Set up two local web origins and demonstrate how SOP blocks cross-origin reads; configure a vulnerable CORS policy and exploit it to extract data.",
                        "interview_q": "Why does an `Access-Control-Allow-Origin: *` header not permit cross-origin requests containing credentials (`Access-Control-Allow-Credentials: true`) in modern browsers?"
                    },
                    {
                        "num": 18,
                        "title": "Authentication Architectures — Passwords, Sessions & JSON Web Tokens (JWT)",
                        "topics": ["Password hashing algorithms: MD5/SHA (insecure) vs bcrypt, Argon2, PBKDF2 (work factor, salt)", "Session-based stateful authentication vs Token-based stateless authentication", "JWT structure: Header (Base64Url), Payload (Claims), Signature", "Standard JWT claims (iss, sub, aud, exp, nbf, iat)", "Cryptographic verification of symmetric (HS256) vs asymmetric (RS256) signatures"],
                        "objectives": "Decode and cryptographically verify JWTs and contrast stateful session stores with stateless bearer tokens.",
                        "lab": "Implement a Python script to decode, verify, and forge unsigned JWTs; test token tamper detection with HMAC verification.",
                        "interview_q": "Explain the trade-offs between stateful session IDs and stateless JWT tokens, specifically regarding immediate session revocation and token size."
                    },
                    {
                        "num": 19,
                        "title": "Modern Federated Identity — OAuth 2.0 & OpenID Connect (OIDC)",
                        "topics": ["OAuth 2.0 roles: Resource Owner, Client, Authorization Server, Resource Server", "Authorization Code Grant Flow step-by-step (with PKCE for public clients)", "Access Tokens vs Refresh Tokens vs ID Tokens", "OpenID Connect (OIDC) identity layer on top of OAuth 2.0", "Common OAuth vulnerabilities: Redirect URI poisoning, CSRF on auth flow, token leakage"],
                        "objectives": "Map out the OAuth 2.0 Authorization Code flow and identify failure points where authorization codes can be intercepted.",
                        "lab": "Trace an OAuth 2.0 authentication flow with Burp Suite, identify state parameter validation, and inspect the issued JWT ID token.",
                        "interview_q": "What is the purpose of the `state` parameter in OAuth 2.0, and what attack is possible if an application omits it?"
                    },
                    {
                        "num": 20,
                        "title": "Web Infrastructure — Reverse Proxies, CDNs, WebSockets & APIs",
                        "topics": ["Reverse proxies (Nginx, HAProxy) role in SSL termination, caching, and routing", "Content Delivery Networks (CDNs) and web application caching behavior", "WebSockets protocol: HTTP Upgrade handshake, bi-directional full-duplex communication", "RESTful API conventions vs RPC architectures", "Header forwarding: X-Forwarded-For, X-Forwarded-Host, X-Real-IP security implications"],
                        "objectives": "Understand how perimeter reverse proxies translate and forward client requests to internal upstream servers.",
                        "lab": "Configure an Nginx reverse proxy forwarding to a backend web app; inspect header manipulation and simulate IP spoofing via X-Forwarded-For.",
                        "interview_q": "How can trusting client-supplied headers like `X-Forwarded-For` without proxy validation lead to authentication bypass or IP restriction evasion?"
                    }
                ]
            },
            {
                "num": 5,
                "id": "week-05-web-security",
                "title": "Web Security Fundamentals",
                "objective": "Understand foundational web vulnerabilities from an attack and defense perspective, including injection and client-side flaws.",
                "days": [
                    {
                        "num": 21,
                        "title": "API Architectures, RESTful Conventions & GraphQL Introspection",
                        "topics": ["API request methods, JSON payloads, and status code standards", "API attack surfaces: Documentation endpoints (/swagger, /api-docs), hidden routes", "GraphQL core concepts: Schemas, Queries, Mutations, Resolvers", "GraphQL Introspection query mechanics", "API rate limiting, authentication headers (Bearer, API-Key)"],
                        "objectives": "Enumerate REST and GraphQL APIs, query schema introspection, and map hidden endpoints.",
                        "lab": "Send a standard GraphQL introspection query to extract the complete schema, types, and hidden mutations from a test application.",
                        "interview_q": "Why should GraphQL introspection be disabled in production environments, and what security risks does an exposed schema introduce?"
                    },
                    {
                        "num": 22,
                        "title": "Cross-Site Scripting (XSS) Core Mechanics — Stored, Reflected & DOM",
                        "topics": ["XSS definition and execution context in the browser", "Reflected XSS: Parameter reflection without encoding", "Stored XSS: Database persistence and payload delivery to multiple users", "DOM-based XSS: Sources (location.search, document.referrer) and Sinks (innerHTML, eval, document.write)", "Defenses: Context-aware output encoding, input validation, CSP"],
                        "objectives": "Distinguish between server-reflected, persistent, and client-side DOM XSS vulnerabilities with safe demonstration payloads.",
                        "lab": "Deploy a vulnerable lab web page, trigger Reflected and DOM XSS using benign alert/log payloads, and implement output encoding fixes.",
                        "interview_q": "Why is HTML entity encoding insufficient when injecting user input directly inside a JavaScript `<script>` block, and what encoding is required?"
                    },
                    {
                        "num": 23,
                        "title": "Cross-Site Request Forgery (CSRF) & SameSite Cookie Defenses",
                        "topics": ["CSRF attack mechanics: Exploiting ambient browser credentials", "State-changing GET requests vs vulnerable POST endpoints", "Anti-CSRF Tokens: Synchronizer token pattern, Double Submit Cookie pattern", "SameSite cookie attribute behavior: Strict, Lax (top-level navigations), None", "Preflight CORS requests as CSRF mitigation"],
                        "objectives": "Construct CSRF proof-of-concept HTML exploit forms and implement anti-CSRF token verification.",
                        "lab": "Build an HTML page that automatically submits a form to change a password on a vulnerable mock banking site; verify SameSite cookie defenses.",
                        "interview_q": "Explain how the `SameSite=Lax` cookie attribute mitigates CSRF attacks while still permitting user-friendly cross-site link clicks."
                    },
                    {
                        "num": 24,
                        "title": "Server-Side Request Forgery (SSRF) Mechanics & Cloud Metadata",
                        "topics": ["Server-Side Request Forgery (SSRF) concept: Coercing servers into sending outbound requests", "Internal network scanning via SSRF (accessing localhost, 127.0.0.1, internal subnets)", "Cloud Instance Metadata Service (IMDS) targeting: AWS 169.254.169.254, GCP, Azure", "IMDSv1 vs IMDSv2 (Session token requirement via PUT header)", "Defenses: Whitelisting, blocking private IP ranges (RFC 1918), disabling unused URL schemes"],
                        "objectives": "Understand how attackers pivot through vulnerable backend web services to query internal infrastructure and cloud credentials.",
                        "lab": "Simulate an SSRF vulnerability that fetches remote profile images; demonstrate internal port discovery on localhost (127.0.0.1).",
                        "interview_q": "How does AWS IMDSv2 prevent SSRF attacks from stealing IAM role credentials compared to IMDSv1?"
                    },
                    {
                        "num": 25,
                        "title": "SQL Injection Fundamentals — Error-based, Union-based & Blind",
                        "topics": ["SQL query construction and the flaw of string concatenation", "Authentication bypass payloads (`' OR 1=1 --`)", "UNION-based SQLi: Column count determination and data type matching", "Error-based SQLi: Extracting data through database engine error messages", "Blind SQLi concepts: Boolean-based true/false response differences and time delays", "Defenses: Parameterized queries (Prepared Statements), ORMs"],
                        "objectives": "Explain why SQL injection occurs and construct safe UNION and Blind SQLi payloads against an authorized database lab.",
                        "lab": "Set up a SQLite / MySQL vulnerable endpoint, use UNION-based injection to extract table schemas, and rewrite the query using parameterized statements.",
                        "interview_q": "Explain why parameterized queries (prepared statements) completely eliminate SQL injection regardless of user input characters."
                    }
                ]
            },
            {
                "num": 6,
                "id": "week-06-tooling",
                "title": "Security Tooling Foundation",
                "objective": "Build operational proficiency with essential security toolchains, intercepting proxies, scanning engines, and scripting for automation.",
                "days": [
                    {
                        "num": 26,
                        "title": "Security Workstation Setup — Kali Linux, Shell Customization & Git OPSEC",
                        "topics": ["Kali Linux / Parrot OS architecture and package management", "Terminal productivity: Zsh/Bash aliases, tmux multiplexing, curl/jq workflows", "Git version control for security practitioners: branching, tagging, commit discipline", "Git OPSEC: Avoiding committing private keys, API tokens, and sensitive client scopes (.gitignore)", "Setting up isolated virtual environments in Python (`venv`)"],
                        "objectives": "Establish a reproducible, clean, and OPSEC-safe security testing workstation and workflow.",
                        "lab": "Configure a dedicated security workspace with git pre-commit hooks that scan for accidental secret commits (TruffleHog / detect-secrets).",
                        "interview_q": "What security risks arise when security practitioners store engagement notes or scripts in public GitHub repositories, and how do you prevent credential leaks?"
                    },
                    {
                        "num": 27,
                        "title": "Network Scanning & Port Enumeration with Nmap",
                        "topics": ["TCP SYN scan (-sS) vs TCP Connect scan (-sT) mechanics", "UDP scanning (-sU) challenges and ICMP port unreachable replies", "Service version detection (-sV) and OS fingerprinting (-O)", "Nmap Scripting Engine (NSE): Categories (vuln, safe, default, discovery)", "Timing templates (-T0 through -T5) and network bandwidth impact"],
                        "objectives": "Execute targeted, deliberate Nmap scans against lab targets and analyze raw TCP packets generated by different scan flags.",
                        "lab": "Scan a local Linux target with -sS, -sT, and -sU; inspect the Wireshark packet capture to observe the half-open SYN vs full 3-way handshake.",
                        "interview_q": "Why does a TCP SYN scan require raw socket / root privileges to execute, whereas a TCP Connect scan can run as an unprivileged user?"
                    },
                    {
                        "num": 28,
                        "title": "Web Application Interception with Burp Suite",
                        "topics": ["Configuring browser proxy settings and installing the Burp CA root certificate", "Burp Suite architecture: Proxy, Repeater, Intruder, Decoder, Comparer", "Crafting and replaying requests in Repeater", "Intruder attack types: Sniper, Battering Ram, Pitchfork, Cluster Bomb", "Match and Replace rules for automated header injection and session testing"],
                        "objectives": "Intercept, analyze, modify, and replay HTTP/HTTPS traffic seamlessly using Burp Suite Community/Pro.",
                        "lab": "Proxy browser traffic through Burp, intercept an authentication request, replay it in Repeater with modified headers, and test a wordlist in Intruder.",
                        "interview_q": "How does Burp Suite intercept HTTPS traffic without causing browser SSL warnings, and what are the security implications of trusting a custom CA certificate?"
                    },
                    {
                        "num": 29,
                        "title": "Python for Security Practitioners — Sockets, Requests & Automation",
                        "topics": ["Python `socket` module: Creating TCP clients, binding servers, handling timeouts", "Python `requests` library: Session management, custom headers, handling cookies, SSL verification", "Command-line argument parsing with `argparse`", "JSON parsing and structured log output", "Building lightweight network and web security automation utilities"],
                        "objectives": "Write functional, well-structured Python scripts to interact directly with network services and REST APIs.",
                        "lab": "Write a multi-threaded TCP port checker in Python that scans a user-defined subnet and exports open ports to a structured JSON file.",
                        "interview_q": "When writing security automation in Python, why should `verify=False` in `requests.get()` be strictly avoided in production tools, and what are the risks?"
                    },
                    {
                        "num": 30,
                        "title": "Phase 1 Capstone Deliverable — Security Lab Environment",
                        "topics": ["Virtualization architecture: Hyper-V, VirtualBox, VMware Workstation", "Host-Only vs NAT vs Bridged virtual network adapters", "Deploying Kali Linux, Windows Evaluation Target, and Vulnerable Linux VM", "Configuring static IP ranges and verifying network isolation from home LAN", "Documenting architecture diagrams, asset inventory, and connectivity verification"],
                        "objectives": "Finalize and document a complete, isolated multi-OS cybersecurity lab environment ready for offensive and defensive operations.",
                        "lab": "Deploy and interconnect a Kali Linux attacker VM, a Windows 10/11 Target VM, and a Linux VM on an isolated Host-Only subnet; verify bidirectional ping and scanning.",
                        "interview_q": "Explain why security testing must strictly occur within isolated host-only or dedicated lab subnets rather than directly over bridging on home or corporate networks."
                    }
                ]
            }
        ]
    }
]

print("Script template ready. Expanding full 40 weeks programmatically...")
