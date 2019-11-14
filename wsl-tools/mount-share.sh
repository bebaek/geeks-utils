#!/bin/bash
# Mount network share interactively by default

read -p "Mount target? " target

# FIXME: reuse saved server for matching target

read -p "Server name? " server
read -p "Share name? " share

sudo mount -t drvfs "\\\\$server\\$share" "$target"
