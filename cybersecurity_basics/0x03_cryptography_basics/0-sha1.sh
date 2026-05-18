#!/bin/bash
echo -n "$1" | sha1sum | tr -d " -">>hash.txt
