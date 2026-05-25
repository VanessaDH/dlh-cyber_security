#!/bin/bash
find / -type d -perm -o+w 2>/dev/null | while read -r dir; do
	echo "$dir"
	chmod o-w "$dir" 2>/dev/null
done
