#!/usr/bin/env bash

git clone https://github.com/AngoraFuzzer/Angora.git

ANGORA_PATH=$(realpath Angora)

cd Angora
mkdir llvm-install

PREFIX=$ANGORA_PATH/llvm-install ./build/install_llvm.sh
PREFIX=$ANGORA_PATH/llvm-install export PATH=$PREFIX/clang+llvm/bin:$PATH
PREFIX=$ANGORA_PATH/llvm-install export LD_LIBRARY_PATH=$PREFIX/clang+llvm/lib:$LD_LIBRARY_PATH

./build/build.sh

echo core | sudo tee /proc/sys/kernel/core_pattern

# run tests
cd tests
./test.sh mini

# command for libjpeg
CC=/home/shelven/Documents/fuzzing/Angora/bin/angora-clang \
CXX=/home/shelven/Documents/fuzzing/Angora/bin/angora-clang++ \
LD=/home/shelven/Documents/fuzzing/Angora/bin/angora-clang \
./configure --disable-shared --prefix=/home/shelven/Documents/fuzzing/angora-targets/install

# Build with taint tracking support
USE_TRACK=1 make -j$(nproc)
make install

# Save the compiled target binary into a new directory
# and rename it with .taint postfix, such as uniq.taint

# Build with light instrumentation support
make clean
USE_FAST=1 make -j$(nproc)
make install

# remember to use extremely simple seed
./angora_fuzzer -i ../angora-targets/jpeg-9c/input -o ../angora-targets/jpeg-9c/output -t ../angora-targets/install/bin/djpeg.taint -- ../angora-targets/install/bin/djpeg.fast @@



# prepare the abilist
cd $ANGORA_PATH/tools

# fix the script

# diff --git a/tools/gen_library_abilist.sh b/tools/gen_library_abilist.sh
# index f6b6d49..cb95a19 100755
# --- a/tools/gen_library_abilist.sh
# +++ b/tools/gen_library_abilist.sh
# @@ -24,7 +24,7 @@ if [ "$NM" = "" ]; then
#      exit 1
#  fi

# -echo "# $1" | grep 'so$'
# +echo "# $1" | grep 'so'
#  if [ $? -eq 0 ]
#  then

touch podofo_abilist.txt
./gen_library_abilist.sh /usr/lib/x86_64-linux-gnu/libfreetype.so.6 >> podofo_abilist.txt discard
./gen_library_abilist.sh /usr/lib/x86_64-linux-gnu/libz.so >> podofo_abilist.txt discard
./gen_library_abilist.sh /usr/lib/x86_64-linux-gnu/libfontconfig.so >> podofo_abilist.txt discard

# command for podofo
# first comment out the useless FIND_PACKAGE in CmakeLists.txt
mkdir build && cd build

CC=/home/shelven/Documents/fuzzing/Angora/bin/angora-clang \
CXX=/home/shelven/Documents/fuzzing/Angora/bin/angora-clang++ \
LD=/home/shelven/Documents/fuzzing/Angora/bin/angora-clang \
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="/home/shelven/Documents/fuzzing/angora-targets/install" -DCMAKE_C_FLAGS="-O0 -g" -DCMAKE_CXX_FLAGS="-O0 -g" -DPODOFO_BUILD_SHARED=FALSE PODOFO_BUILD_STATIC=TRUE ..

export ANGORA_TAINT_RULE_LIST=$ANGORA_PATH/tools/podofo_abilist.txt
USE_TRACK=1 make -j$(nproc)
...
