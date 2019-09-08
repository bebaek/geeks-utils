#!/bin/bash
# Push spacemacs config to repo.

local="$HOME/.spacemacs"
share="./data/_spacemacs"
backup="$share.bak"

# Warn about the security consequence
echo "Warning: This copies your $local to $share. Make sure no private \
information is shared before pushing the changes to the public domain."

# Check working directory
if [ ! -f "${0##*/}" ]; then
    echo Run "${0}" in its directory. Exitting...
    exit 1
fi

# Backup
if [ -f "$share" ]; then
    mv -v "$share" "$backup"
fi

# Push
cp -v "$local" "$share"
