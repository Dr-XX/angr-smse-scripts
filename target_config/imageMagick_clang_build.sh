#!/bin/sh

CC=gclang CXX=gclang++ CCFLAGS="-DDEBUG -g" CPPFLAGS="-I${NATIVEROOT}/include" LDFLAGS="-L${NATIVEROOT}/lib" ../../configure --prefix=${NATIVEROOT} --disable-openmp --disable-hdri --without-threads --without-bzlib --without-zstd --without-dps --without-fftw --without-flif --without-fpx --without-djvu --without-fontconfig --without-freetype --without-raqm --without-heic --without-jbig --without-lcms --without-openjp2 --without-lqr --without-lzma --without-openexr --without-pango --without-webp --without-xml  --without-jpeg --without-png --without-zlib --without-tiff
#CFLAGS="-DDEBUG -g -fprofile-arcs -ftest-coverage" LDFLAGS="-lgcov --coverage" 
