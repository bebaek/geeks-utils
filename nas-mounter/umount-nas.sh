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

gio mount -u "smb://$MYNAS/$1"

echo Done.
