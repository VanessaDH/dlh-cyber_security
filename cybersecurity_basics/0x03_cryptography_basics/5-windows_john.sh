john --wordlist=/usr/share/wordlists/rockyou.txt --format=nt "$1"; john --show --format=nt "$1" | awk -F: 'NF>1 {print $2}' > 5-password.txt
