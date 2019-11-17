#!/bin/bash
# Push package config file to share dir

# Process args
. util/proc-args.sh

backup="$share.bak"

# Create share directory as needed
if [[ ! -d "$share_pkg_dir" ]]; then
    echo Creating $share_pkg_dir...
    mkdir "$share_pkg_dir"
fi

# Alert user
echo "Info: This copies your $local to $share."

# Backup
if [ -f "$share" ]; then
    mv -v "$share" "$backup"
fi

# Push
cp -v "$local" "$share"
