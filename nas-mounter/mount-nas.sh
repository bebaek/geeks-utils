#!/bin/bash
# Mount NAS user home

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 USERNAME"
    exit
fi

gio mount smb://betelgeuse.local/"$1"

echo Checking mountpoint...
ls "/run/user/$(id -u $USER)/gvfs/smb-share:server=betelgeuse.local,share=$USER"
