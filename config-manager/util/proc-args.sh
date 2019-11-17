#!/bin/bash
# Common code between push-config.sh and pull-config.sh

script="${0##*/}"
conf="paths.conf"

# Check working directory
if [ ! -f "$script" ]; then
    echo Run "${0}" in its directory. Exiting...
    exit 1
fi

# Import config paths
. "$conf"

usage="\
Usage: bash $script <package name> [<share directory>]
    <package name> should exist in paths.conf.
    <share directory> can be omitted if SHARE_DIR is set.
"

# Show usage and exit if no argument is given
if [[ $# -eq 0 ]]; then
    echo "$usage"
    exit 1
fi

# Select package from the argument
declare pkg="$1"
if [[ -z "${!pkg}" ]]; then
    echo "$pkg is not listed in $conf."
    exit 1
fi
local="${!pkg}"

# Other variables
if [[ -z "$SHARE_DIR" ]]; then
    if [[ $# -lt 2 ]]; then
        echo "Either <share directory> should be given or SHARE_DIR should be set."
        exit 1
    fi
    SHARE_DIR="$2"
fi

share_pkg_dir="$SHARE_DIR/$pkg"
share="$share_pkg_dir/${local##*/}"
