#!/bin/bash

set -e

ROOT=`git rev-parse --show-toplevel`
BASEURL="http://stat-computing.org/dataexpo/2009"
SUFFIX=".csv.bz2"

echo "==> Downloading 1994-2008 Airlines data..."
for year in {1994..2008}; do
    URL="${BASEURL}/${year}${SUFFIX}"
    if [ ! -f $ROOT/dataset/${year}${SUFFIX} ]; then
        wget "$URL" -P $ROOT/dataset
    else
        echo "==> ${year}${SUFFIX} found. Skipping..."
    fi
done
echo "==> Done."