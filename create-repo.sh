#!/bin/bash
# This script creates an rpm repository layout in the current directory.
set -e

# Set gpg rpm signing key id
echo "%_signature gpg
%_gpg_name C9C7B7290DB9747C72C310BA6323D07A20625E4D" >~/.rpmmacros

# Dump gpg private key into a file
echo "$private_key" >gpg-private-key.gpg

# import gpg private key
gpg --import gpg-private-key.gpg
# Dump public key into a file
echo "$public_key" >public_key.gpg

# Copy built rpms to the current directory
cp ~/rpmbuild/RPMS/*/*.rpm .

# Sign rpms
rpm --addsign ./*.rpm

# Create repodata folder
createrepo_c .

# Sign repodata
gpg --detach-sign --armor repodata/repomd.xml
