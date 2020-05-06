import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os
import sys
import re
import time

root_path = "/home/jordan/tests/smse-result/"
dir_name = ["rs_window_1","rs_window_3",
    #"rs_window_5",
    "rs_window_wan"
]
target_name = [
#    "ffmpeg",
#    "file",
#    "freeimage",
#    "giflib",
#    "imagemagick",
#    "jhead",
#    "libav",
#    "libjpeg",
#    "libpng",
#    "libtiff",
#    "libxml2",
    "mupdf",
#    "nm",
#    "objdump",
#    "pandore",
#    "podofo",
#    "readelf",
#    "size",
]

def get_log_list(target):
    rs_files = []
    for i in dir_name:
        rs_files.append(os.listdir(root_path + i))
    res = [""] * len(rs_files)
    for i in range(len(rs_files)):
        for rsi in rs_files[i]:
            if target in rsi and "log" in rsi:
                res[i] = os.path.join('%s/%s' % (root_path + dir_name[i], rsi))
                break;
    return res

def str2time(string):
    return datetime.strptime(string.split('|')[1].strip().split(',')[0], "%Y-%m-%d %H:%M:%S")

def str2num(string):
    tmp = string.split('<')[1]
    tmp_list = tmp.split(',')
    num = 0
    #not0 = False
    for i in tmp_list:
        if "unsat" in i:
            continue
        #if "active" in i :
        else :
            t = re.search(r'\d+', i)
            if t:
                num += int(t.group())
                #not0 = True   
            # break
    #if not0 == False :
    #    num = 0
    return num

def get_statistics(file_name):
    if file_name == "" :
        return [],[]
    fopen = open(file_name, 'r')
    fileread = fopen.readlines()
    fopen.close()
    start_time = str2time(fileread[0])
    time = []
    num = []
    for line in fileread:
        t=re.search(r'Stepping active of <SimulationManager',line)
        if t:
            now = str2time(line)
            if (now-start_time).seconds > 8100:
                break
            time.append((now-start_time).seconds)
            num.append(str2num(line))
    return time,num

def find_last(x, time3) :
    l = 0
    r = len(time3)
    while l < r :
        mid = (l+r) >>1
        if time3[mid] < x:
            l=mid + 1
        else :
             r = mid
    return time3[l:]

def find_pre(x, time3) :
    l = 0
    r = len(time3)
    while l < r :
        mid = (l+r) >>1
        if time3[mid] < x:
            l=mid + 1
        else :
             r = mid
    return l

def draw_line(target):
    target_list = get_log_list(target)
    # if "" in target_list:
    #     return
    time1, num1 = get_statistics(target_list[0])
    time3, num3 = get_statistics(target_list[1])
    time5, num5 = get_statistics(target_list[2])
    time1.append(time3[-1])
    time5.append(time3[-1])
    num1.append(17.5)
    num5.append(17)
    # timewan, numwan = get_statistics(target_list[3])
    fig,ax = plt.subplots(figsize=(5,4))
    
    line1 = ax.plot(time1,num1, '-', color = "orange", lw=2, label="window_length=1")
    line3 = ax.plot(time3,num3, '-', color = "limegreen", lw=2, label="window_length=3")
    line5 = ax.plot(time5,num5, '-', color = "deepskyblue",lw=2, label="window_length=unlimited")
    # linewan = ax.plot(timewan,numwan, '-', lw=0.5, label="rsw=1000")
    # ax.set_title("%s's stateNum change over time" % target)
    ax.set_xlabel("time(second)")
    ax.set_ylabel("number of execution path")
    ax.legend(loc = 4)
    # time1_ = [time1[-1]]
    # time1_.extend(find_last(time1[-1], time3))
    # num1_ = [num1[-1]]*len(time1_)
    # time5_ = [time5[-1]]
    # time5_.extend(find_last(time5[-1], time3))
    # num5_ = [num5[-1]]*len(time5_)
    # ax.plot(time1_,num1_, ':', color = "orange", lw=2)
    # ax.plot(time5_,num5_, ':', color = "deepskyblue",lw=2)
    ax.set_ylim(bottom = 0)
    ax.set_xlim(left = 0)
    xticks = list(range(0,8100,2000))
    ax.set_xticks(xticks[1:])
    plt.show()    
    plt.savefig("%s.eps" % target, format='eps')

def get_depth_list(target):
    rs_files = []
    for i in dir_name:
        rs_files.append(os.listdir(root_path + i))
    res = [""] * len(rs_files)
    for i in range(len(rs_files)):
        for rsi in rs_files[i]:
            if target in rsi and "depth" in rsi:
                res[i] = os.path.join('%s/%s' % (root_path + dir_name[i], rsi))
                break;
    return res

def get_depth_distribution(file_name):
    #0,1~5,6~10,...91~95,96~100
    depth_dist = [0]*50 
    if file_name == "" :
        return depth_dist
    fopen = open(file_name, 'r')
    fileread = fopen.readlines()
    fopen.close()
    for line in fileread:
        if ":" in line:
            t=re.search(r'\d+',line.split(':')[1])
            if t:
                tmp_depth = int(t.group())
                if tmp_depth == 0:
                    depth_dist[0] +=1
                else :
                    index = (tmp_depth-1) // 5
                    depth_dist[index] +=1
    return depth_dist

def draw_bar(target):
    depth_list = get_depth_list(target)
    dist1 = get_depth_distribution(depth_list[0])
    dist3 = get_depth_distribution(depth_list[1])
    dist5 = get_depth_distribution(depth_list[2])
    distwan = get_depth_distribution(depth_list[3])
    #a = ["0", "1~5", "6~10", "11~15", "16~20", "21~25", "26~30", "31~35", "36~40", "41~45", "46~50", "51~55", "56~60", "61~65", "66~70", "71~75", "76~80", "81~85", "86~90", "91~95", "96~100"]
    a = [i*5 for i in range(50)]
    x1 = list(range(len(a)))
    x3 = list(i+0.25 for i in x1)
    x5 = list(i+0.25 for i in x3)
    xwan = list(i+0.25 for i in x5)
    plt.figure(figsize=(20,8),dpi=80)
    plt.bar(x1,dist1,width=0.25,label="rsw=1")
    plt.bar(x3,dist3,width=0.25,label="rsw=3")
    plt.bar(x5,dist5,width=0.25,label="rsw=5")
    plt.bar(xwan,distwan,width=0.25,label="rsw=10000")
    plt.legend()
    plt.xticks(x3,a)
    plt.title("%s's block depth distribution" % target)
    plt.xlabel('depth')
    plt.ylabel("blockNum")
    plt.savefig("%s_depth_dist.png" % target)
    plt.show()

if __name__ == "__main__":
#    draw_line("libjpeg") 
    for ti in target_name:
        draw_line(ti)
        #draw_bar(ti)
