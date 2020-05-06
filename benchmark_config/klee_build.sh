#!/bin/sh

cmake -DENABLE_SOLVER_Z3=ON -DENABLE_POSIX_RUNTIME=ON -DENABLE_KLEE_UCLIBC=ON  -DKLEE_UCLIBC_PATH=/home/jordan/tools/klee-uclibc -DCMAKE_INSTALL_PREFIX=/home/jordan/tools/klee/install-smse -DCMAKE_BUILD_TYPE=Debug ..
