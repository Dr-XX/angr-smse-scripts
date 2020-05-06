#!/bin/sh
BCROOT=/home/jordan/tests/imgmgk/bc && \
NATIVEROOT=/home/jordan/tests/imgmgk/native && \
mkdir -p /home/jordan/tests/imgmgk ${NATIVEROOT} ${BCROOT}/bin ${BCROOT}/lib && \
cd /home/jordan/tests/imgmgk && \
#pip install --upgrade pip && \
#wget https://zlib.net/zlib-1.2.11.tar.gz && \
tar xvzf zlib-1.2.11.tar.gz && \
cd zlib-1.2.11 && \
CC=gclang CCFLAGS="-DDEBUG -g" ./configure --prefix=${NATIVEROOT} && \
make -j6 && \
get-bc libz.so && \
get-bc libz.a && \
make install && \
cp libz.bca ${BCROOT}/lib/ && \
cp libz.so.1.2.11.bc ${BCROOT}/lib/
\
cd .. && \
#wget https://downloads.sourceforge.net/project/libpng/libpng16/1.6.36/libpng-1.6.36.tar.gz  && \
tar xvzf libpng-1.6.36.tar.gz && \
cd libpng-1.6.36 && \
CC=gclang CCFLAGS="-DDEBUG -g" CPPFLAGS="-DPNG_NO_FLOATING_ARITHMETIC -I${NATIVEROOT}/include" LDFLAGS="-L${NATIVEROOT}/lib -Wl,--rpath -Wl,${NATIVEROOT}/lib" ./configure --prefix=${NATIVEROOT} && \
make -j6 && \
make install && \
get-bc .libs/libpng16.so.16.36.0 && \
get-bc .libs/libpng16.a && \
cp .libs/libpng16.bca ${BCROOT}/lib/ && \
cp .libs/libpng16.so.16.36.0.bc ${BCROOT}/lib/libpng16.so.bc && \
\
cd .. && \
#wget https://tukaani.org/xz/xz-5.2.3.tar.gz && \
tar xvzf xz-5.2.3.tar.gz && \
cd xz-5.2.3 && \
CC=gclang CCFLAGS="-DDEBUG -g" ./configure --prefix=${NATIVEROOT} --disable-assembler --enable-threads=no --enable-debug --disable-assembler --disable-nls && \
make -j6 && \
make install && \
get-bc src/liblzma/.libs/liblzma.a && \
get-bc src/liblzma/.libs/liblzma.so.5.2.3 && \
cp src/liblzma/.libs/liblzma.bca ${BCROOT}/lib/ && \
cp src/liblzma/.libs/liblzma.so.5.2.3.bc ${BCROOT}/lib/ && \
\
cd .. && \
#wget http://ijg.org/files/jpegsrc.v9a.tar.gz && \
tar xvzf jpegsrc.v9a.tar.gz && \
cd jpeg-9a && \
CC=gclang CCFLAGS="-DDEBUG -g -I${NATIVEROOT}/include" LDFLAGS="-L${NATIVEROOT}/lib" ./configure --prefix=${NATIVEROOT} && \
make -j6 && \
make install && \
get-bc .libs/libjpeg.so.9.1.0 && \
get-bc .libs/libjpeg.a && \
cp .libs/libjpeg.bca ${BCROOT}/lib/ && \
cp .libs/libjpeg.so.9.1.0.bc ${BCROOT}/lib/ && \
\
cd .. && \
#wget -c http://download.osgeo.org/libtiff/tiff-4.0.8.tar.gz && \
tar xvzf tiff-4.0.8.tar.gz && \
cd tiff-4.0.8 && \
CC=gclang CXX=gclang++ CCFLAGS="-DDEBUG -g" CPPFLAGS="-I${NATIVEROOT}/include" LDFLAGS="-L${NATIVEROOT}/lib" ./configure --prefix=${NATIVEROOT} --disable-cxx --disable-mdi && \
make -j6 && \
make install && \
get-bc ./libtiff/.libs/libtiff.so.5.2.6 && \
get-bc ./libtiff/.libs/libtiff.a && \
cp libtiff/.libs/libtiff.bca ${BCROOT}/lib/ && \
cp ./libtiff/.libs/libtiff.so.5.2.6.bc ${BCROOT}/lib/ && \
\
cd .. && \
#git clone https://github.com/ImageMagick/ImageMagick.git && \
 








