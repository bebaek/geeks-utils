#!/bin/sh
# Generates ssh key

# Check if usual key file exists
default_file="$HOME/.ssh/id_rsa"
if [ -f $default_file ]; then
   read -p "$default_file exists. Quit? ([y]/n) " yn
   if [ "$yn" != 'N' ] && [ "$yn" != 'n' ]; then
       exit 1
   fi
fi

# Generate key
read -p "Comment to insert? " comment
ssh-keygen -t rsa -b 4096 -C "$comment"
