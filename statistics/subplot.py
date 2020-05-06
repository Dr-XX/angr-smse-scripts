import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime
import os
import sys
import re
import time

ferry=[
    [0 , 5, 16, 7, 6, 8, 4], #jpeg
    [0 , 13, 3, 3, 1, 0, 0], #podofo
    [0 , 8,  3, 8, 1, 0, 0],  #giflib
#    [0 , 6, 11, 4, 0, 0, 0], #pandore
    [0 , 11,  6, 0, 0, 0, 3], #jhead
    [0 , 2, 11, 7, 4, 0, 2], #libpng
    [0 , 16, 9, 4, 1, 0, 0 ] #ffmpeg
]
angr=[
    [0, 4, 12, 4, 5, 0, 0], #jpeg
    [0, 0,  0, 0, 0, 0, 0],
    [0, 3,  2, 5, 1, 0, 0],  #giflib
#    [0, 2,  7, 1, 0, 0, 0],  #pandore
    [0, 4,  3, 0, 0, 0, 0], #jhead
    [0, 0, 11, 2, 0, 0, 0], 
    [0, 0,  0, 0, 0, 0, 0]
]
afl=[
    [0, 4, 13, 4, 2, 0, 0], #jpeg
    [0, 1, 0,  0, 0, 0, 0],
    [0, 0,  1, 0, 0, 0, 0], 
#    [0, 1,  0, 0, 0, 0, 0], 
    [0, 1,  0, 0, 0, 0, 0], 
    [0, 0,  0, 0, 0, 0, 0],
    [0, 0,  0, 0, 0, 0, 0] 
]
klee=[
    [0, 4, 3, 4, 0, 0, 0], #jpeg
    [0, 0, 0, 0, 0, 0, 0],
    [0, 3, 2, 4, 0, 0, 0], 
#    [0, 1, 2, 0, 0, 0, 0], 
    [0, 4, 0, 0, 0, 0, 1], 
    [0, 0, 3, 7, 1, 0, 2], 
    [0, 0, 0, 0, 0, 0, 0]
]
qsym=[
    [0, 3, 9, 1, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0], 
#    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0]
]
angora=[
    [0, 4, 15, 4, 2, 1, 1], 
    [0, 1, 0,  0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0], 
#    [0, 0, 0, 0, 0, 0, 0], 
    [0, 4, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0]
]
bench = [ferry, angr, afl, klee, qsym, angora]
bench_name = ["Ferry", "angr", "AFL", "KLEE", "QSYM", "Angora"]
target_name = [
    "libjpeg", 
    "PoDoFo",
    "giflib", 
#    "pandore", 
    "jhead", 
    "libpng", 
    "ffmpeg"
]
depth_range= [
    ["0", "10", "20", "30", "40", "50", "60"],
    ["0", "5", "10", "15", "20"], # pandore, ffmpeg
    ["0", "2", "4", "6", "8"] #podofo
]

target_len = [
    7, #jpeg
    5, #podofo
    5, #giflib
#    4, #pandore
    7, #jhead 
    7, #libpng
    5, #ffmpeg
]
lcolor = ["r", "limegreen", "gold", "gray" ,"deepskyblue","purple"]
# linew = [3, 1.2, 1.7, 1.5 , 2,1.5]
f, ax = plt.subplots(1,6,figsize=(36,6),dpi=1080)
label_set = [True] *6
offset = 0
#xticks_x = []
#xticks_info = []
x_label = []



def draw(j, length ,tar_name):
    x = list(range(0,length))
    ymax = 0
    for i in range(len(bench)):
        y = np.cumsum(bench[i][j][0:length])
        if i == 0 :
            ymax = y[-1]
        #bar = plt.bar(x = x, height = y, width=0.25, color="none", edgecolor="none")
        ax[j].plot(x, y, color=lcolor[i] ,lw=2.5, ms=10, label=bench_name[i])
        if j == 3:
            ax[j].legend(bbox_to_anchor=(0, -0.18), loc=10, borderaxespad=0, ncol = 6, frameon = False ,prop = {'size':26})
    if j == 1:
         xticks_info = depth_range[2][0:length]
    elif j == 5:
        xticks_info = depth_range[1][0:length]
    else :
        xticks_info = depth_range[0][0:length]
    ax[j].set_xticks(x[1:])
    ax[j].set_xticklabels(xticks_info[1:],size = 24)
    yrange = ymax // 5
    ymax = (1 + ymax // 5) * 5
    ax[j].set_yticks(list(range(0, ymax, yrange)))
    ax[j].set_yticklabels(list(range(0, ymax, yrange)), size = 24)
    ax[j].set_ylim(bottom = 0)
    ax[j].set_xlim(left = 0)
    ax[j].set_title(tar_name, size = 30)
    #for bi in bar:
    #    height = bi.get_height()
    #    plt.text(bi.get_x() + bi.get_width() / 4, height, str(bi.get_height()) , ha="center", va="bottom", size=16)


offset = 0
for j in range(len(target_name)): 
    draw(j, target_len[j], target_name[j] ) 

# for i in range(len(target_name)):
#    plt.text(x_label[i], -2, target_name[i], size = 20)
# plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
plt.savefig("depth_bar_no_pandore_down.eps",dpi=1080,format='eps', bbox_inches='tight')
plt.show()


