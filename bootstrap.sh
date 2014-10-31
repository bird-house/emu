#!/bin/bash

echo "Starting bootstrap"
python -c 'import urllib; print urllib.urlopen("https://raw.githubusercontent.com/bird-house/birdhousebuilder.bootstrap/master/Makefile").read()' > Makefile
echo "Updated installation script"
echo "Bootstrap done"

