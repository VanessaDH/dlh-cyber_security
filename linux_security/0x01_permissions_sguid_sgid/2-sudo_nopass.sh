#!/bin/bash
sudo bash -c "cat >> /etc/sudoers <<< \"$1 ALL=(ALL) NOPASSWD:ALL\""
