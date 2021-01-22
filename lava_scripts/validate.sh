#!/bin/bash

PROG="base64"
PROGOPT="-d"

for file in ./crashes/* ./hangs/* ./queue/*
do
    { /home/jordan/tests/lava_corpus/LAVA-M/${PROG}/coreutils-8.24-lava-safe/lava-install/afl/bin/${PROG} ${PROGOPT} ${file} ; } &> /dev/null
    echo $? 
done > validated.txt

