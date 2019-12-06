#!/bin/bash

# "/home/jordan/tests/podofo-0.9.5/install/bin/angr-depth-expt"
# "/home/jordan/tests/giflib-5.2.1/install/bin/angr-depth-expt"
# "/home/jordan/tests/pandore/angr-depth-expt"
# "/home/jordan/tests/libpng-1.6.36/contrib/examples/angr-depth-expt"
# "/home/jordan/tests/FreeImage/Examples/Generic/angr-depth-expt"
# "/home/jordan/tests/libav/install-default/bin/angr-depth-expt"
# "/home/jordan/tests/jpeg-9c/O0-g-install/bin/angr-result"
#"/home/jordan/tests/jpeg-9c/O0-g-install/bin/angr-depth-expt"
#"/home/jordan/tests/ImageMagick/O0-g-install/bin/angr-result"
#"/home/jordan/tests/ImageMagick/O0-g-install/bin/angr-depth-expt"

#"/home/jordan/tests/jpeg-9c/O0-g-install/bin/angr-depth-expt"
#"/home/jordan/tests/jpeg-9c/O0-g-install/bin/angr-result"
#"/home/jordan/tests/ImageMagick/O0-g-install/bin/angr-result"
#"/home/jordan/tests/libxml2-2.9.9/O0-g-install/bin/angr-result"
#"/home/jordan/tests/podofo-0.9.5/O0-g-install/bin/angr-result"


# "/home/jordan/tests/ffmpeg-3.1.3/install/bin/angr-depth-expt"

dir_array=(
"/home/jordan/tests/jpeg-9c/O0-g-install/bin/angr-depth-expt"
"/home/jordan/tests/libxml2-2.9.9/O0-g-install/bin/angr-depth-expt"
"/home/jordan/tests/ImageMagick/O0-g-install/bin/angr-depth-expt"
"/home/jordan/tests/podofo-0.9.5/O0-g-install/bin/angr-depth-expt"
"/home/jordan/tests/ffmpeg-3.1.3/O0-g-install/bin/angr-depth-expt"
)

script_array=(
"drive.py"
"drive.py"
"drive.py"
"drive.py"
"drive.py"
"drive.py"
"angr_drive.py"
"drive.py"
"angr_drive.py"
"drive.py"
"angr_drive.py"
"drive.py"


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
    if [ $i -eq 5 ]
    then
        echo "break"
        break
    fi
done
