#!/bin/bash
find / -type d -perm -o+w 2>/dev/null -print -exec echo {} \; -exec chmod o-w {} \; 2>/dev/null 
