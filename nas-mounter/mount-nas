#!/bin/bash
# Mount NAS user home

set -e

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 USERNAME"
    exit
fi

if [[ -z "$MYNAS" ]]; then
    echo MYNAS variable should be set.
    exit
fi

user="$1"
mountpoint="/run/user/$(id -u $USER)/gvfs/smb-share:server=betelgeuse.local,share=$user"

gio mount "smb://$MYNAS/$user"

echo Checking mountpoint...
ls -d "$mountpoint"
ls "$mountpoint"
echo Done.
