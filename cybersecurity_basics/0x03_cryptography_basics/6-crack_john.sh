john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha256 "$1" ; john --show --format=raw-sha256 "$1" | awk -F: 'NF>1 {print $2}' > 6-password.txt
