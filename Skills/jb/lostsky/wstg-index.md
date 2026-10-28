# CyberStrike — OWASP WSTG 4.2 Skill Index

Source: `./references/upstream/WEB\OWASP_WSTG_4.2\`  
Skill dirs: **125** (each = one `SKILL.md`). Total source bytes: **1,541,411**.

Each entry: `owasp_id` — test name | what it tests | key technique/command.

## Categories

- **WSTG-INFO** (Information Gathering) — 10 tests
- **WSTG-CONF** (Configuration & Deployment Management) — 13 tests
- **WSTG-IDNT** (Identity Management) — 5 tests
- **WSTG-ATHN** (Authentication) — 11 tests
- **WSTG-AUTHZ** (Authorization) — 7 tests
- **WSTG-SESS** (Session Management) — 11 tests
- **WSTG-INPV** (Input Validation) — 29 tests
- **WSTG-ERRH** (Error Handling) — 2 tests
- **WSTG-CRYP** (Cryptography) — 4 tests
- **WSTG-BUSL** (Business Logic) — 10 tests
- **WSTG-CLNT** (Client-side) — 15 tests
- **WSTG-APIT** (API) — 4 tests
- **Rollup / multi-domain dirs** — 4

---

## WSTG-INFO — Information Gathering (10)

### WSTG-INFO-01 — Conduct Search Engine Discovery Reconnaissance for Information Leakage
- **Dir:** `wstg-info-01`
- **Tests:** This test aims to identify sensitive information about the target organization that has been unintentionally exposed on the internet through search engines and cache services. When search engines index web pages, they may also index sensitive configuration files, internal documentation, user informa
- **Checks:** Network diagrams and configuration information; Archived posts by administrators/personnel; Login procedure information; Username formats and email addresses; Error message content (stack traces, debug info); Development, test, or staging environment URLs
- **Key cmd:** `site:target.com                    # Results only from target domain`
- **CWE:** [CWE-200]

### WSTG-INFO-02 — Fingerprint Web Server
- **Dir:** `wstg-info-02`
- **Tests:** Web server fingerprinting is the process of identifying the type, version, and configuration of a web server. This information is critical for penetration testers as it helps identify known vulnerabilities associated with specific server versions. Attackers use this information to find and exploit u
- **Checks:** Web server software (Apache, nginx, IIS, LiteSpeed, etc.); Web server version number; Operating system information; Installed modules and extensions; Server configuration details; Backend technologies (PHP, ASP.NET, Java, etc.)
- **Key cmd:** `curl -I https://target.com`
- **CWE:** [CWE-200]

### WSTG-INFO-03 — Review Webserver Metafiles for Information Leakage
- **Dir:** `wstg-info-03`
- **Tests:** Web servers contain various metafiles that can inadvertently expose sensitive information about the application structure, hidden directories, restricted areas, and internal configurations. Files such as `robots.txt`, `sitemap.xml`, `security.txt`, and META tags are often overlooked but can provide 
- **Checks:** `robots.txt` - Spider/crawler directives; `sitemap.xml` - Site structure mapping; `sitemap_index.xml` - Sitemap index files; `security.txt` - Security policy disclosure; `humans.txt` - Team/contributor information; `crossdomain.xml` - Flash cross-domain policy
- **Key cmd:** `curl -s https://target.com/robots.txt`
- **CWE:** [CWE-200]

### WSTG-INFO-04 — Enumerate Applications on Webserver
- **Dir:** `wstg-info-04`
- **Tests:** A single web server can host multiple web applications accessible through different URLs, ports, or virtual hosts. This test aims to comprehensively discover all web applications running on the target infrastructure. Missing applications during enumeration can result in overlooking critical vulnerab
- **Checks:** Non-standard URL paths (/app1, /app2, /admin, /api); Non-standard ports (8080, 8443, 3000, 4443, etc.); Virtual hosts (different hostnames on same IP); Subdomains (app.target.com, admin.target.com); Load balancer backends; Hidden administrative interfaces
- **Key cmd:** `nmap -Pn -sT -sV -p0-65535 target.com`
- **CWE:** [CWE-200]

### WSTG-INFO-05 — Review Web Page Content for Information Leakage
- **Dir:** `wstg-info-05`
- **Tests:** Web pages often contain more information than what is visually displayed to users. HTML comments, JavaScript files, metadata, and debug artifacts can inadvertently expose sensitive information such as credentials, internal paths, infrastructure details, and business logic. This test involves systema
- **Checks:** HTML comments (`<!-- -->`); META tags; JavaScript files (external and inline); Source maps (`.map` files); CSS files and comments; Hidden form fields
- **Key cmd:** `curl -s https://target.com | grep -o '<!--.*-->'`
- **CWE:** [CWE-200]

### WSTG-INFO-06 — Identify Application Entry Points
- **Dir:** `wstg-info-06`
- **Tests:** Entry points are the interfaces through which user-supplied data enters the application. Identifying all entry points is critical for mapping the application's attack surface before conducting targeted security tests. Entry points include URL parameters, POST body data, HTTP headers, cookies, file u
- **Checks:** URL query string parameters (GET); POST body parameters; HTTP headers (custom and standard); Cookies and session tokens; Hidden form fields; File upload fields
- **Key cmd:** `| Location     | Parameter        | Value          |`
- **CWE:** [CWE-200]

### WSTG-INFO-07 — Map Execution Paths Through Application
- **Dir:** `wstg-info-07`
- **Tests:** Mapping execution paths involves understanding how users navigate through an application and identifying all possible workflows, decision points, and code paths. This foundational step ensures testers comprehend the application's structure before conducting comprehensive security testing. Understand
- **Checks:** User workflows and navigation patterns; Decision points and branching logic; Multi-step processes (checkout, registration, etc.); State-dependent functionality; Role-based access paths; Error handling flows
- **Key cmd:** `zap-cli spider https://target.com`
- **CWE:** [CWE-200]

### WSTG-INFO-08 — Fingerprint Web Application Framework
- **Dir:** `wstg-info-08`
- **Tests:** Web application framework fingerprinting identifies the underlying technologies, libraries, and frameworks used to build a web application. This information helps penetration testers understand the testing landscape, identify known vulnerabilities specific to detected frameworks, and tailor their te
- **Checks:** HTTP response headers (X-Powered-By, Server); Cookies (framework-specific names); HTML source code patterns; META tags (generator); File extensions (.php, .asp, .jsp); Directory structure
- **Key cmd:** `curl -sI https://target.com | grep -iE 'server|x-powered-by|x-aspnet|x-drupal|x-generator'`
- **CWE:** [CWE-200]

### WSTG-INFO-09 — Fingerprint Web Application
- **Dir:** `wstg-info-09`
- **Key cmd:** `curl -s https://target.com/version`
- **CWE:** [CWE-200]

### WSTG-INFO-10 — Map Application Architecture
- **Dir:** `wstg-info-10`
- **Tests:** Mapping application architecture involves identifying all components that make up the application infrastructure, including web servers, application servers, databases, load balancers, CDNs, firewalls, and security devices. Understanding the architecture helps penetration testers identify scope boun
- **Checks:** Web server (Apache, nginx, IIS); Application server (Tomcat, JBoss, .NET); Database server (MySQL, PostgreSQL, MSSQL, Oracle); Caching layer (Redis, Memcached, Varnish); Message queue (RabbitMQ, Kafka); Search engine (Elasticsearch, Solr)
- **Key cmd:** `curl -sI https://target.com | grep -i server`
- **CWE:** [CWE-200]

---

## WSTG-CONF — Configuration & Deployment Management (13)

### WSTG-CONF-01 — Test Network Infrastructure Configuration
- **Dir:** `wstg-conf-01`
- **Tests:** This test evaluates the security configuration of network infrastructure components that support the web application. It includes assessing web servers, application servers, database servers, load balancers, and administrative interfaces for misconfigurations, default credentials, and known vulnerab
- **Checks:** Web server configuration; Application server settings; Database server exposure; Load balancer configuration; Firewall rules; Network segmentation
- **Key cmd:** `nmap -sV -sC -p- target.com`
- **CWE:** [CWE-16]

### WSTG-CONF-02 — Test Application Platform Configuration
- **Dir:** `wstg-conf-02`
- **Tests:** This test examines the configuration of the application platform including web servers, application servers, and their components. Misconfigurations can expose sensitive information, enable attacks, or provide unauthorized access. Key areas include default files, sample applications, debug settings,
- **Checks:** Default/sample files and applications; Debug mode and settings; Error handling configuration; Logging configuration; Server modules and extensions; Directory listings
- **Key cmd:** `for file in \`
- **CWE:** [CWE-16]

### WSTG-CONF-03 — Test File Extensions Handling for Sensitive Information
- **Dir:** `wstg-conf-03`
- **Tests:** This test examines how the web server handles different file extensions. Misconfigured servers may expose source code, include files, backup files, or other sensitive content when requested with specific extensions. Attackers exploit these misconfigurations to access database credentials, API keys, 
- **Checks:** Source code disclosure via extensions; Include files (.inc, .config); Backup files (.bak, .old, .backup); Temporary files (.tmp, .swp, ~); Archive files (.zip, .tar, .gz); Configuration files
- **Key cmd:** `wget --spider -r -l 3 https://target.com 2>&1 | grep -oP 'https?://[^\s]+' > urls.txt`
- **CWE:** [CWE-200]

### WSTG-CONF-04 — Review Old Backup and Unreferenced Files for Sensitive Information
- **Dir:** `wstg-conf-04`
- **Tests:** Old backup files, unreferenced pages, and forgotten content can expose sensitive information including source code, credentials, and outdated vulnerable functionality. These files often contain debugging information, database credentials, or reveal application logic that aids attackers. This test fo
- **Checks:** Backup files (.bak, .old, .backup, ~); Temporary files (.tmp, .swp, .temp); Archive files (.zip, .tar, .gz, .rar); Editor files (.bak, ~, .orig); Unreferenced pages; Old versions of files
- **Key cmd:** `files=("edituser.asp" "adduser.asp" "deleteuser.asp"`
- **CWE:** [CWE-16]

### WSTG-CONF-05 — Enumerate Infrastructure and Application Admin Interfaces
- **Dir:** `wstg-conf-05`
- **Tests:** Administrative interfaces provide privileged access to application and infrastructure management functions. These interfaces are high-value targets for attackers as they often allow configuration changes, user management, and access to sensitive data. This test identifies hidden or poorly protected 
- **Checks:** Application admin panels; CMS admin interfaces; Database management tools; Server management consoles; Cloud management portals; API management interfaces
- **Key cmd:** `TARGET=$1`
- **CWE:** [CWE-548]

### WSTG-CONF-06 — Test HTTP Methods
- **Dir:** `wstg-conf-06`
- **Tests:** HTTP methods define the type of action to be performed on a resource. While GET and POST are commonly used, other methods like PUT, DELETE, TRACE, and OPTIONS may be enabled and exploitable. This test identifies which HTTP methods are supported by the web server and checks for potential security iss
- **Key cmd:** `curl -X OPTIONS -I https://target.com/`
- **CWE:** [CWE-200]

### WSTG-CONF-07 — Test HTTP Strict Transport Security
- **Dir:** `wstg-conf-07`
- **Tests:** HTTP Strict Transport Security (HSTS) is a security mechanism that forces browsers to communicate with websites only over HTTPS. When properly implemented, HSTS protects against protocol downgrade attacks, SSL stripping, and cookie hijacking. This test verifies that the HSTS header is present, prope
- **Key cmd:** `curl -sI https://target.com | grep -i strict-transport-security`
- **CWE:** [CWE-200]

### WSTG-CONF-08 — Test RIA Cross Domain Policy
- **Dir:** `wstg-conf-08`
- **Tests:** Rich Internet Application (RIA) cross-domain policy files control how Flash and Silverlight applications can access resources across different domains. Misconfigured policy files can allow unauthorized cross-domain access, leading to data theft and other security issues. While these technologies are
- **Checks:** `/crossdomain.xml` (Adobe Flash); `/clientaccesspolicy.xml` (Microsoft Silverlight); Wildcard permissions (`*`); Overly permissive configurations; Unnecessary cross-domain access
- **Key cmd:** `curl -s https://target.com/crossdomain.xml`
- **CWE:** [CWE-16]

### WSTG-CONF-09 — Test File Permission
- **Dir:** `wstg-conf-09`
- **Tests:** Incorrect file permissions can expose sensitive data, allow unauthorized modifications, or enable code execution. This test examines file and directory permissions to identify overly permissive settings that could be exploited by attackers. Proper file permissions are a critical component of defense
- **Checks:** Web application files; Configuration files; Sensitive data files (encrypted data, keys); Log files; Executable files (scripts, binaries); Database files
- **Key cmd:** `ls -la /var/www/html/`
- **CWE:** [CWE-434]

### WSTG-CONF-10 — Test for Subdomain Takeover
- **Dir:** `wstg-conf-10`
- **Tests:** Subdomain takeover occurs when a subdomain's DNS record points to an external service that is no longer in use or has been deleted. Attackers can claim the abandoned resource and host their own content on the victim's subdomain. This can lead to credential theft, phishing, cookie stealing, and reput
- **Checks:** A records pointing to decommissioned IPs; CNAME records pointing to unclaimed services; NS records pointing to expired domains; MX records pointing to abandoned mail services
- **Key cmd:** `amass enum -d target.com -o subdomains.txt`
- **CWE:** [CWE-16]

### WSTG-CONF-11 — Test Cloud Storage
- **Dir:** `wstg-conf-11`
- **Tests:** Cloud storage services (AWS S3, Azure Blob Storage, Google Cloud Storage) are commonly used to store application data, backups, and static assets. Misconfigured access controls can expose sensitive data to unauthorized users or allow arbitrary file uploads. This test identifies publicly accessible b
- **Checks:** Publicly readable buckets/containers; Publicly writable buckets/containers; Unauthenticated listing permissions; Overly permissive ACLs; Missing encryption; Exposed sensitive data
- **Key cmd:** `curl -s https://target.com | grep -oP 's3\.amazonaws\.com[^"'"'"' ]*'`
- **CWE:** [CWE-16]

### WSTG-CONF-12 — Test for Content Security Policy
- **Dir:** `wstg-conf-12`
- **Tests:** Content Security Policy (CSP) is a security mechanism that helps prevent cross-site scripting (XSS), clickjacking, and other code injection attacks. CSP defines which sources of content are allowed to be loaded and executed by the browser. This test evaluates whether CSP is implemented correctly and
- **Checks:** CSP header present; CSP meta tag usage; Report-Only mode vs enforcement; Policy completeness
- **Key cmd:** `curl -sI https://target.com | grep -i content-security-policy`
- **CWE:** []

### WSTG-CONF-13 — Test for Path Confusion
- **Dir:** `wstg-conf-13`
- **Tests:** Path confusion vulnerabilities arise when web servers, application frameworks, or caching systems interpret URL paths differently. Attackers can exploit these inconsistencies to bypass security controls, trigger web cache deception, or access restricted resources. This test identifies path handling 
- **Checks:** Path normalization differences; URL encoding handling; Trailing slash behavior; Path parameter handling; Extension handling; Cache key generation
- **Key cmd:** `curl -s https://target.com/user/dashboard`
- **CWE:** []

---

## WSTG-IDNT — Identity Management (5)

### WSTG-IDNT-01 — Test Role Definitions
- **Dir:** `wstg-idnt-01`
- **Tests:** Role definitions testing evaluates how well an application implements role-based access control (RBAC). This test identifies whether roles are properly defined, whether users can only access resources appropriate for their role, and whether role hierarchies are correctly enforced. Poorly defined rol
- **Checks:** Documented role definitions exist; Roles follow principle of least privilege; Role separation is properly implemented; Administrative roles are properly restricted; Role hierarchy is clearly defined
- **Key cmd:** `curl -s -H "Authorization: Bearer $TOKEN" \`
- **CWE:** []

### WSTG-IDNT-02 — Test User Registration Process
- **Dir:** `wstg-idnt-02`
- **Tests:** The user registration process is a critical security boundary where new identities are created in the system. Testing this process identifies vulnerabilities such as weak identity verification, insufficient validation, mass registration vulnerabilities, and privilege escalation during account creati
- **Checks:** Identity verification requirements; Email/phone verification; CAPTCHA implementation; Rate limiting on registration; Input validation; Duplicate account prevention
- **Key cmd:** `curl -s -X POST "https://target.com/api/register" \`
- **CWE:** []

### WSTG-IDNT-03 — Test Account Provisioning Process
- **Dir:** `wstg-idnt-03`
- **Tests:** Account provisioning is the process by which user accounts are created, modified, and managed by administrators or automated systems. This test evaluates the security of the provisioning workflow, including how accounts are created, what privileges are assigned, and whether proper authorization is r
- **Checks:** Authorization required for account creation; Approval workflows exist; Audit logging of provisioning actions; Principle of least privilege applied; Separation of duties enforced; Temporary/service account management
- **Key cmd:** `curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \`
- **CWE:** []

### WSTG-IDNT-04 — Test Account Enumeration
- **Dir:** `wstg-idnt-04`
- **Tests:** Account enumeration occurs when an application reveals whether a username or email exists in the system through different response messages, timing differences, or HTTP status codes. Attackers use this information to compile valid account lists for targeted attacks such as brute-force, credential st
- **Checks:** Login form responses; Registration form responses; Password reset functionality; Username recovery feature; API endpoints; Response timing differences
- **Key cmd:** `curl -s -X POST "https://target.com/login" \`
- **CWE:** []

### WSTG-IDNT-05 — Test Username Policy
- **Dir:** `wstg-idnt-05`
- **Tests:** Username policy testing evaluates the rules and restrictions applied to username creation and management. Weak username policies can lead to account enumeration, impersonation attacks, and user confusion. This test examines whether the application enforces appropriate restrictions on username format
- **Checks:** Minimum/maximum length requirements; Allowed character sets; Case sensitivity handling; Reserved username protection; Duplicate prevention; Username format validation
- **Key cmd:** `curl -s -X POST "https://target.com/api/register" \`
- **CWE:** []

---

## WSTG-ATHN — Authentication (11)

### WSTG-ATHN-01 — Testing for Credentials Transported over an Encrypted Channel
- **Dir:** `wstg-athn-01`
- **Tests:** This test verifies that user credentials (usernames, passwords, tokens) are transmitted over encrypted channels (HTTPS/TLS) to prevent interception by attackers. Transmitting credentials over unencrypted HTTP exposes them to man-in-the-middle attacks, network sniffing, and session hijacking. All aut
- **Checks:** Login pages served over HTTPS; Login form submits to HTTPS endpoint; Password reset over HTTPS; Registration over HTTPS; API authentication over HTTPS; Session tokens transmitted securely
- **Key cmd:** `curl -sI "http://target.com/login" | head -20`
- **CWE:** [CWE-522]

### WSTG-ATHN-02 — Testing for Default Credentials
- **Dir:** `wstg-athn-02`
- **Tests:** Many applications, devices, and services ship with default or well-known credentials that administrators often forget to change. Attackers can easily find these credentials through documentation, online databases, or simple guessing. This test identifies systems using default credentials that could 
- **Checks:** Application default accounts; Framework/CMS defaults; Database default credentials; Admin panel defaults; API default tokens; Third-party component defaults
- **Key cmd:** `curl -sI "https://target.com" | grep -i "server\|x-powered-by"`
- **CWE:** [CWE-640]

### WSTG-ATHN-03 — Testing for Weak Lock Out Mechanism
- **Dir:** `wstg-athn-03`
- **Tests:** Account lockout mechanisms are designed to protect against brute-force password attacks by temporarily or permanently locking accounts after a certain number of failed login attempts. This test evaluates whether the lockout mechanism is properly implemented and cannot be bypassed. Weak or missing lo
- **Checks:** Lockout threshold exists; Lockout duration appropriate; Lockout applies to all authentication methods; Lockout cannot be bypassed; Account enumeration via lockout; Denial of service via lockout
- **Key cmd:** `TARGET="https://target.com/api/login"`
- **CWE:** [CWE-304]

### WSTG-ATHN-04 — Testing for Bypassing Authentication Schema
- **Dir:** `wstg-athn-04`
- **Tests:** Authentication bypass testing examines whether an application's authentication controls can be circumvented. Attackers may exploit logic flaws, misconfigurations, or vulnerabilities to access protected resources without proper authentication. This test identifies weaknesses that allow unauthorized a
- **Checks:** Direct page access; Parameter manipulation; Session prediction; SQL injection in auth; Forced browsing; Authentication logic flaws
- **Key cmd:** `protected_pages=(`
- **CWE:** [CWE-307]

### WSTG-ATHN-05 — Testing for Vulnerable Remember Password
- **Dir:** `wstg-athn-05`
- **Tests:** "Remember me" or "remember password" functionality allows users to stay logged in across browser sessions. This test examines whether this functionality is implemented securely. Insecure implementations may store credentials in cleartext, use predictable tokens, or create persistent sessions that ar
- **Checks:** Token generation security; Token storage method; Token expiration; Token scope (device/browser specific); Credential storage; Token revocation capability
- **Key cmd:** `response=$(curl -s -X POST "https://target.com/login" \`
- **CWE:** [CWE-287]

### WSTG-ATHN-06 — Testing for Browser Cache Weaknesses
- **Dir:** `wstg-athn-06`
- **Tests:** Browser cache weakness testing examines whether sensitive authentication and user data can be retrieved from browser cache, history, or back button functionality. Improper cache control headers may allow sensitive pages to be cached, enabling attackers to access private information from shared or pu
- **Checks:** Sensitive pages cached; Missing cache-control headers; Back button exposes data; Browser history reveals sensitive URLs; Autocomplete on sensitive forms; Credential caching
- **Key cmd:** `pages=(`
- **CWE:** [CWE-613]

### WSTG-ATHN-07 — Testing for Weak Password Policy
- **Dir:** `wstg-athn-07`
- **Tests:** Password policy testing evaluates the strength requirements enforced by an application during password creation and change. Weak policies allow users to create easily guessable passwords, making accounts vulnerable to brute-force and dictionary attacks. This test examines minimum length, complexity 
- **Checks:** Minimum length requirement; Maximum length limit; Complexity requirements (uppercase, lowercase, numbers, symbols); Dictionary word prevention; Common password blocklist; Personal information restrictions
- **Key cmd:** `lengths=(1 2 3 4 5 6 7 8 10 12 16)`
- **CWE:** [CWE-287]

### WSTG-ATHN-08 — Testing for Weak Security Question Answer
- **Dir:** `wstg-athn-08`
- **Tests:** Security questions are often used as a secondary authentication mechanism for password recovery. This test evaluates whether security questions provide adequate protection or are vulnerable to guessing, research, or social engineering attacks. Weak security questions can allow attackers to bypass au
- **Checks:** Easily guessable questions; Publicly researchable answers; Limited question choices; No answer format requirements; No rate limiting on attempts; Case-sensitive matching issues
- **Key cmd:** `curl -s "https://target.com/api/security-questions" | jq '.'`
- **CWE:** [CWE-287]

### WSTG-ATHN-09 — Testing for Weak Password Change or Reset Functionalities
- **Dir:** `wstg-athn-09`
- **Tests:** Password change and reset functionalities are critical security controls that must be properly implemented. This test examines these mechanisms for vulnerabilities such as weak token generation, missing validation, token leakage, and account takeover possibilities. Weaknesses in these functions can 
- **Checks:** Token predictability; Token expiration; Token single-use enforcement; Email enumeration; Host header injection; Token leakage in URLs
- **Key cmd:** `tokens=()`
- **CWE:** [CWE-521]

### WSTG-ATHN-10 — Testing for Weaker Authentication in Alternative Channel
- **Dir:** `wstg-athn-10`
- **Tests:** Many applications provide multiple access channels (web, mobile, API, legacy interfaces) that may have inconsistent authentication controls. This test identifies scenarios where alternative channels have weaker security than the primary channel, potentially allowing attackers to bypass stronger cont
- **Checks:** Mobile application API; Legacy web interface; Admin/internal interfaces; Partner/B2B APIs; Command-line tools; WebSocket connections
- **Key cmd:** `curl -s "https://target.com" | grep -oP 'https?://[a-zA-Z0-9./-]+api[a-zA-Z0-9./-]*'`
- **CWE:** [CWE-287]

### WSTG-ATHN-11 — Testing Multi-Factor Authentication (MFA)
- **Dir:** `wstg-athn-11`
- **Tests:** Multi-Factor Authentication adds an additional layer of security beyond passwords. This test examines the implementation of MFA for weaknesses such as bypass vulnerabilities, weak OTP generation, lack of rate limiting, and improper enrollment procedures. A flawed MFA implementation can give users fa
- **Checks:** MFA bypass possibilities; OTP strength and predictability; Rate limiting on OTP attempts; Backup code security; MFA enrollment process; Recovery mechanism security
- **Key cmd:** `session=$(curl -s -X POST "https://target.com/api/login" \`
- **CWE:** []

---

## WSTG-AUTHZ — Authorization (7)

### WSTG-AUTHZ-01 — Testing Directory Traversal File Include
- **Dir:** `wstg-authz-01`
- **Tests:** Directory traversal (also known as path traversal) is a vulnerability that allows attackers to access files and directories outside the intended directory by manipulating file path parameters. Attackers use special characters like `../` to navigate the file system and access sensitive files such as 
- **Checks:** File download parameters; Image/document path parameters; Template file parameters; Language/locale file parameters; Log file viewers; Configuration file loaders
- **Key cmd:** `grep -rE "file=|path=|doc=|template=|page=|include=" burp_requests.txt`
- **CWE:** [CWE-639]

### WSTG-AUTHZ-02 — Testing for Bypassing Authorization Schema
- **Dir:** `wstg-authz-02`
- **Tests:** Authorization bypass occurs when an attacker gains access to resources or functions without proper permission. This happens when the application fails to enforce access controls consistently, allowing users to access other users' data, perform privileged actions, or access restricted functionality t
- **Checks:** Horizontal privilege escalation (accessing other users' data); Vertical privilege escalation (accessing admin functions); Missing authorization checks on endpoints; Client-side only authorization; Parameter manipulation bypasses; Forced browsing to restricted pages
- **CWE:** [CWE-639]

### WSTG-AUTHZ-03 — Testing for Privilege Escalation
- **Dir:** `wstg-authz-03`
- **Tests:** Privilege escalation occurs when a user gains access to resources or capabilities beyond their authorized level. There are two types: vertical escalation (gaining higher privileges like admin access) and horizontal escalation (accessing resources of other users at the same privilege level). This tes
- **Checks:** Role parameter manipulation; Admin function access; Hidden admin endpoints; JWT/token manipulation; Cookie value tampering; SQL injection for role bypass
- **Key cmd:** `curl -s "https://target.com/api/user/profile" \`
- **CWE:** [CWE-269]

### WSTG-AUTHZ-04 — Testing for Insecure Direct Object References (IDOR)
- **Dir:** `wstg-authz-04`
- **Tests:** Insecure Direct Object References (IDOR) occur when an application uses user-supplied input to access objects directly without proper authorization checks. Attackers can modify parameters like IDs, filenames, or keys to access unauthorized resources belonging to other users. IDOR is a form of broken
- **Checks:** User IDs (user_id, uid, userId); Document/File IDs (doc_id, file_id); Order IDs (order_id, orderId); Account numbers; Transaction IDs; Message/Email IDs
- **Key cmd:** `endpoints=(`
- **CWE:** [CWE-639]

### WSTG-AUTHZ-05 — Testing for OAuth Weaknesses
- **Dir:** `wstg-authz-05`
- **Tests:** OAuth 2.0 is an authorization framework that enables applications to obtain limited access to user accounts. Misconfigurations or implementation flaws in OAuth can lead to account takeover, token theft, unauthorized access, and data exposure. This test identifies vulnerabilities in OAuth implementat
- **Checks:** Authorization endpoint security; Token endpoint security; Redirect URI validation; State parameter implementation; PKCE implementation; Token storage and handling
- **Key cmd:** `curl -s "https://target.com/.well-known/oauth-authorization-server" | jq '.'`
- **CWE:** []

### WSTG-AUTHZ-05.1 — Testing OAuth Authorization Server Weaknesses
- **Dir:** `wstg-authz-05.1`
- **Tests:** The OAuth Authorization Server is responsible for authenticating users, obtaining consent, and issuing access tokens. Vulnerabilities in the authorization server can compromise the entire OAuth ecosystem, leading to unauthorized access to protected resources across all client applications. This test
- **Checks:** Authorization endpoint security; Token endpoint security; Token introspection endpoint; Token revocation endpoint; UserInfo endpoint; Discovery endpoints (.well-known)
- **Key cmd:** `curl -s "https://auth.target.com/.well-known/oauth-authorization-server" | jq '.'`
- **CWE:** []

### WSTG-AUTHZ-05.2 — Testing OAuth Client Weaknesses
- **Dir:** `wstg-authz-05.2`
- **Tests:** OAuth clients (also known as relying parties) are applications that use OAuth to access protected resources on behalf of users. Client-side vulnerabilities can lead to token theft, account takeover, and unauthorized access. This test focuses on identifying weaknesses in how the client application ha
- **Checks:** Token storage security; Redirect URI handling; State parameter validation; PKCE implementation; Token refresh handling; Logout/revocation handling
- **Key cmd:** `grep -iE "code=|token=|access_token=|state=" browser_history.txt`
- **CWE:** []

---

## WSTG-SESS — Session Management (11)

### WSTG-SESS-01 — Testing for Session Management Schema
- **Dir:** `wstg-sess-01`
- **Tests:** Session management is the mechanism by which a web application maintains state with users across multiple requests. Weaknesses in session management can lead to session hijacking, fixation, or prediction attacks. This test evaluates the overall session management implementation including token gener
- **Checks:** Token randomness/entropy; Token length (minimum 128 bits); Token predictability; Token format/structure; Token transmission security; Token storage location
- **Key cmd:** `curl -sI "https://target.com/login" | grep -iE "set-cookie|session|token"`
- **CWE:** [CWE-539]

### WSTG-SESS-02 — Testing for Cookies Attributes
- **Dir:** `wstg-sess-02`
- **Tests:** Cookie attributes control how browsers handle cookies, including security restrictions. Improperly configured cookie attributes can expose session tokens to theft via XSS attacks, man-in-the-middle attacks, or cross-site request forgery. This test examines whether cookies are configured with appropr
- **Checks:** Secure flag (HTTPS only); HttpOnly flag (no JavaScript access); SameSite attribute (CSRF protection); Domain scope; Path scope; Expires/Max-Age settings
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-384]

### WSTG-SESS-03 — Testing for Session Fixation
- **Dir:** `wstg-sess-03`
- **Tests:** Session fixation is an attack where the attacker sets a user's session ID to a known value. When the victim authenticates, the attacker can hijack their session using the pre-set session ID. This occurs when the application doesn't regenerate the session ID after authentication, allowing the attacke
- **Checks:** Session ID regeneration on login; Session ID regeneration on privilege change; Session ID acceptance from URL; Session ID acceptance from POST data; Cross-subdomain session fixation; Session adoption after authentication
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-613]

### WSTG-SESS-04 — Testing for Exposed Session Variables
- **Dir:** `wstg-sess-04`
- **Tests:** Session variables may be exposed through various channels including URLs, error messages, logs, HTTP headers, or client-side storage. Exposure of session tokens or sensitive session data can lead to session hijacking, information disclosure, or account takeover. This test identifies instances where 
- **Checks:** Session ID in URL parameters; Session data in error messages; Session tokens in HTTP Referer; Session data in browser storage; Session info in server logs; Session variables in hidden fields
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-614]

### WSTG-SESS-05 — Testing for Cross Site Request Forgery (CSRF)
- **Dir:** `wstg-sess-05`
- **Tests:** Cross-Site Request Forgery (CSRF) forces authenticated users to execute unwanted actions on a web application. Attackers craft malicious requests that are automatically sent by the victim's browser with their session credentials, allowing unauthorized actions like password changes, fund transfers, o
- **Checks:** CSRF token implementation; Token validation on server; SameSite cookie attribute; Origin/Referer validation; State-changing GET requests; Token uniqueness and randomness
- **CWE:** [CWE-352]

### WSTG-SESS-06 — Testing for Logout Functionality
- **Dir:** `wstg-sess-06`
- **Tests:** Logout functionality must properly terminate user sessions by invalidating session tokens on the server side. Improper logout implementation can allow continued access using old session tokens, session replay attacks, or leave users vulnerable if using shared computers.
- **Checks:** Server-side session invalidation; Client-side token clearing; "Remember me" token revocation; All sessions logout (multi-device); Browser cache clearing; Redirect after logout
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-613]

### WSTG-SESS-07 — Testing for Session Timeout
- **Dir:** `wstg-sess-07`
- **Tests:** Session timeout controls how long a session remains valid after periods of inactivity or absolute time limits. Improper timeout configuration can leave sessions vulnerable to hijacking if users don't explicitly logout, especially on shared computers or public networks.
- **Checks:** Idle timeout implementation; Absolute timeout (max session age); Timeout consistency across endpoints; Timeout bypass via activity; Warning before timeout; Timeout on sensitive actions
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-384]

### WSTG-SESS-08 — Testing for Session Puzzling
- **Dir:** `wstg-sess-08`
- **Tests:** Session puzzling occurs when session variables are used for multiple purposes across different application flows. Attackers can manipulate session state in one flow to affect behavior in another, potentially bypassing authentication or authorization controls.
- **Checks:** Session variable reuse across flows; Authentication bypass via flow manipulation; State confusion attacks; Password reset session abuse; Registration flow exploitation
- **CWE:** [CWE-200]

### WSTG-SESS-09 — Testing for Session Hijacking
- **Dir:** `wstg-sess-09`
- **Tests:** Session hijacking occurs when an attacker obtains a valid session token through various means (sniffing, XSS, prediction) and uses it to impersonate the legitimate user. This test evaluates the application's resilience against session hijacking attacks and the effectiveness of protective measures.
- **Checks:** Token transmission security (HTTPS); Token exposure vectors (XSS, logs); Session binding (IP, User-Agent); Concurrent session detection; Session token predictability; Re-authentication for sensitive operations
- **Key cmd:** `curl -sI "https://target.com" | grep -i "set-cookie" | grep -i "httponly"`
- **CWE:** [CWE-384]

### WSTG-SESS-10 — Testing JSON Web Tokens (JWT)
- **Dir:** `wstg-sess-10`
- **Tests:** JSON Web Tokens (JWT) are widely used for authentication and authorization. Misconfigurations in JWT implementation can lead to authentication bypass, privilege escalation, or information disclosure. This test evaluates the security of JWT generation, validation, and handling.
- **Checks:** Algorithm confusion (none, HS256/RS256); Weak signing secrets; Missing signature validation; Sensitive data in payload; Token expiration (exp claim); Token revocation mechanism
- **Key cmd:** `TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2Mj`
- **CWE:** []

### WSTG-SESS-11 — Testing for Concurrent Sessions
- **Dir:** `wstg-sess-11`
- **Tests:** Concurrent session handling determines how an application manages multiple simultaneous sessions for the same user account. Improper handling can allow attackers to maintain access even after legitimate users change passwords or attempt to terminate sessions, and may enable account sharing in violat
- **Checks:** Multiple simultaneous sessions allowed; Session invalidation on password change; Session termination capabilities; New login behavior (invalidate previous?); Device/session management features; Session limit enforcement
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

---

## WSTG-INPV — Input Validation (29)

### WSTG-INPV-01 — Testing for Reflected Cross-Site Scripting (XSS)
- **Dir:** `wstg-inpv-01`
- **Tests:** Reflected XSS occurs when user input is immediately returned by the application without proper sanitization. The malicious script is reflected off the web server in error messages, search results, or any response that includes user input. This allows attackers to execute scripts in victims' browsers
- **Checks:** URL parameters reflected in response; Form inputs reflected in response; HTTP headers reflected in response; Error messages containing user input; Search functionality; Redirect parameters
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-93]

### WSTG-INPV-02 — Testing for Stored Cross-Site Scripting (XSS)
- **Dir:** `wstg-inpv-02`
- **Tests:** Stored XSS (Persistent XSS) occurs when user input is permanently stored on the target server and later displayed to other users without proper sanitization. This is more dangerous than reflected XSS because it affects all users who view the infected page and doesn't require social engineering to tr
- **Checks:** User profile fields (name, bio, etc.); Comments and posts; Forum messages; File uploads (SVG, HTML); Email functionality; Log viewers
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-79]

### WSTG-INPV-03 — Testing for HTTP Verb Tampering
- **Dir:** `wstg-inpv-03`
- **Tests:** HTTP Verb Tampering exploits web servers or applications that respond differently to various HTTP methods (GET, POST, PUT, DELETE, etc.). Attackers may bypass security controls by using alternative HTTP methods that aren't properly restricted, potentially gaining unauthorized access to protected res
- **Checks:** Supported HTTP methods per endpoint; Authentication bypass via method change; Authorization bypass via method change; HEAD method information leakage; TRACE method enabled (XST); Arbitrary methods acceptance
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-89]

### WSTG-INPV-04 — Testing for HTTP Parameter Pollution (HPP)
- **Dir:** `wstg-inpv-04`
- **Tests:** HTTP Parameter Pollution (HPP) occurs when an application doesn't properly handle multiple parameters with the same name. Different web servers and frameworks handle duplicate parameters differently, which can lead to bypassing input validation, WAF evasion, or logic manipulation.
- **Checks:** Duplicate parameter handling; Server-side parameter pollution; Client-side parameter pollution; WAF bypass via parameter pollution; Business logic bypass; Parameter precedence
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-94]

### WSTG-INPV-05 — Testing for SQL Injection
- **Dir:** `wstg-inpv-05`
- **Tests:** SQL Injection occurs when untrusted data is sent to an interpreter as part of a command or query. The attacker's hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization. SQL injection can result in data theft, data loss, denial of serv
- **Checks:** User input in SQL queries; Error-based injection; Union-based injection; Blind injection (Boolean/Time); Second-order injection; Stored procedures
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-89, CWE-564]

### WSTG-INPV-05.1 — Testing for SQL Injection - Oracle
- **Dir:** `wstg-inpv-05.1`
- **Tests:** Oracle-specific SQL injection testing focuses on exploiting Oracle Database features, syntax, and built-in functions. Oracle's unique characteristics include PL/SQL, dual table, specific error messages, and distinct functions that can be leveraged for detection and exploitation.
- **Checks:** Oracle-specific error messages; Oracle system tables; PL/SQL injection; Oracle functions exploitation; UTL_HTTP for out-of-band; XML functions
- **Key cmd:** `TARGET="https://target.com/product?id="`
- **CWE:** []

### WSTG-INPV-05.2 — Testing for SQL Injection - MySQL
- **Dir:** `wstg-inpv-05.2`
- **Tests:** MySQL-specific SQL injection testing leverages MySQL's unique syntax, functions, and features. MySQL is widely used in web applications (LAMP stack), making it a common target. Key features include information_schema, comment syntax, and specific functions for data extraction and exploitation.
- **Checks:** MySQL error messages; information_schema access; MySQL-specific functions; Stacked queries; File operations (LOAD_FILE, INTO OUTFILE); User-defined functions
- **Key cmd:** `TARGET="https://target.com/product?id="`
- **CWE:** []

### WSTG-INPV-05.3 — Testing for SQL Injection - SQL Server
- **Dir:** `wstg-inpv-05.3`
- **Tests:** Microsoft SQL Server-specific SQL injection testing leverages MSSQL's unique features including xp_cmdshell for OS command execution, OPENROWSET for data exfiltration, and specific error messages. MSSQL often runs with elevated privileges, making successful exploitation particularly dangerous.
- **Checks:** MSSQL error messages; xp_cmdshell availability; Stacked queries support; OPENROWSET data exfiltration; System table access; Linked servers
- **Key cmd:** `TARGET="https://target.com/product?id="`
- **CWE:** []

### WSTG-INPV-05.4 — Testing for SQL Injection - PostgreSQL
- **Dir:** `wstg-inpv-05.4`
- **Tests:** PostgreSQL-specific SQL injection testing exploits PostgreSQL's unique features including dollar-quoted strings, array operations, COPY command for file operations, and extension capabilities. PostgreSQL is common in modern web stacks and offers powerful features that can be exploited.
- **Checks:** PostgreSQL error messages; String concatenation (||); Dollar-quoted strings; COPY command file access; Extension functions; Large object operations
- **Key cmd:** `TARGET="https://target.com/product?id="`
- **CWE:** []

### WSTG-INPV-05.5 — Testing for SQL Injection - MS Access
- **Dir:** `wstg-inpv-05.5`
- **Tests:** Microsoft Access SQL injection testing targets Access databases (Jet/ACE engine) often used in legacy or small-scale web applications. Access has limited features compared to enterprise databases but can still be exploited for data extraction and authentication bypass.
- **Checks:** Access-specific error messages; MSysObjects system table; IIF() function (Access-specific); TOP keyword instead of LIMIT; Date format (#date#)
- **Key cmd:** `TARGET="https://target.com/product?id="`
- **CWE:** []

### WSTG-INPV-05.6 — Testing for NoSQL Injection
- **Dir:** `wstg-inpv-05.6`
- **Tests:** NoSQL injection targets NoSQL databases (MongoDB, CouchDB, Redis, etc.) where traditional SQL injection techniques don't apply. These databases use different query languages and data structures, but are still vulnerable to injection attacks through JSON payloads, JavaScript execution, and operator m
- **Checks:** MongoDB operator injection ($gt, $ne, $regex); JSON injection in queries; JavaScript execution (server-side); Authentication bypass; Array/object injection; Redis command injection
- **Key cmd:** `TARGET="https://target.com/api/login"`
- **CWE:** []

### WSTG-INPV-05.7 — Testing for ORM Injection
- **Dir:** `wstg-inpv-05.7`
- **Tests:** ORM (Object-Relational Mapping) Injection occurs when attackers exploit vulnerabilities in ORM frameworks (Hibernate, SQLAlchemy, ActiveRecord, Entity Framework) by manipulating query parameters or HQL/JPQL/LINQ queries. Even though ORMs provide abstraction, improper use can still lead to injection 
- **Checks:** HQL/JPQL injection (Hibernate/JPA); Dynamic query building; Raw SQL within ORM; Query parameter manipulation; Filter/Order injection; Mass assignment vulnerabilities
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

### WSTG-INPV-05.8 — Testing for Client-Side SQL Injection
- **Dir:** `wstg-inpv-05.8`
- **Tests:** Client-side SQL injection targets local databases accessed via JavaScript, such as Web SQL Database (deprecated but still present), IndexedDB with SQL-like queries, or SQLite in mobile applications (Cordova, React Native). While less common than server-side SQLi, it can expose sensitive local data o
- **Checks:** Web SQL Database usage; SQLite in hybrid mobile apps; IndexedDB query manipulation; Local storage SQL parsing; Electron app databases; Browser extension databases
- **CWE:** []

### WSTG-INPV-06 — Testing for LDAP Injection
- **Dir:** `wstg-inpv-06`
- **Tests:** LDAP Injection occurs when user input is incorrectly filtered or not sanitized before being included in LDAP queries. Attackers can modify LDAP queries to bypass authentication, extract sensitive directory information, or modify directory data.
- **Checks:** Authentication forms using LDAP; User search functionality; Directory lookups; Filter manipulation; DN (Distinguished Name) injection; Boolean-based blind injection
- **Key cmd:** `TARGET="https://target.com/login"`
- **CWE:** [CWE-90]

### WSTG-INPV-07 — Testing for XML Injection
- **Dir:** `wstg-inpv-07`
- **Tests:** XML Injection occurs when user input is incorporated into XML documents without proper validation or encoding. This includes XML External Entity (XXE) injection, XPath injection, and XML tag injection. These vulnerabilities can lead to data disclosure, server-side request forgery, denial of service,
- **Checks:** XML External Entity (XXE) injection; Billion Laughs attack (XML bomb); XML tag injection; SOAP injection; XML parameter entities; Blind XXE via out-of-band
- **Key cmd:** `TARGET="https://target.com/api/process"`
- **CWE:** [CWE-91]

### WSTG-INPV-08 — Testing for SSI Injection
- **Dir:** `wstg-inpv-08`
- **Tests:** Server-Side Includes (SSI) Injection occurs when an attacker can inject SSI directives into web pages that are processed by the web server. SSI allows embedding dynamic content into HTML pages, and successful injection can lead to arbitrary command execution, file disclosure, or other server-side at
- **Checks:** SSI directive injection; File inclusion via SSI; Command execution via SSI; Virtual includes; .shtml, .stm, .shtm extensions; XBitHack configuration
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-90]

### WSTG-INPV-09 — Testing for XPath Injection
- **Dir:** `wstg-inpv-09`
- **Tests:** XPath Injection occurs when user input is incorporated into XPath queries without proper validation. Attackers can manipulate queries to bypass authentication, access unauthorized data, or extract the entire XML document. Unlike SQL injection, XPath has no access control, making the entire document 
- **Checks:** XPath query manipulation; Authentication bypass; Data extraction; Boolean-based blind injection; Error-based injection; XML document traversal
- **Key cmd:** `TARGET="https://target.com/search"`
- **CWE:** [CWE-78]

### WSTG-INPV-10 — Testing for IMAP/SMTP Injection
- **Dir:** `wstg-inpv-10`
- **Tests:** IMAP/SMTP Injection occurs when user input is incorporated into mail server commands without proper validation. Attackers can manipulate email functionality to send spam, access other users' mailboxes, execute arbitrary IMAP/SMTP commands, or bypass email-based security controls.
- **Checks:** Email header injection; IMAP command injection; SMTP command injection; CC/BCC injection; From address spoofing; Newline/CRLF injection
- **Key cmd:** `TARGET="https://target.com/contact"`
- **CWE:** [CWE-601]

### WSTG-INPV-11 — Testing for Code Injection
- **Dir:** `wstg-inpv-11`
- **Tests:** Code Injection occurs when an application incorporates user input into code that is dynamically executed. This includes injection into interpreted languages (PHP, Python, JavaScript, Ruby) through functions like eval(), exec(), or similar. Successful exploitation leads to arbitrary code execution on
- **Checks:** eval() with user input; exec() with user input; Dynamic code execution; Template evaluation; Serialization vulnerabilities; Dynamic function calls
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-94, CWE-95]

### WSTG-INPV-11.1 — Testing for File Inclusion (LFI/RFI)
- **Dir:** `wstg-inpv-11.1`
- **Tests:** File Inclusion vulnerabilities occur when applications dynamically include files based on user input. Local File Inclusion (LFI) allows reading files from the server, while Remote File Inclusion (RFI) allows including files from remote URLs, potentially leading to remote code execution.
- **Checks:** Local File Inclusion (LFI); Remote File Inclusion (RFI); Directory traversal; PHP wrappers exploitation; Log poisoning; Null byte injection
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

### WSTG-INPV-12 — Testing for Command Injection
- **Dir:** `wstg-inpv-12`
- **Tests:** Command Injection (OS Command Injection) occurs when an application passes unsafe user data to a system shell. Attackers can execute arbitrary operating system commands, potentially gaining full control of the server.
- **Checks:** Shell metacharacter injection; Command chaining operators; Backtick command substitution; Blind command injection; Out-of-band command injection
- **Key cmd:** `TARGET="https://target.com/api/ping"`
- **CWE:** []

### WSTG-INPV-13 — Testing for Format String Injection
- **Dir:** `wstg-inpv-13`
- **Tests:** Format String vulnerabilities occur when user input is used as the format string argument in functions like printf, sprintf, fprintf (C/C++) or similar functions in other languages. Attackers can read from or write to memory, crash applications, or achieve code execution.
- **Checks:** Printf-family functions with user input; Log functions with format strings; Error messages with format strings; Memory disclosure via %x, %p; Application crashes via %n
- **Key cmd:** `TARGET="https://target.com/api"`
- **CWE:** []

### WSTG-INPV-14 — Testing for Incubated Vulnerabilities
- **Dir:** `wstg-inpv-14`
- **Tests:** Incubated vulnerabilities are attacks where the malicious payload is stored initially and executed later in a different context or time. These include stored XSS that triggers on admin pages, time-delayed SQL injection, or payloads that activate when processed by scheduled jobs or different users.
- **Checks:** Stored payloads executed in different contexts; Admin panel stored XSS; Scheduled job exploitation; Second-order SQL injection; Email/notification triggers; Report/export functionality exploitation
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

### WSTG-INPV-15 — Testing for HTTP Splitting/Smuggling
- **Dir:** `wstg-inpv-15`
- **Tests:** HTTP Request Smuggling occurs when front-end and back-end servers interpret HTTP request boundaries differently. HTTP Response Splitting injects CRLF characters to manipulate headers. Both can lead to cache poisoning, session hijacking, XSS, or bypassing security controls.
- **Checks:** CRLF injection in headers; CL.TE smuggling; TE.CL smuggling; TE.TE smuggling; HTTP desync attacks; Cache poisoning
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

### WSTG-INPV-16 — Testing for HTTP Incoming Requests
- **Dir:** `wstg-inpv-16`
- **Tests:** This test examines how applications handle incoming HTTP requests, including unusual methods, oversized headers, malformed requests, and protocol-level attacks. Proper handling prevents denial of service, information disclosure, and bypass of security controls.
- **Checks:** Oversized headers handling; Malformed requests handling; HTTP method handling; Request body size limits; Timeout handling; Connection handling
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

### WSTG-INPV-17 — Testing for Host Header Injection
- **Dir:** `wstg-inpv-17`
- **Tests:** Host Header Injection occurs when applications trust the Host header value without validation. This can lead to cache poisoning, password reset poisoning, SSRF, and access to internal virtual hosts. Many applications use the Host header to generate URLs, making this a critical vulnerability.
- **Checks:** Password reset poisoning; Cache poisoning; Web cache deception; Access to internal hosts; SSRF via Host header; Routing manipulation
- **Key cmd:** `TARGET="target.com"`
- **CWE:** []

### WSTG-INPV-18 — Testing for Server-Side Template Injection (SSTI)
- **Dir:** `wstg-inpv-18`
- **Tests:** Server-Side Template Injection occurs when user input is embedded in templates in an unsafe manner. Attackers can inject template directives to execute arbitrary code on the server, read files, or access sensitive data. This affects frameworks like Jinja2, Twig, Freemarker, Velocity, and others.
- **Checks:** Template engine detection; Sandbox escape; Remote code execution; File read via templates; Blind SSTI; Framework-specific payloads
- **Key cmd:** `TARGET="https://target.com/page"`
- **CWE:** []

### WSTG-INPV-19 — Testing for Server-Side Request Forgery (SSRF)
- **Dir:** `wstg-inpv-19`
- **Tests:** Server-Side Request Forgery (SSRF) occurs when an attacker can make the server-side application make HTTP requests to an arbitrary domain of the attacker's choosing. This can be used to attack internal services, access cloud metadata, scan internal networks, or bypass access controls.
- **Checks:** URL parameter manipulation; Internal service access; Cloud metadata access; Protocol smuggling; Blind SSRF; DNS rebinding
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

### WSTG-INPV-20 — Testing for Mass Assignment
- **Dir:** `wstg-inpv-20`
- **Tests:** Mass Assignment (also known as Auto-binding or Object Injection) occurs when an application automatically binds user-provided data to internal objects. Attackers can modify object properties they shouldn't have access to, such as changing user roles, prices, or account status by adding extra paramet
- **Checks:** Hidden parameter injection; Role/privilege escalation; Price/amount manipulation; Status field modification; Admin flag injection; Timestamp manipulation
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

---

## WSTG-ERRH — Error Handling (2)

### WSTG-ERRH-01 — Testing for Improper Error Handling
- **Dir:** `wstg-errh-01`
- **Tests:** Improper error handling can reveal sensitive information about the application's internal workings, including technology stack, database structure, file paths, and configuration details. Attackers use this information to craft more targeted attacks. Proper error handling should provide minimal infor
- **Checks:** Stack traces exposed; Database error messages; File path disclosure; Framework/version info; Debug information; Internal IP addresses
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-209]

### WSTG-ERRH-02 — Testing for Stack Traces
- **Dir:** `wstg-errh-02`
- **Tests:** Stack traces provide detailed information about application internals including function call sequences, file paths, line numbers, and sometimes variable values. When exposed to users, stack traces can reveal sensitive implementation details that help attackers understand the application architectur
- **Checks:** Stack traces in error responses; Debug mode enabled; Exception details exposed; Framework-specific error pages; API error responses; JavaScript console errors
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-209]

---

## WSTG-CRYP — Cryptography (4)

### WSTG-CRYP-01 — Testing for Weak Transport Layer Security
- **Dir:** `wstg-cryp-01`
- **Tests:** Transport Layer Security (TLS) protects data in transit between clients and servers. Weak TLS configurations can allow attackers to intercept, decrypt, or modify communications. This test evaluates the strength of TLS implementation including protocol versions, cipher suites, certificate validity, a
- **Checks:** Protocol versions (TLS 1.2/1.3 only); Cipher suite strength; Certificate validity and chain; HSTS implementation; Certificate pinning (mobile); Mixed content issues
- **Key cmd:** `TARGET="target.com"`
- **CWE:** [CWE-326]

### WSTG-CRYP-02 — Testing for Padding Oracle
- **Dir:** `wstg-cryp-02`
- **Tests:** A padding oracle attack exploits the information leaked when a system reveals whether decrypted data has valid padding. This occurs with block ciphers in CBC mode when the application returns different error messages or behaviors for valid versus invalid padding. Attackers can use this to decrypt ci
- **Checks:** CBC mode encryption usage; Different responses for padding errors; Timing differences in responses; Error message differences; Encrypted cookies/tokens; ASP.NET ScriptResource/WebResource
- **Key cmd:** `curl -sI "https://target.com" | grep -i "set-cookie"`
- **CWE:** [CWE-326]

### WSTG-CRYP-03 — Testing for Sensitive Information Sent via Unencrypted Channels
- **Dir:** `wstg-cryp-03`
- **Tests:** Sensitive data transmitted over unencrypted channels (HTTP) can be intercepted by attackers through man-in-the-middle attacks. This includes credentials, session tokens, personal information, and financial data. All sensitive communications must use encrypted channels (HTTPS) with proper configurati
- **Checks:** Login forms over HTTP; Session tokens over HTTP; Sensitive data in HTTP requests; Mixed content issues; HTTP to HTTPS redirects; API calls over HTTP
- **Key cmd:** `TARGET="target.com"`
- **CWE:** [CWE-311]

### WSTG-CRYP-04 — Testing for Weak Encryption
- **Dir:** `wstg-cryp-04`
- **Tests:** Weak encryption can occur through the use of outdated algorithms, insufficient key lengths, improper implementation, or predictable initialization vectors. This test identifies cryptographic weaknesses in data encryption at rest and in transit within the application.
- **Checks:** Encryption algorithm strength; Key length adequacy; IV/nonce randomness; ECB mode usage; Hardcoded keys; Custom crypto implementations
- **Key cmd:** `curl -s "https://target.com/api/user/export" | \`
- **CWE:** [CWE-327]

---

## WSTG-BUSL — Business Logic (10)

### WSTG-BUSL-01 — Test Business Logic Data Validation
- **Dir:** `wstg-busl-01`
- **Tests:** Business logic data validation testing examines whether the application correctly validates data according to business rules, not just technical constraints. While technical validation (data type, format, length) is often implemented, business-level validation (logical ranges, relationships, state t
- **Checks:** Numeric ranges (prices, quantities, percentages); Date/time logic (booking dates, age restrictions); Relationship validation (dependent fields); State transitions (order status, account state); Calculation integrity (totals, discounts); Cross-field validation
- **Key cmd:** `curl -s "https://target.com/api/products/1" | jq '{price, min_qty, max_qty}'`
- **CWE:** [CWE-840]

### WSTG-BUSL-02 — Test Ability to Forge Requests
- **Dir:** `wstg-busl-02`
- **Tests:** Request forgery testing examines whether an application properly validates the authenticity and integrity of requests. Attackers may attempt to forge requests by predicting parameters, manipulating tokens, replaying captured requests, or bypassing client-side controls. This test identifies weaknesse
- **Checks:** Predictable tokens/identifiers; Missing request validation; Replay attack vulnerability; Parameter manipulation; Missing integrity checks; Client-side validation bypass
- **Key cmd:** `curl -s -X POST "https://target.com/api/transaction" \`
- **CWE:** [CWE-840]

### WSTG-BUSL-03 — Test Integrity Checks
- **Dir:** `wstg-busl-03`
- **Tests:** Integrity testing examines whether an application properly validates that data has not been tampered with during transmission or storage. Applications may rely on checksums, hashes, digital signatures, or HMAC to ensure data integrity. This test identifies weaknesses in integrity verification mechan
- **Checks:** Checksum validation; Hash verification; Digital signature validation; HMAC implementation; Encryption integrity (authenticated encryption); Database integrity constraints
- **Key cmd:** `curl -s "https://target.com/api/order/123" \`
- **CWE:** [CWE-840]

### WSTG-BUSL-04 — Test for Process Timing
- **Dir:** `wstg-busl-04`
- **Tests:** Process timing testing examines whether an application's business logic can be exploited through timing attacks or race conditions. Attackers may exploit timing vulnerabilities to bypass security controls, perform double-spending attacks, or gain unauthorized access. This includes testing for race c
- **Checks:** Race conditions in transactions; Double-spending attacks; Time-of-check time-of-use (TOCTOU); Parallel request exploitation; Timing-based enumeration; Session timing issues
- **Key cmd:** `echo "Identified targets:`
- **CWE:** [CWE-840]

### WSTG-BUSL-05 — Test Number of Times a Function Can Be Used Limits
- **Dir:** `wstg-busl-05`
- **Tests:** Function usage limit testing examines whether an application properly enforces restrictions on how many times a user can perform specific actions. These limits protect against abuse, fraud, and resource exhaustion. Attackers may attempt to bypass these controls to gain unfair advantages, such as unl
- **Checks:** Daily/weekly/monthly transaction limits; Free trial limitations; Download quotas; API rate limits; Voting/rating limits; Coupon/promotional code usage
- **Key cmd:** `for i in {1..50}; do`
- **CWE:** [CWE-840]

### WSTG-BUSL-06 — Test Circumvention of Work Flows
- **Dir:** `wstg-busl-06`
- **Tests:** Workflow circumvention testing examines whether an application properly enforces the intended sequence of steps in multi-step processes. Many business processes require specific steps to be completed in order (e.g., shopping cart → checkout → payment → confirmation). Attackers may attempt to skip st
- **Checks:** Step sequence enforcement; State validation between steps; Direct URL/endpoint access; Back button/history manipulation; Bookmark/link sharing vulnerabilities; Parameter manipulation for step skipping
- **CWE:** [CWE-840]

### WSTG-BUSL-07 — Test Defenses Against Application Misuse
- **Dir:** `wstg-busl-07`
- **Tests:** Application misuse defense testing examines whether an application has adequate controls to detect and prevent abuse patterns. This includes testing for automated attack detection, unusual behavior monitoring, and defensive measures against brute force, scraping, credential stuffing, and other abuse
- **Checks:** Rate limiting implementation; Account lockout policies; CAPTCHA deployment; IP-based blocking; Behavioral analysis; Automated attack detection
- **Key cmd:** `ENDPOINTS=(`
- **CWE:** [CWE-840]

### WSTG-BUSL-08 — Test Upload of Unexpected File Types
- **Dir:** `wstg-busl-08`
- **Tests:** File upload functionality is a common attack vector where attackers attempt to upload malicious files that can lead to remote code execution, denial of service, or information disclosure. This test examines whether the application properly validates uploaded files and rejects unexpected or dangerous
- **Checks:** File extension filtering; MIME type validation; Magic number/file signature verification; File content inspection; File size limits; Filename sanitization
- **Key cmd:** `curl -s "https://target.com/api/upload" -X OPTIONS`
- **CWE:** [CWE-840]

### WSTG-BUSL-09 — Test Upload of Malicious Files
- **Dir:** `wstg-busl-09`
- **Tests:** This test examines whether the application properly scans and rejects files containing malicious content such as malware, exploits, or embedded scripts. Even if file type validation is in place, malicious content within allowed file types (e.g., macro-enabled Office documents, PDFs with JavaScript, 
- **Checks:** Malware/virus detection; Office macros; PDF JavaScript; Image-based exploits; Archive bombs (zip bombs); Embedded scripts in allowed formats
- **Key cmd:** `echo 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > eicar.txt`
- **CWE:** [CWE-840]

### WSTG-BUSL-10 — Test Payment Functionality
- **Dir:** `wstg-busl-10`
- **Tests:** Payment functionality testing examines the security of e-commerce and financial transaction features. This includes testing for price manipulation, currency conversion issues, payment flow bypasses, and other vulnerabilities that could result in financial loss. Payment systems are critical targets f
- **Checks:** Price integrity validation; Quantity manipulation; Currency handling; Discount/coupon abuse; Payment flow integrity; Refund functionality
- **Key cmd:** `curl -s -X POST "https://target.com/api/cart/add" \`
- **CWE:** []

---

## WSTG-CLNT — Client-side (15)

### WSTG-CLNT-01 — Testing for DOM-Based Cross Site Scripting
- **Dir:** `wstg-clnt-01`
- **Tests:** DOM-based XSS occurs when client-side JavaScript processes data from untrusted sources and writes it to the DOM without proper sanitization. Unlike reflected or stored XSS, the payload never reaches the server - the entire attack happens in the browser. This makes DOM XSS harder to detect with serve
- **Checks:** document.URL; document.location; document.referrer; window.location; window.name; localStorage/sessionStorage
- **CWE:** [CWE-79]

### WSTG-CLNT-01.1 — Testing for Self DOM-Based XSS
- **Dir:** `wstg-clnt-01.1`
- **Tests:** Self DOM-Based XSS (also called Self-XSS) occurs when users are tricked into executing malicious JavaScript in their own browser context. While the attack requires social engineering, it can still lead to session theft or account compromise if combined with other vulnerabilities.
- **Checks:** Console paste protection; Self-XSS warnings; Input fields vulnerable to paste attacks; Developer tools protections
- **CWE:** []

### WSTG-CLNT-02 — Testing for JavaScript Execution
- **Dir:** `wstg-clnt-02`
- **Tests:** This test identifies scenarios where user input can lead to arbitrary JavaScript execution through various vectors including javascript: URIs, event handlers, and dynamic code evaluation.
- **Checks:** javascript: URI handling; Event handler injection; eval() with user input; Function constructor abuse; Template literal injection
- **Key cmd:** `curl -s "https://target.com/redirect?url=javascript:alert(1)"`
- **CWE:** [CWE-79]

### WSTG-CLNT-03 — Testing for HTML Injection
- **Dir:** `wstg-clnt-03`
- **Tests:** HTML injection allows attackers to inject arbitrary HTML content into web pages. While not as severe as XSS (no script execution), it can be used for phishing, defacement, or to manipulate page content to trick users.
- **Checks:** Form fields reflected in page; URL parameters in HTML; Error messages with user input; Search results display; User profile content
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-94]

### WSTG-CLNT-04 — Testing for Client-Side URL Redirect
- **Dir:** `wstg-clnt-04`
- **Tests:** Client-side URL redirect vulnerabilities (open redirects) occur when JavaScript redirects users based on URL parameters without validation. Attackers can craft links that redirect victims to malicious sites, facilitating phishing attacks.
- **Checks:** location.href assignments; location.replace() calls; window.open() with user input; meta refresh with parameters; Form action manipulation
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-601]

### WSTG-CLNT-05 — Testing for CSS Injection
- **Dir:** `wstg-clnt-05`
- **Tests:** CSS injection allows attackers to inject malicious CSS into web pages. While typically less severe than XSS, it can be used for data exfiltration (via attribute selectors), UI redressing, content spoofing, and in some cases, JavaScript execution in older browsers.
- **Checks:** Style attribute injection; CSS in user-controlled content; @import directive injection; expression() in IE; Data exfiltration via CSS
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-94]

### WSTG-CLNT-06 — Testing for Client-Side Resource Manipulation
- **Dir:** `wstg-clnt-06`
- **Tests:** Client-side resource manipulation occurs when attackers can control what resources (scripts, styles, images) a page loads. This can lead to loading malicious scripts, defacement, or data theft by manipulating URLs of external resources.
- **Checks:** Dynamic script loading; User-controlled src attributes; JSONP endpoints; Dynamic CSS loading; iframe src manipulation
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-200]

### WSTG-CLNT-07 — Testing for Cross-Origin Resource Sharing (CORS)
- **Dir:** `wstg-clnt-07`
- **Tests:** CORS is a browser mechanism that allows controlled access to resources from different origins. Misconfigured CORS policies can allow malicious websites to read sensitive data from authenticated users, leading to data theft.
- **Checks:** Wildcard (\*) Access-Control-Allow-Origin; Origin reflection without validation; null origin acceptance; Credentials with permissive CORS; Internal endpoints exposed
- **Key cmd:** `TARGET="https://target.com/api/user"`
- **CWE:** [CWE-942]

### WSTG-CLNT-08 — Testing for Cross-Site Flashing
- **Dir:** `wstg-clnt-08`
- **Tests:** Cross-Site Flashing (XSF) vulnerabilities occur in Flash/SWF applications when user input is improperly handled. Although Flash is deprecated, legacy applications may still use it. Similar vulnerabilities can exist in other rich media technologies.
- **Checks:** Flash files on target site; crossdomain.xml configuration; External data loading in SWF; User input in Flash parameters; Legacy rich media content
- **Key cmd:** `TARGET="target.com"`
- **CWE:** [CWE-1021]

### WSTG-CLNT-09 — Testing for Clickjacking
- **Dir:** `wstg-clnt-09`
- **Tests:** Clickjacking (UI redressing) tricks users into clicking hidden elements by overlaying transparent frames over legitimate UI. Attackers can make users unknowingly perform actions like changing settings, making purchases, or granting permissions.
- **Checks:** X-Frame-Options header; Content-Security-Policy frame-ancestors; JavaScript frame-busting code; Sensitive actions without confirmation; iframe embedding allowed
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-922]

### WSTG-CLNT-10 — Testing WebSockets
- **Dir:** `wstg-clnt-10`
- **Tests:** WebSockets provide full-duplex communication channels over a single TCP connection. Security issues can arise from missing authentication, lack of input validation, cross-site WebSocket hijacking, and insecure data transmission.
- **Checks:** WebSocket authentication; Origin validation; Input validation; Encryption (WSS); Rate limiting; Authorization per message
- **CWE:** [CWE-200]

### WSTG-CLNT-11 — Testing Web Messaging
- **Dir:** `wstg-clnt-11`
- **Tests:** HTML5 Web Messaging (postMessage API) allows cross-origin communication between windows/frames. Vulnerabilities arise when messages are sent without proper origin validation or when received messages are processed without sanitization, leading to XSS or data leakage.
- **Checks:** postMessage origin validation; Message data sanitization; Sensitive data in messages; Wildcard (\*) targetOrigin; Message handler implementation
- **CWE:** [CWE-79]

### WSTG-CLNT-12 — Testing Browser Storage
- **Dir:** `wstg-clnt-12`
- **Tests:** Browser storage mechanisms (localStorage, sessionStorage, IndexedDB, cookies) can store sensitive data client-side. Vulnerabilities occur when sensitive information is stored insecurely, accessible to XSS attacks, or persists longer than necessary. Testing ensures proper data protection and lifecycl
- **Checks:** Sensitive data in localStorage; Sensitive data in sessionStorage; IndexedDB data exposure; Cookie security attributes; Data persistence and cleanup; Access control to stored data
- **CWE:** [CWE-79]

### WSTG-CLNT-13 — Testing for Cross-Site Script Inclusion (XSSI)
- **Dir:** `wstg-clnt-13`
- **Tests:** Cross-Site Script Inclusion (XSSI) allows attackers to steal sensitive data by including a victim's JavaScript files as script sources from an attacker-controlled page. This exploits the fact that JavaScript files may contain sensitive user data and are not protected by Same-Origin Policy when loade
- **Checks:** Dynamic JavaScript endpoints; JSON responses loadable as scripts; JSONP endpoints; Authenticated script resources; Sensitive data in JavaScript; Callback parameter manipulation
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** [CWE-942]

### WSTG-CLNT-14 — Testing for Reverse Tabnabbing
- **Dir:** `wstg-clnt-14`
- **Tests:** Reverse Tabnabbing is a phishing attack where a malicious page opened via `target="_blank"` can modify the opener page's location through `window.opener`. This can redirect users to a phishing page while they believe they're still on the original site.
- **Checks:** Links with target="\_blank"; rel="noopener noreferrer" attribute; window.open() calls without noopener; User-generated links; Dynamic link creation
- **Key cmd:** `TARGET="https://target.com"`
- **CWE:** []

---

## WSTG-APIT — API (4)

### WSTG-APIT-00 — API Testing Overview
- **Dir:** `wstg-apit-00`
- **Tests:** APIs (Application Programming Interfaces) are the backbone of modern applications, enabling communication between different services, mobile apps, and frontend interfaces. API security testing focuses on identifying vulnerabilities specific to API implementations including authentication, authorizat
- **Checks:** API key security; OAuth implementation; JWT validation; BOLA (IDOR) vulnerabilities; BFLA (Function-level auth); Rate limiting
- **Key cmd:** `TARGET="target.com"`
- **CWE:** []

### WSTG-APIT-01 — API Reconnaissance
- **Dir:** `wstg-apit-01`
- **Tests:** API reconnaissance involves discovering and documenting all available API endpoints, understanding their functionality, and identifying potential attack surfaces. This includes finding undocumented endpoints, deprecated versions, and understanding the API structure.
- **Checks:** Public API documentation; Hidden/undocumented endpoints; API versions; Authentication mechanisms; Rate limiting; Response formats
- **Key cmd:** `TARGET="target.com"`
- **CWE:** [CWE-200]

### WSTG-APIT-02 — Testing for Broken Object Level Authorization (BOLA)
- **Dir:** `wstg-apit-02`
- **Tests:** Broken Object Level Authorization (BOLA), also known as IDOR, occurs when an API fails to validate that the requesting user has permission to access the requested object. Attackers can manipulate object identifiers to access data belonging to other users.
- **Checks:** User ID manipulation; Resource ID tampering; UUID/GUID enumeration; Access control on all endpoints; Horizontal privilege escalation; Batch/bulk operations
- **Key cmd:** `curl -s -H "Authorization: Bearer $TOKEN" \`
- **CWE:** [CWE-200]

### WSTG-APIT-99 — Testing GraphQL
- **Dir:** `wstg-apit-99`
- **Tests:** GraphQL is a query language for APIs that allows clients to request exactly the data they need. While flexible, GraphQL APIs introduce unique security challenges including introspection, batching attacks, nested queries, and authorization bypass opportunities.
- **Checks:** Introspection enabled; Authorization per field/type; Query depth limits; Query complexity limits; Batching vulnerabilities; Injection attacks
- **Key cmd:** `TARGET="target.com"`
- **CWE:** []

---

## Rollup / Multi-domain Skills (4)

These dirs aggregate multiple WSTG categories (category field is a broad label, not a single test).

### wstg-auth-session — WSTG identity, authentication, authorization, and session management testing
- **Dir:** `wstg-auth-session` | category: ``

### wstg-injection — WSTG input validation and injection testing - SQLi, XSS, SSTI, SSRF, command injection, XXE
- **Dir:** `wstg-injection` | category: ``

### wstg-logic-client-api — WSTG business logic, client-side, and API security testing
- **Dir:** `wstg-logic-client-api` | category: ``

### wstg-recon-config — WSTG reconnaissance, configuration, error handling, and cryptography testing techniques
- **Dir:** `wstg-recon-config` | category: ``
