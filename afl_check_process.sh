#!/bin/bash


log_dir=(
#"/home/jordan/tests/afl-install/test_result/ffmpeg-new"
"/home/jordan/tests/afl-install/test_result/libav"
#"/home/jordan/tests/afl-install/test_result/freeimage"
)

binary_path=(
#"/home/jordan/tests/afl-install/bin/ffmpeg"
"/home/jordan/tests/afl-install/bin/avconv"
#"/home/jordan/tests/afl-install/bin/freeimage_showmetadata"
)

afl_args=(
#" -m 1000 "
" -m 1000 "
)

binary_args=(
"-i @@"
"-i @@"
#"@@"

)


i=0
while true; do
    sleep 10
    echo "sleep"
    # compile=`ps -ef|grep jordan|grep clang |grep -v grep |wc -l`
    # if [ $compile -eq 0 ]
    # then
        count=`ps -ef|grep jordan|grep afl-fuzz |grep -v grep |wc -l`
        if [ $count -eq 0 ]
        then
            date >> log
            echo ${log_dir[$i]},${binary_path[$i]}, ${binary_args[$i]} >> log
            cd ${log_dir[$i]}
            AFL_SKIP_CRASHES=1 AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1 AFL_SKIP_CPUFREQ=1 LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/jordan/tests/afl-install/lib timeout -s INT 6h afl-fuzz ${afl_args[$i]} -i ../in -o . ${binary_path[$i]} ${binary_args[$i]}
            break
            i=`expr $i + 1`
        fi
    # fi
    if [ $i -eq 1 ]
    then
        echo "break"
        break
    fi
done
