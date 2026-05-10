#!/bin/bash
find "$1" -type -f -mtime -1 -perm \( -perm -4000 -o -perm -2000 \) -exec ls -ldb {} \; 2>/dev/null
