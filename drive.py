import logging
import time
import sys
import os
import angr
import traceback
import psutil
from angr import options, procedures
from angr.state_plugins.runtime_state import RuntimeStatePlugin
from angr.exploration_techniques import RuntimeStateMonitor,MemoryWatcher

class HookLog(angr.SimProcedure):

    def run(self, avcl, level, fmt):
        return

class HookReturnTrue(angr.SimProcedure):

    def run(self):
        return 1


project_name = "djpeg_smse"
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

target_file = "/home/jordan/tests/jpeg-9c/O0-g-install/bin/djpeg"



if __name__ == "__main__":
    load_options = {
        'auto_load_libs': True,
        'except_missing_libs': True,
        'ld_path': [
            "/home/jordan/tests/jpeg-9c/O0-g-install/lib",
            "/lib/x86_64-linux-gnu",
            "/lib64"
        ]
    }

    p = angr.Project(target_file, load_options=load_options)
    pre_hooks = {
        'term_init': HookReturnTrue(),
        'signal': HookReturnTrue(),
        'av_log': HookLog(),
        'parse_loglevel': HookReturnTrue(),
        'fcntl': HookReturnTrue(),
    }
    for func, hook in pre_hooks.items():
        symbol = p.loader.find_symbol(func)
        if symbol is None:
            continue
        p.hook(symbol.rebased_addr, hook, replace=True)

    s = p.factory.entry_state(concrete_fs=True,
			      cwd=os.getcwd(),
                              args=[
                                  target_file,
				  '/home/jordan/tests/resource/testimg.jpg',
                              ],)
    RuntimeStatePlugin.prepare_runtime_state_tracking(s, switch_offset=0)

    simgr = p.factory.simgr(s)
    rt_monitor = RuntimeStateMonitor(min_memory=4096)
    simgr.use_technique(rt_monitor)
    
    # simgr.run()

    try:
        simgr.run()
            
    # except (KeyboardInterrupt, RecursionError):
    #     pass
    except Exception as e:
        print("unexcepted exception")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=20, file=open('traceback_' + project_name, 'a+'))
        logger.warning("unexpected exception")
        logger.exception(sys.exc_info())
        print(e)
    finally:
        # p.kb.runtime_states.dump_addr_annotation(open('addr_annotation_' + project_name, 'a+'))
        for bbl_addr, bbl_depth in rt_monitor.block_depth.items():
            print("block:0x%x, depth:%d" % (bbl_addr, bbl_depth), file=open('depth_' + project_name, 'a+'))
        print(len(rt_monitor.covered_blocks), file=open('block_coverage_' + project_name, 'a+'))
        list_covered_blocks = list(rt_monitor.covered_blocks)
        hex_unsorted_blocks = [hex(x) for x in list_covered_blocks]
        print(hex_unsorted_blocks, file=open('block_coverage_' + project_name, 'a+'))
        print(psutil.Process(os.getpid()).memory_info().vms)
        logger.warning("memory used: %d" % (psutil.Process(os.getpid()).memory_info().vms/1024/1024))
        logger.warning("%s" % simgr)
        # import IPython; IPython.embed()
        print (p.kb.runtime_states.reached_runtime_states.__repr__(), file=open('dbg_repr_' + project_name, 'a+'))
        if len(simgr.errored) >0 :
            for s in simgr.errored:
                print(s.error, file=open('errored_' + project_name, 'a+'))
                print(s.state, file=open('errored_' + project_name, 'a+'))
                traceback.print_exception(0,0,s.traceback,limit=20,file=open('errored_' + project_name, 'a+'))
