#!/bin/bash
# This script creates an rpm repository layout in the current directory.
set -e

# Check if sha256sum of old and new rpms are the same
# Exit if they match
if sha256 -c eupnea-utils.sha256; then
  echo "RPM checksum matches -> no update needed"
  echo "Exiting"
  exit 0
fi

# Calculate sha256sum of new rpms
sha256sum eupnea-utils-*.rpm >eupnea-utils.sha256

# Set gpg rpm signing key id
echo "%_signature gpg
%_gpg_name C2FD94D27193AF9D55E351C529CA5218233BC283" >~/.rpmmacros

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
