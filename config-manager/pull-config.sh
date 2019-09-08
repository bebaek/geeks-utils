#!/bin/bash
# Pull package config file from share dir

# Process args
. proc-args.sh

backup="$local.bak"

# Backup
if [ -f "$local" ]; then
    mv -v "$local" "$backup"
fi

# Pull
cp -v "$share" "$local"
