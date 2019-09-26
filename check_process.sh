#!/bin/bash

dir_array=(
"/home/jordan/tests/libav/install/bin/angr-depth-expt"
"/home/jordan/tests/FreeImage/Examples/Generic/angr-result-depth"
"/home/jordan/tests/FreeImage/Examples/Generic/angr-result-depth"
"/home/jordan/tests/giflib-5.2.1/install/bin/angr-depth-expt"
"/home/jordan/tests/giflib-5.2.1/install/bin/angr-depth-expt"
"/home/jordan/tests/libpng-1.6.36/contrib/examples/angr-depth-expt"
"/home/jordan/tests/libpng-1.6.36/contrib/examples/angr-depth-expt"

)

script_array=(
"angr_drive.py"
"drive.py"
"angr_drive.py"
"drive.py"
"angr_drive.py"
"drive.py"
"angr_drive.py"

)

i=0
while true; do
    sleep 10
    echo "sleep"
    count=`ps -ef|grep jordan|grep python3|grep -v grep |wc -l`
    if [ $count -eq 0 ]
    then
        #echo $count
        echo ${dir_array[$i]},${script_array[$i]} > /home/jordan/tests/angr-smse-scripts/log
        cd ${dir_array[$i]}
        #head ../${script_array[$i]}
        timeout -s INT 6h python3 ../${script_array[$i]} 
        i=`expr $i + 1`
    fi
    if [ $i -eq 7 ]
    then
        echo "break"
        break
    fi
done
