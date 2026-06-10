#!/bin/bash
sudo hashcat -a 0 -m 0 "$1" /usr/share/wordlists/rockyou.txt -o 7-password.txt --outfile-format=2
