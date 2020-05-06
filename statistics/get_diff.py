import sys
import os
import json

result_dir = ""
#"/home/jordan/tests/jpeg-9c/O0-g-install/bin/"    


smse_depth_name = ""
benchmark_depth = ""

smse_coverage = ""
benchmark_coverage = ""



def get_block_diff(so_offset):
    f_smse_coverage = open(smse_coverage)
    f_benchmark_coverage = open(benchmark_coverage)
    
    smse_coverage_cnt = int(f_smse_coverage.readline().strip())
    smse_coverage_tmp = set(int(i) for i in f_smse_coverage.readline()[1:-2].split(', '))
    smse_coverage_list = set()
    #ignore some unconcerned block
    for i in range(len(so_offset)):
        for j in smse_coverage_tmp:
            if i == 0 and  j < 0x1000000:
                smse_coverage_list.add(hex(j))
            elif j >= 0x1000000*so_offset[i][0] and j < 0x1000000*(so_offset[i][0]+1):
                smse_coverage_list.add(hex(j))
    smse_coverage_cnt = len(smse_coverage_list)

    benchmark_coverage_cnt = int(f_benchmark_coverage.readline().strip())
    benchmark_tmp = set(int(i) for i in f_benchmark_coverage.readline()[1:-2].split(', '))
    benchmark_coverage_list = set()
    for i in range(len(so_offset)):
        for j in benchmark_tmp :
            if i == 0 and  j < 0x1000000:
                benchmark_coverage_list.add(hex(j))
            elif j >= so_offset[i][1] and j <= so_offset[i][1]:
                #calculate offset
                benchmark_coverage_list.add(hex(j-so_offset[i][1]+0x1000000*so_offset[i][0]))
    benchmark_coverage_cnt = len(benchmark_coverage_list)

    print("smse coverage: %d, benchmark coverage: %d, "%(smse_coverage_cnt, benchmark_coverage_cnt))

    #diff
    smse_list = smse_coverage_list - benchmark_coverage_list
    benchmark_list = benchmark_coverage_list - smse_coverage_list
    print("smse - benchmark:%d" % len(smse_list))
    print(smse_list)
    print('\n')
    
    print("benchmark - smse:%d" % len(benchmark_list))
    print(benchmark_list)
    print('\n')

    #depth distribution,from 0-100
    distr = [0]*100
     
    #get depth from smse-depth-log
    with open(smse_depth_name) as f :
        smse_depth = json.load(f)

    print("smse - benchmark:%d" % len(smse_list))
    for it in smse_list:
        print ("addr:%s, depth:%d;" % (it,smse_depth[it]), end = ' ')
        distr[(smse_depth[it])] += 1
    print()
    print(distr)
    print()
    
    #get depth from angr-depth-log
'''
    distr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    angr_depth = open(result_dir +'/'+ angr_dir + angr_depth_name).readlines()
    angr_depth_dict = {}

    print("angr - smse:%d" % len(angr_smse_list))
    for i in range(len(angr_depth)) :
        tmp = angr_depth[i].split(':')
        addr = tmp[1].split(',')[0]
        depth = int(tmp[-1])
        angr_depth_dict[addr] = depth
    for it in angr_smse_list:
        print ("addr:%s, depth:%d;" % (it,angr_depth_dict[it]), end = ' ')
        distr[(angr_depth_dict[it]//5)] += 1
    print()
    print(distr)
    print()
'''


if len(sys.argv) <= 3:
    print("usage:get_diff.py smse_coverage_filepath other_coverage_filepath smse_depth_file_path")
    exit()
else: 
    smse_coverage = sys.argv[1]
    benchmark_coverage = sys.argv[2]
    smse_depth_name = sys.argv[3]

    num = int(input("How many shared library need count?"))
    so_offset=[(0,0,0)]
    for i in range(num) :
        key = int(input("The number of the shared library in smse log:"))
        st = int(input("The start address of the shared library in benchmark:"), 16)
        en = int(input("The end address of the shared library in benchmark:"), 16)
        so_offset.append((key,st,en))

        

get_block_diff(so_offset)
