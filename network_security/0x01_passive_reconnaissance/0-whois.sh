#!/bin/bash
whois "$1" | awk -F': *' '/^(Registrant|Admin|Tech) /{gsub(/Ext$/,"Ext:"); printf "%s%s,%s", (NR>1?"\n":""), $1, $2}' > "$1.csv"
