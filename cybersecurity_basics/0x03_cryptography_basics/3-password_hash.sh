#!/bin/bash
salt=$(openssl rand -base64 16)
combined="$1$sal"
echo -n "$combined" | openssl dgst -sha512
