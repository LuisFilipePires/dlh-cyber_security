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
