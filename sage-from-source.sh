#!/usr/bin/env bash
# Author: Harald Schilly <harald.schilly@gmail.com>
# Author: Benjamin Jones <benjaminfjones@gmail.com>
# License: Apache 2.0
# This script downloads and installs Sage (http://www.sagemath.org) for you.
#
# This script requires that you have either `aria2c` or `wget` installed in
# order to download the sage source tarball.
#
# Usage: $ ./sage-from-source.sh 5.5.beta3
#

# break if any command has exit status != 0
set -e

# variables
#
TARGET=$HOME/sage
SAGE_MATH_WASH="http://sage.math.washington.edu"
SAGE_MATH_ORG="http://www.sagemath.org"
# uncomment for latest release
#VER=$(wget -O - $HOMEPAGE/version.html | tail -n 1)
VER=$1
META=$SAGE_MATH_ORG/mirror/src/meta/sage-$VER.tar.metalink
TAR=$SAGE_MATH_WASH/home/release/sage-$VER/sage-$VER.tar
FILE=sage-$VER.tar

# now the real part starts
#
cd $TARGET

# downloads sage-x.y.z.tar from the mirror network
#
aria2c --seed-time=0 -d $TARGET $META
# wget $TAR # uncomment for direct http download

# extracts sage
echo "Download complete, now extracting Sage ..."
tar xf $FILE

# compile
#
cd sage-$VER
export MAKE="make -j4" # change "4" to the number of desired simultaneous build processes
export SAGE_ATLAS_ARCH="fast"
export SAGE_PARALLEL_SPKG_BUILD="yes"
make build

# finished
echo
echo "If everything looks good, you can now now run Sage here:" $TARGET/sage-$VER/sage
