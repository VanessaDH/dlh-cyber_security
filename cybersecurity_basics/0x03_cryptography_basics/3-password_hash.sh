#!/bin/bash
salt=$(openssl rand -base64 16) && echo -n "$1$sal" | openssl dgst -sha512 > 3_hash.txt
