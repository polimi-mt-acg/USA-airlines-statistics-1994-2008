#!/bin/bash

set -e

BASEURL="http://stat-computing.org/dataexpo/2009"
SUFFIX=".csv.bz2"

echo "==> Downloading 1994-2008 Airlines data..."
for year in {1994..2008}; do
    URL="${BASEURL}/${year}${SUFFIX}"
    if [ ! -f "dataset/${year}${SUFFIX}" ]; then
        wget --directory-prefix=dataset "$URL"
    else
        echo "==> ${year}${SUFFIX} found. Skipping..."
    fi
done
echo "==> Done."