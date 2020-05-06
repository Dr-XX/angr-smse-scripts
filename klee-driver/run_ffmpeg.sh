#!/bin/sh

klee -write-cvcs -write-cov -output-module -max-memory=63000 -max-time=21600 -watchdog -only-output-states-covering-new -debug-crosscheck-core-solver=z3 -solver-backend=z3 \
	-link-llvm-lib=/home/jordan/tests/ffmpeg-3.1.3/install/lib/libavcodec.bca  \
	-link-llvm-lib=/home/jordan/tests/ffmpeg-3.1.3/install/lib/libavdevice.bca \
	-link-llvm-lib=/home/jordan/tests/ffmpeg-3.1.3/install/lib/libavfilter.bca \
	-link-llvm-lib=/home/jordan/tests/ffmpeg-3.1.3/install/lib/libswresample.bca \
	-link-llvm-lib=/home/jordan/tests/ffmpeg-3.1.3/install/lib/libswscale.bca \
	-link-llvm-lib=/home/jordan/tests/ffmpeg-3.1.3/install/lib/libavformat.bca \
	-link-llvm-lib=/home/jordan/tests/ffmpeg-3.1.3/install/lib/libavutil.bca \
	-libc=uclibc -posix-runtime /home/jordan/tests/ffmpeg-3.1.3/install/bin/ffmpeg.bc -i  A -sym-files 1 500
