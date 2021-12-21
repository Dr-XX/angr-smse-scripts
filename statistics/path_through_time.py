#-*- coding: UTF-8 -*- 
import matplotlib
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimSun'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
# plt.rcParams.update({'font.size': 7.5})
plt.rcParams['font.size']=13
import sys


root_path="/home/jordan/tests/target-afl-install/"
fuzzer_path=[
    "afl-output/",
    "afl++-output/",
    "fairfuzz-output/",
    "chunkfuzzer-output/",
]

fuzzer_linestyle=[
    ":",
    "-.",
    "--",
    "-"
]
fuzzer_label = [
    "AFL",
    "AFL++",
    "FairFuzz",
    "ChunkFuzzer"
]

target_path=[
    "1/vorbis/",
    "1/openjpeg/",
    "1/pngpixel/",
    "2/djpeg/",
    "1/tcpdump/",
    "1/podofopdfinfo/",
]

target_path2=[
    "--",
    "--",
    "2/pngpixel/png/",
    "--",
    "2/tcpdump/pcap/",
    "2/podofopdfinfo/pdf/"
]

label_name=[
    "Vorbis",
    "OpenJPEG",
    "Libpng",
    "Libjpeg",
    "tcpdump",
    "PoDoFo"
]

f, ax = plt.subplots(2,3,figsize=(12,8),dpi=1080)
# f, ax = plt.subplots(1,1,figsize=(8,12),dpi=1080)


def get_data(path, divisor):
    plot_file = open(path, "r")
    plot_file.readline()
    line = plot_file.readline().strip()
    time = []
    inputs = []
    while line:
        data = line.split(",")
        time.append((int)(data[0])/divisor)
        # inputs.append((float)(data[6].split("%")[0]) * 100)
        inputs.append((int)(data[3]))
        line = plot_file.readline().strip()
    start = time[0]
    for i in range(0, len(time)):
        time[i] = time[i] - start
    return time, inputs

def draw(x, y, i):
    for j in range(4):
        divisor = 1
        if j == 1 :
            if i in [0,2,4,5] :
                divisor = 1000
        plot_path = root_path+fuzzer_path[j]+target_path[i]+"plot_data"
        if j == 1 :
            if i in [2,4,5]:
                print(i,j)
                plot_path = root_path+fuzzer_path[j]+target_path2[i]+"plot_data"
        time, path_cnt = get_data(plot_path, divisor)
        # print(time,path_cnt)
        ax[x][y].plot(time,path_cnt,color='black',linestyle=fuzzer_linestyle[j], label=fuzzer_label[j])
        if i == 4: 
            ax[x][y].legend(bbox_to_anchor=(0, -0.2), loc=3, borderaxespad=0, ncol=4, frameon=False)
    ax[x][y].set_title(label_name[i])
    


for i in range(6) :
    x = i // 3
    y = i % 3
    draw(x, y, i)

# draw(0, 0, 0)

plt.savefig("inputs_time2.png",dpi=1080,format='png', bbox_inches='tight')
plt.show()
