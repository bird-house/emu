#!/bin/bash

echo "Bootstrapping ..."

if [ -f /etc/debian_version ] ; then
    echo "Install Debian/Ubuntu packages for Birdhouse build ..."
    sudo apt-get update && sudo apt-get -y install python wget build-essential
elif [ -f /etc/redhat-release ] ; then
    echo "Install CentOS packages for Birdhouse build ..."
    sudo rpm -i http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
    sudo yum -y install wget gcc-c++
elif [ `uname -s` = "Darwin" ] ; then
    echo "Install Homebrew packages for Birdhouse build ..."
    brew install wget
fi

echo "Fetching current Makefile for Birdhouse build ..."
python -c 'import urllib; print urllib.urlopen("https://raw.githubusercontent.com/bird-house/birdhousebuilder.bootstrap/master/Makefile").read()' > Makefile

echo "Bootstrapping done"

