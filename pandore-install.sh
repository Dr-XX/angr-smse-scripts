#/bin/bash

#first, modify "configure"
#CXX=${CXX}
#CXXFLAGS="$CFLAGS -DNDEBUG -O0 -Iinclude"

export LD_LIBRARY_PATH=`pwd`/lib:$LD_LIBRARY_PATH
CC=gcc CXX=g++ ./configure --prefix=/home/jordan/tests/pandore/install
#CC=gclang CXX=gclang++
