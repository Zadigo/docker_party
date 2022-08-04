#!/bin/bash/

# A script that initializes a GPG
# key on the server for trust purposes
# https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key

EMAIL=""

gpg --full-generate-key

gpg --list-secret-keys --keyid-format=long
