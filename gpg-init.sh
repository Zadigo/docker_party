#!/bin/bash/

# A script that initializes a GPG
# key on the server for trust purposes
# https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key

EMAIL=""

# Chooe 1 and then 4096 bit
gpg --full-generate-key

gpg --list-secret-keys --keyid-format=long

# Copy the tring after rsa4096/ on the ec line and
# ue it there
gpg --armor --export $key
