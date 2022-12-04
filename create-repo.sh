#!/bin/bash
# This script creates an rpm repository layout in the current directory.
set -e

# Prepare system
# Set gpg rpm signing key id
echo "%_signature gpg
%_gpg_name C2FD94D27193AF9D55E351C529CA5218233BC283" > ./.rpmmacros

# Dump gpg private key into a file
echo "$private_key" > gpg-private-key.gpg

# Create repodata folder
createrepo_c .


# Copy built rpms to the current directory
cp ~/rpmbuild/RPMS/*/*.rpm .

# Sign rpms
rpm --addsign ./*.rpm

# Sign repodata
gpg --detach-sign --armor repodata/repomd.xml