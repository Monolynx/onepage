#!/usr/bin/env bash

SECONDS=0

cd /vagrant_data/
sudo apt-get update -y
sudo apt-get install -y build-essential libssl-dev python3 python3-dev python3-setuptools git python3-imaging libffi-dev python-oauth2 python3-pip libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
# sudo easy_install pip
sudo apt-get install language-pack-en-base -y && sudo locale-gen en_US en_US.UTF-8 && sudo dpkg-reconfigure locales

# project specific system packages
sudo pip3 install setuptools==7.0
sudo pip3 install pyopenssl ndg-httpsclient pyasn1


