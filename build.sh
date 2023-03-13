#!/bin/bash

# Simple little script used to "build" the latest package, generate a
# reStructure README, and push it to pypi. All in one little go.
# How fun is that?

# Do the sdist thing
python3 setup.py sdist

# Grab the latest build from the 'dist' folder
latest_build=`ls -tp dist | grep -v /$ | head -1`

# Convert README.md to README.rst, because maintaining two READMEs would be silly
pandoc README.md --from markdown --to rst -s -o README.rst

# Upload that sucker to pypi
twine upload dist/$latest_build
