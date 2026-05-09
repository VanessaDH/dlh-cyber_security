#!/bin/bash
find "$1" -prem -4000 -exec ls -ldb {} \; 2>/dev/null
