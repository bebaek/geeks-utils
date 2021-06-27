#!/bin/bash
# Unmount NAS user home

set -e

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 USERNAME"
    exit
fi

gio mount -u smb://betelgeuse.local/"$1"
