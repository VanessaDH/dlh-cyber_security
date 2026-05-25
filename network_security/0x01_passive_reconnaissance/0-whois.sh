#!/bin/bash
whois "$1" | awk -F':[ \t]*' '/^(Registrant|Admin|Tech) /{gsub(/Ext[ \t]*$/, "Ext:", $1); printf "%s%s, %s", (NR>1 ? "\n" : ""), $1, $2}' > "$1.csv"
