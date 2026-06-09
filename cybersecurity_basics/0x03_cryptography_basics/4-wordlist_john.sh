#!/bin/bash
john --show --format=raw-md5 hash.txt | cut -d: -f2 > 4-password.txt
