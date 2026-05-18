#!/bin/bash
john --format=raw-sha1 --wordlist=/usr/share/wordlists/rockyou.txt "$1" ; john --show --format=raw-sha1 "$1" | cut -d: -f2 | sed '$d' > 4-password.txt
