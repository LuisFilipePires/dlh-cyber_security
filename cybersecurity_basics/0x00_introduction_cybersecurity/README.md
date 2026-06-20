# dlh-cyber_security

### Exercice 0 0_release.sh

In the terminal, execute the script using:
$ ./0-realese.sh
> Kali

***
#!/bin/bash
lsb_release -is
***
The lsb_release command (Linux Standard Base) is used to display distribution-specific information.

flags -i -s
-i ID -> show identification distributor
-s short output -> show the short version

lsb_release -a -> all
lsb_release -rs -> version
lsb_release -cs -> codename
lsb_release -ds -> description

lsb_release -a 
No LSB modules are available.
Distributor ID: Kali
Description:    Kali GNU/Linux Rolling
Release:        2026.1
Codename:       kali-rolling


This information is usually stored in:
/etc/os-release or /etc/lsb-release
