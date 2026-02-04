#!/bin/bash
set -e

# 1. Download the official source
VERSION="0.7.0"
curl -L "https://github.com/sentriz/cliphist/archive/v${VERSION}/cliphist-${VERSION}.tar.gz" -o "cliphist-${VERSION}.tar.gz"

# 2. Unpack and generate a fresh vendor folder
tar -xf "cliphist-${VERSION}.tar.gz"
cd "cliphist-${VERSION}"
go mod vendor
tar -czf ../vendor.tar.gz vendor/
cd ..

# 3. Clean up (COPR only wants the spec and the tarballs in the result dir)
rm -rf "cliphist-${VERSION}"
