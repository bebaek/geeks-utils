#!/bin/bash
# Set up development env.

# Exit if any command fails
set -e

echo Start: set up Python environment.
echo

devenv=secim_filter

# Packages for development
pkgs=(flake8)

# Create virtual environment. python3-venv is required.
# Use _venv/ instead of .venv/. Spacemacs cannot even handle the presence of .venv/.
echo Creating virtual environment...
python3 -m venv --clear "$HOME/_venv/$devenv"
. "$HOME/_venv/$devenv/bin/activate"
echo Activated $(which python)
echo

echo Installing the latest pip and wheel...
pip install -U pip
pip install wheel
echo

echo Installing required pip packages...
if [ ${#pkgs[@]} -ne 0 ]; then
    pip install ${pkgs[@]}
fi
echo

echo Installing tflite runtime from wheel url...
pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
echo

# Run setup.py
echo "Runnning local setup.py..."
pip install -e .
echo

echo End: set up Python environment. Start with activating the venv by
echo      . ~/_venv/secim_filter/bin/activate
