#!/bin/bash
# Push spacemacs config to repo.

local="$HOME/.spacemacs"
share="./data/_spacemacs"
backup="$share.bak"

# Check working directory
if [ ! -f "${0##/}" ]; then
    echo Run "${0}" in its directory.
    exit 1
fi

# Backup
if [ -f "$share" ]; then
    mv -v "$share" "$backup"
fi

# Push
cp -v "$local" "$share"
