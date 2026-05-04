#!/bin/bash
grep -w "ID" /etc/os-release | cut -d= -f2
