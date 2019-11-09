import sys
import os

result_dir = "/home/jordan/tests/jpeg-9c/O0-g-install/bin/"    
angr_dir = "angr-result/"
smse_dir = "angr-depth-expt/"
angr_depth_name = "depth_djpeg_angr_state_with_depth_inspect20191031173304"
smse_depth_name = "depth_djpeg_smse20191102114226"
#"depth_djpeg_smse_depth20191031113238"

angr_block_name = "block_coverage_djpeg_angr_state_with_depth_inspect20191031173304"
smse_block_name = "block_coverage_djpeg_smse20191102114226"
#"block_coverage_djpeg_smse_depth20191031113238"


def get_block_diff():

    f_angr_block = open(result_dir +'/'+ angr_dir + angr_block_name)
    f_smse_block = open(result_dir +'/'+ smse_dir + smse_block_name)

    angr_block_cnt = int(f_angr_block.readline().strip())
    angr_block_list = set(i for i in f_angr_block.readline()[1:-2].split('\'') if len(i) > 2)

    smse_block_cnt = int(f_smse_block.readline().strip())
    smse_block_list = set(i for i in f_smse_block.readline()[1:-2].split('\'') if len(i) > 2)

    print("angr coved block: %d, smse coved block: %d"%(angr_block_cnt, smse_block_cnt))

    #diff
    smse_angr_list = smse_block_list - angr_block_list
    angr_smse_list = angr_block_list - smse_block_list
    
    #depth distribution,from 0-100, every 5 depth
    distr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
     
    #get depth from smse-depth-log
    smse_depth = open(result_dir +'/'+ smse_dir + smse_depth_name).readlines()
    smse_depth_dict = {}

    print("smse - angr:%d" % len(smse_angr_list))
    for i in range(len(smse_depth)) :
        tmp = smse_depth[i].split(':')
        addr = tmp[1].split(',')[0]
        depth = int(tmp[-1])
        smse_depth_dict[addr] = depth
    for it in smse_angr_list:
        print ("addr:%s, depth:%d;" % (it,smse_depth_dict[it]), end = ' ')
        distr[(smse_depth_dict[it]//5)] += 1
    print()
    print(distr)
    print()
    
    #get depth from angr-depth-log
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
    print("smse - angr:%d" % len(smse_angr_list))
    print(smse_angr_list)
    print('\n')
    
    print("angr - smse:%d" % len(angr_smse_list))
    print(angr_smse_list)
    print('\n')
    '''

'''
if len(sys.argv) <= 1:
    print("usage:get_diff.py <dir_abs_path> (depth)")
    exit()
else: 
    result_dir = sys.argv[1]
    for file_name in os.listdir(result_dir +'/'+ angr_dir) :
        if "block_coverage" in file_name:
            angr_block_name = file_name
        elif file_name.startswith("depth"):
            angr_depth_name = file_name
    for file_name in os.listdir(result_dir +'/'+ smse_dir) :
        if "block_coverage" in file_name:
            smse_block_name = file_name
        elif file_name.startswith("depth"):
            smse_depth_name = file_name
'''
get_block_diff()
