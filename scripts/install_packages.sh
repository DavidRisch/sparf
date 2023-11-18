#!/usr/bin/env bash

echo "install packages start:"
date

cd /mnt/workfiles/sparf

echo "pip freeze before:"
pip freeze

pip install -r requirements_2.txt -f https://storage.googleapis.com/jax-releases/jax_releases.html --no-warn-script-location

echo "pip freeze after:"
pip freeze

echo "install packages end:"
date
