#!/bin/bash
# Mount NAS user home

set -e

mountpoint="/run/user/$(id -u $USER)/gvfs/smb-share:server=betelgeuse.local,share=$USER"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 USERNAME"
    exit
fi

if [[ -z "$MYNAS" ]]; then
    echo MYNAS variable should be set.
    exit
fi

gio mount "smb://$MYNAS/$1"

echo Checking mountpoint...
ls -d "$mountpoint"
ls "$mountpoint"
echo Done.
