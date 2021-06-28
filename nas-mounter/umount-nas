#!/bin/bash
# Unmount NAS user home

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

gio mount -u "smb://$MYNAS/$user"

echo Done.
