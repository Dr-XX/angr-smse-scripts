#!/bin/bash

dir_array=(
"/home/jordan/tests/jpeg-9c/install/bin/angr-result-depth"
"/home/jordan/tests/libav/install/bin/angr-result-depth"
"/home/jordan/tests/libav/install/bin/angr-result-depth"
"/home/jordan/tests/FreeImage/Examples/Generic/angr-result-depth"
"/home/jordan/tests/FreeImage/Examples/Generic/angr-result-depth"
)

script_array=(
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
    count=`ps -ef|grep jordan|grep python3|wc -l`
    if [ $count -eq 0 ]
    then
        #echo $count
        echo ${dir_array[$i]},${script_array[$i]}
        cd ${dir_array[$i]}
        #head ../${script_array[$i]}
        timeout -s INT 6h python3 ../${script_array[$i]} 
        i=$i+1
    fi
    if [ $i -eq 5 ]
    then
        break
    fi
done
