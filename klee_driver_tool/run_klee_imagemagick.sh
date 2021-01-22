#!/bin/sh

klee -write-cvcs -write-cov -output-module -max-memory=63000 -max-time=21600 -watchdog -only-output-states-covering-new -debug-crosscheck-core-solver=z3 -solver-backend=z3 -search=dfs -link-llvm-lib=/home/jordan/tests/ImageMagick/install-support/lib/libMagickCore-7.Q16.bca -link-llvm-lib=/home/jordan/tests/ImageMagick/install-support/lib/libMagickWand-7.Q16.bca -link-llvm-lib=/home/jordan/tests/ImageMagick/install-support/lib/libMagick++-7.Q16.bca -libc=uclibc -posix-runtime /home/jordan/tests/ImageMagick/install-support/bin/magick.bc identify -verbose A -sym-files 1 500
