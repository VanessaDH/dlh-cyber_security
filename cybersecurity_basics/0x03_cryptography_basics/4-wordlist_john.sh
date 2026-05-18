#!/bin/bash
john --wordlist=/urs/share/wordlists/rockyou.txt $1 && john --show $1 > 4-password.txt
