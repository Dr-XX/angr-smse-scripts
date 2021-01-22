###compile


#deflault
#see validate.sh

#afl
export CC=/home/jordan/tools/afl-2.52b/afl-gcc CXX=/home/jordan/tools/afl-2.52b/afl-g++
#same as default

#CLANG
./configure --prefix=/home/jordan/tests/lava_corpus/LAVA-M/base64/coreutils-8.24-lava-safe/lava-install/clang --disable-nls CFLAGS="-g -O1 -Xclang -disable-llvm-passes -D__NO_STRING_INLINES  -D_FORTIFY_SOURCE=0 -U__OPTIMIZE__" LIBS="-lacl"
make -j6
make install
get-bc xxxx


###run
#angr
#see ~/test/tests/smse-evaluation-driver

#afl
#see /home/jordan/tests/lava-result/afl/check_process.sh


