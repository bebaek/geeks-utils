#!/bin/bash
# Set up generic Python development environment based on the standard venv.

echo Start: set up generic Python environment.

devenv=default

# Packages for development
pkgs=(flake8 ipython jupyterlab)

# Create virtual environment.
# Use _venv/. Spacemacs cannot even handle the presence of .venv/.
echo Creating virtual environment...
python3 -m venv --clear ~/_venv/default

# For Debian/Ubuntu, python3-venv package needs to be installed
stat=$?
if [ $stat -ne 0 ]; then
    echo venv needs to be installed. For Ubuntu, run: apt install python3-venv
    exit 1
fi

. ~/_venv/default/bin/activate

# Installing wheel first helps install certain packages (e.g., backcall)
echo Installing wheel by pip first...
pip3 install wheel

# Install support packages
echo Installing required pip packages...
if [ ${#pkgs[@]} -ne 0 ]; then
    pip3 install ${pkgs[@]}
fi

echo End: set up Python environment.
