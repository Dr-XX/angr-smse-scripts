import logging
import time
import sys
import os
import angr
from angr.state_plugins.runtime_state import RuntimeStatePlugin
from angr.exploration_techniques import RuntimeStateMonitor

project_name = "djpeg_angr_state_with_depth"
sys.setrecursionlimit(100000)

file_handler = logging.FileHandler(
    '%s_%s.log' % (project_name, time.strftime('%Y%m%d%H%M%S')))
formatter = logging.Formatter(
    '%(levelname)s | %(asctime)s | %(name)s | %(message)s')
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

project_name = project_name + time.strftime('%Y%m%d%H%M%S')
target_file = "/home/jordan/tests/jpeg-9c/install/bin/djpeg"


if __name__ == "__main__":
    load_options = {
        'auto_load_libs': True,
        'except_missing_libs': True,
        'ld_path': [
	    "/home/jordan/tests/jpeg-9c/install/lib/",
            "/lib/x86_64-linux-gnu/",
            "/lib64"
        ]
    }

    p = angr.Project(target_file, load_options=load_options)

    s = p.factory.entry_state(concrete_fs=True,
			      cwd=os.getcwd(),
                              args=[
                                  target_file,
				  '/home/jordan/tests/resource/testimg.jpg',
                              ],)
    RuntimeStatePlugin.prepare_runtime_state_tracking(s, switch_offset=0)

    simgr = p.factory.simgr(s)
    # simgr.use_technique(RuntimeStateMonitor())
    memory_watcher = angr.exploration_techniques.MemoryWatcher(min_memory=5000)
    simgr.use_technique(memory_watcher)
    
    # simgr.run()

    covered_blocks = set()
    block_depth = dict()
    try:
        while len(simgr.active) > 0:
            simgr.step()
            for s in simgr.active:
                for bbl in s.history.bbl_addrs:
                    if bbl in block_depth:
                        block_depth[bbl] = min(block_depth[bbl], s.runtime_state.runtime_state_depth) 
                    else :
                        block_depth[bbl] = s.runtime_state.runtime_state_depth
                covered_blocks = covered_blocks.union(set(s.history.bbl_addrs))
                
            for s in simgr.deadended:
                for bbl in s.history.bbl_addrs:
                    if bbl in block_depth:
                        block_depth[bbl] = min(block_depth[bbl], s.runtime_state.runtime_state_depth) 
                    else :
                        block_depth[bbl] = s.runtime_state.runtime_state_depth
                covered_blocks = covered_blocks.union(set(s.history.bbl_addrs))
            
    # except (KeyboardInterrupt, RecursionError):
    #     pass
    except Exception as e:
        print("unexpected exception")
        # import IPython; IPython.embed()
        print(e)
    finally:
        # p.kb.runtime_states.dbg_repr(open('runtime_states_' + project_name, 'a+'))
        # p.kb.runtime_states.dump_addr_annotation(open('addr_annotation_' + project_name, 'a+'))
        for s in simgr.lowmem:
                for bbl in s.history.bbl_addrs:
                    if bbl in block_depth:
                        block_depth[bbl] = min(block_depth[bbl], s.runtime_state.runtime_state_depth) 
                    else :
                        block_depth[bbl] = s.runtime_state.runtime_state_depth
                covered_blocks = covered_blocks.union(set(s.history.bbl_addrs))
        print(len(covered_blocks), file=open('block_coverage_' + project_name, 'a+'))
        list_covered_blocks = list(covered_blocks)
        hex_unsorted_blocks = [hex(x) for x in list_covered_blocks]
        print(hex_unsorted_blocks, file=open('block_coverage_' + project_name, 'a+'))
        list_covered_blocks.sort()
        hex_covered_blocks = [hex(x) for x in list_covered_blocks]
        print("sorted:", file=open('block_coverage_' + project_name, 'a+'))
        print(hex_covered_blocks, file=open('block_coverage_' + project_name, 'a+'))
        # print block depth
        for bbl, depth in block_depth.items():
            print("block:0x%x, depth:%d" % (bbl, depth), file=open('depth_' + project_name, 'a+'))
        # import IPython; IPython.embed()
