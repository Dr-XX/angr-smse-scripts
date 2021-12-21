#-*- coding: UTF-8 -*- 
import matplotlib
from matplotlib import font_manager as fm, rcParams
# from matplotlib.font_manager import *
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 6.0)
plt.rcParams['font.sans-serif']=['SimSun'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
# from matplotlib import rcParams
# config = {
#     "font.family":'serif',
#     "font.size": 6,
#     "mathtext.fontset":'stix',
#     "font.serif": ['SimSun'],
# }
# rcParams.update(config)
import sys

labels =        ['OGG', 'JP2', 'PNG', 'JPEG', 'PCAP', 'PDF']
true_positive = [0,      5,     5,     12,     1,      9]
editor010 =     [3,      5,     6,     12,     1,      13]
X = range(len(true_positive))

rects1 = plt.bar(x=X, height=true_positive, width=0.2, alpha=0.8, color='white', edgecolor='black', hatch='/', label='ChunkFuzzer识别正确块数')
rects2 = plt.bar(x=[i + 0.25 for i in X], height=editor010, width=0.2, color='black', label='010 Editor识别块数')
plt.ylim(0, 15)

for x,y in zip(X,true_positive):
    plt.text(x,y+0.05,'%d' %y, ha='center',va='bottom')

for x,y in zip(X,editor010):
    plt.text(x+0.25,y+0.05,'%d' %y, ha='center',va='bottom')

plt.xticks([index + 0.2 for index in X], labels)
# plt.title("ChunkFuzzer块结构识别精确率", fontproperties=myfont)
# plt.title("ChunkFuzzer块结构识别精确率")
# plt.legend(prop=myfont, loc="upper left")
plt.legend(loc="upper left")

plt.savefig("true_positive_compare2.png",dpi=1080,format='png', bbox_inches='tight')
plt.show()
