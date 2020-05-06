import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime
import os
import sys
import re
import time

'''
ferry = [
    [46,20,20,21,20,26,29],#all
    [5, 20, 8,12,11, 2,24],#0~9
    [16, 0, 2, 9, 6,11, 5],#10~19
    [ 7, 0, 8, 0, 0, 2, 0],#20~29
    [ 6, 0, 2, 0, 0, 4, 0],#30
    [ 7, 0, 0, 0, 0, 0, 0],#40
    [ 5, 0, 0, 0, 3, 7, 0],#50
]
angr =  [
    [25, 0,11,11, 7,13, 0],#all
    [ 4, 0, 3, 7, 4, 0, 0],#0
    [12, 0, 1, 3,11, 0, 0],#10
    [ 4, 0, 6, 0, 0, 2, 0],#20
    [ 5, 0, 1, 0, 0, 0, 0],#30
    [ 0, 0, 0, 0, 0, 0, 0],#40
    [ 0, 0, 0, 0, 0, 0 ,0],#50
]
afl = [
    [23, 1, 1, 1, 1, 0, 0],
    [ 4, 1, 0, 1, 1, 0, 0],#0
    [13, 0, 1, 0, 0, 0, 0],#10
    [ 4, 0, 0, 0, 0, 0, 0],#20
    [ 2, 0, 0, 0, 0, 0, 0],#30
    [ 0, 0, 0, 0, 0, 0, 0],#40
    [ 0, 0, 0, 0, 0, 0, 0] #50
]
klee =  [
    [11, 0, 8, 2, 5, 13,0], #all
    [ 4, 0, 2, 1, 4, 0, 0],#0
    [ 3, 0, 1, 1, 0, 3, 0], #10
    [ 4, 0, 5, 0, 0, 2, 0], #20
    [ 0, 0, 0, 0, 0, 1, 0], #30
    [ 0, 0, 0, 0, 0, 0, 0], #40
    [ 0, 0, 0, 0, 1, 7, 0], #50
]
qsym =  [
    [15, 0, 1, 0, 0, 0, 0],
    [ 3, 0, 1, 0, 0, 0, 0],#0
    [ 9, 0, 0, 1, 0, 0, 0],#10
    [ 4, 0, 0, 0, 0, 0, 0],#20
    [ 2, 0, 0, 0, 0, 0, 0],#30
    [ 0, 0, 0, 0, 0, 0, 0],#40
    [ 0, 0, 0, 0, 0, 0, 0],#50
]
angora =[
    [27, 1, 0, 0, 4, 0, 0],
    [ 4, 1, 0, 0, 4, 0, 0],#0
    [15, 0, 0, 0, 0, 0, 0],#10
    [ 4, 0, 0, 0, 0, 0, 0],#20
    [ 2, 0, 0, 0, 0, 0, 0],#30
    [ 0, 0, 0, 0, 0, 0, 0],#40
    [ 2, 0, 0, 0, 0, 0, 0],#50
]
'''
ferry=[
    [5 , 5, 16, 7, 6, 7, 5], #jpeg
#    [20, 20, 0, 0, 0, 0, 0], #podofo
    [8 , 8, 2, 8, 2, 0, 0],  #giflib
    [12, 12, 9, 0, 0, 0, 0], #pandore
    [11, 11, 6, 0, 0, 0, 3], #jhead
    [2 , 2, 11, 2, 4, 0, 7], #libpng
#    [24, 24, 5, 0, 0, 0, 0]  #ffmpeg
]
angr=[[4, 4, 12, 4, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0], [3, 3, 1, 6, 1, 0, 0], [7, 7, 4, 0, 0, 0, 0], [4, 4, 3, 0, 0, 0, 0], [0, 0, 11, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
afl=[[4, 4, 13, 4, 2, 0, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
klee=[[4, 4, 3, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 2, 1, 5, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0, 1], [0, 0, 3, 2, 1, 0, 7], [0, 0, 0, 0, 0, 0, 0]]
qsym=[[3, 3, 9, 1, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
angora=[[4, 4, 15, 4, 2, 0, 2], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
bench = [ferry, angr, afl, klee, qsym, angora]
bench_name = ["ferry", "angr", "afl", "klee", "qsym", "angora"]
target_name = ["libjpeg","PoDoFo", "giflib", "pandore", "jhead", "libpng", "FFmpeg",]
#depth_range = ["all", "0~9", "10~19","20~29", "30~39", "40~49", "50~"]
depth_range=  ["0", "10", "20", "30", "40", "50", "60"]
target_len = [7, 2, 5, 3, 7, 7, 3]
lcolor = ["r", "limegreen", "gold", "gray" ,"deepskyblue","purple"]
linew = [3, 1.2, 1.7, 1.5 , 2,1.5]
f, ax = plt.subplots(figsize=(30,12),dpi=1080)
label_set = [True] *6
offset = 0
xticks_x = []
xticks_info = []
x_label = []



def draw(i, y,offset,length,line_color,tar_name, ben_name, set_label):
    y = y[0:length]
    x = [offset+0.25*i for i in range(length)]
    #bar = plt.bar(x = x, height = y, width=0.25, color="none", edgecolor="none")
    #print(y,offset,length,line_color,tar_name, ben_name, set_label)
    if ben_name == "ferry":
        xticks_x.extend(x)
        xticks_info.extend(depth_range[0:length])
        x_label.append((x[0]+x[-1]) / 2 - 0.25)

    plt.plot(x, y, color=line_color ,lw=linew[i], ms=10, label=ben_name)
    if set_label:
        plt.legend(prop = {'size':20})
    #for bi in bar:
    #    height = bi.get_height()
    #    plt.text(bi.get_x() + bi.get_width() / 4, height, str(bi.get_height()) , ha="center", va="bottom", size=16)


offset = 0
for j in range(len(target_name)): 
    for i in range(len(bench)):
        draw(i, bench[i][j], offset, target_len[j],lcolor[i],target_name[j], bench_name[i], label_set[i])
        if label_set[i]:
            label_set[i] = False
    offset += 0.25*target_len[j]
    offset += 0.5
plt.xticks(xticks_x, xticks_info, rotation=45, size = 16)
plt.yticks(size = 16)
plt.ylim(0,25)
for i in range(len(target_name)):
    plt.text(x_label[i], -2, target_name[i], size = 20)
#plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
plt.savefig("depth_bar.eps",dpi=1080,format='eps', bbox_inches='tight')
plt.show()


