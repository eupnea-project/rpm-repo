#!/bin/bash

# This script is called on reboot after installing a new kernel

# one of the following commands will fail due to dnf preventing the removal of the currently running kernel
# this is fine, we just want to remove the other kernel
dnf remove -y eupnea-mainline-kernel || true
dnf remove -y eupnea-chromeos-kernel || true
