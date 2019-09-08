#!/bin/bash
# Pull spacemacs config from repo.

local="$HOME/.spacemacs"
share="./data/_spacemacs"
backup="$local.bak"

# Warn about the security consequence
echo "Warning: This copies $share to $local. Make sure no malicious code is \
contained in $share."

# Check working directory
if [ ! -f "${0##*/}" ]; then
    echo Run "${0}" in its directory. Exiting...
    exit 1
fi

# Backup
if [ -f "$local" ]; then
    mv -v "$local" "$backup"
fi

# Pull
cp -v "$share" "$local"
