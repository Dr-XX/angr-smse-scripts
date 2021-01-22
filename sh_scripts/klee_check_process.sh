#!/bin/bash


log_dir=(
"jpeg"
#"readelf"
#"size"
#"pandore"
#"file"
#"giflib"
#"ImageMagick"
#"jhead"
#"libpng"
)

binary_name=(
"djpeg.bc"
#"readelf.bc"
#"size.bc"
#"ppng2pan.bc"
#"file.bc"
#"giftext.bc"
#"magick.bc"
#"jhead.bc"
#"pngpixel.bc"
)


link_lib=(
"-link-llvm-lib=/home/jordan/tests/clang60-install/lib/libjpeg.bca"
#""
#""
#"-link-llvm-lib=/home/jordan/tests/clang60-install/lib/libpandore.bca"
#""
#""
#"-link-llvm-lib=/home/jordan/tests/clang60-install/lib/libMagickCore-7.Q16HDRI.bca -link-llvm-lib=/home/jordan/tests/clang60-install/lib/libMagickWand-7.Q16HDRI.bca -link-llvm-lib=/home/jordan/tests/clang60-install/lib/libjpeg.bca"
""
"-link-llvm-lib=/home/jordan/tests/clang60-install/lib/libpng16.bca"
)

binary_args=(
#"-a A"
"A"
"A"
"A"
"A"
"A"
"identify -verbose A"
"A"
"0 0 A"
)


i=0
while true; do
    sleep 10
    echo "sleep"
    #compile=`ps -ef|grep jordan|grep clang |grep -v grep |wc -l`
    #if [ $compile -eq 0 ]
    #then
        count=`ps -ef |grep jordan| grep klee |grep -v grep |wc -l`
        if [ $count -eq 0 ]
        then
            date >> log
            echo ${log_dir[$i]},${binary_path[$i]},${link_lib[$i]}, ${binary_args[$i]} >> log
            klee -write-cvcs -write-cov -output-module -max-memory=60000 -max-time=21600 -watchdog -only-output-states-covering-new -debug-crosscheck-core-solver=z3 -solver-backend=z3 -search=random-path ${link_lib[$i]} -libc=uclibc -posix-runtime -output-dir=/home/jordan/tests/clang60-install/test_result_random/${log_dir[$i]}  /home/jordan/tests/clang60-install/bin/${binary_name[$i]} ${binary_args[$i]} -sym-files 1 500
            i=`expr $i + 1`
        fi
    #fi
    if [ $i -eq 1 ]
    then
        echo "break"
        break
    fi
done
