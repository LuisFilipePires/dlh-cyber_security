## Network Protocols: Auditing and Securing

### 0-iptables.sh

- `sudo`
  runs the command with administrator (root) privileges

- `iptables`
  Linux firewall tool used to manage network traffic rules

- `-L`
  lists all current firewall rules

- `--line-numbers`
  adds line numbers to each rule (useful to delete or modify specific rules)

- `-v`
  verbose mode → shows detailed information (packets, bytes, interfaces)

- `-n`
  numeric output → shows IP addresses and ports without resolving names (faster and clearer)

---
### exercice 2-harden.sh

- `find /` searches the entire system starting from the root directory `/`

- `-xdev` does not cross other filesystems or mounted partitions

- `-type d` searches only directories

- `-perm 0002` finds files with write permission for others

- `-print` prints the results (find items)

- `-exec` executes a command on the found results

- `chmod o-w` removes write permission for others (`o`)

- `{}` represents the currently found item

- `+` executes commands in batch (more efficient)

---

### 3-identify.sh
#### #!/bin/bash
#### sudo lynis audit system


Lynis is a security auditing tool that scans a Linux system and checks its security posture.

It verifies:

- `Security patches` It checks whether the system and installed software are up to date and if known security updates are missing.
- `Misconfigurations` It looks for unsafe or incorrect system settings that could weaken security.
- `Exposed services` It detects running services that are accessible from the network and could increase attack surface.
- `Incorrect permissions` It checks file and directory permissions to ensure sensitive data is not accessible to unauthorized users.
- `Known vulnerabilities` It compares system components against known security issues and common weakness patterns.

---

###  4-audit.sh
#### grep -Ev '^\s*#|^\s*$' /etc/ssh/sshd_config

- `grep` tool to filter the text
- `-E` extended regular expressions
- `-v` invert match - shows everything except `patern`
-  `^\s*#` remove all comment lines (lines starting with optional spaces followed by #)
-  `^` line beginning
-  `\s` spaces
-  `#` comments
-  `|` regular expression -> OR
-  `^\s*$'` empty lines
-  `/etc/ssh/sshd_config` path

---

### 5-sshd_config
#### cat 5-sshd_config
- Protocol 2
- PermitRootLogin no
- PasswordAuthentication no
- PermitEmptyPasswords no
- PubkeyAuthentication yes
- X11Forwarding no
- Port 22

`Protocol 2` Uses only SSH version 2. SSHv2 is the secure and modern version of the SSH protocol. It fixes vulnerabilities present in SSHv1 and provides stronger encryption and authentication.

`PermitRootLogin no` Disables direct root login. This prevents users from logging in directly as the root user via SSH. Instead, users must log in with a normal account and use sudo, reducing the risk of brute-force attacks on the root account.

`PasswordAuthentication no` Disables password-based login. Only key-based authentication is allowed. This is more secure because SSH keys are much harder to brute-force compared to passwords.

`PermitEmptyPasswords no` Prevents empty passwords. Users are not allowed to log in if their account has no password set. This closes a serious security vulnerability.

`PubkeyAuthentication yes` Enables public key authentication. Allows users to authenticate using SSH keys instead of passwords. This is the recommended and most secure method.

`X11Forwarding no` Disables graphical forwarding over SSH. Prevents remote graphical applications from being forwarded through SSH. This reduces attack surface and improves security.

`Port 22` Defines the SSH listening port. Port 22 is the default SSH port. While it is commonly used, it is also frequently scanned by attackers. In real hardening, this is often changed to a non-standard port.

---

### 6-nfs.sh
#### !/bin/bash
#### showmount -e "$1"

`NFS` (Network File System) allows sharing folders over a network.

`showmount` consulting NFS servers tool

`-e` list

---

### 7-snmp.sh

#### grep "public" /etc/snmp/snmpd.conf

`SNMP` uses community strings as passwords. If the default public community is enabled, unauthorized users may access system or network information.

`SNMP` (Simple Network Management Protocol) monitors network devices
- routers
- switches
- servers
- printers

---

### 8-smtp.sh

When TLS/STARTTLS is enabled:

email content is encrypted in transit

login credentials are protected

attackers cannot easily read or modify messages

---

### 9-tls_version.txt

The TLS versions were tested using OpenSSL. A version is considered supported only if a valid protocol handshake is successfully negotiated. If the server does not properly negotiate the protocol version, it is marked as not supported. Modern servers typically disable TLS 1.0 and TLS 1.1 due to security vulnerabilities, while TLS 1.2 and TLS 1.3 are usually enabled.

---
