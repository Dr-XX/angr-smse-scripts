import sys
import re
import os

def get_bug_number(file_name):
    bug_num = set()
    fopen = open(file_name, 'rb')
    fileread = fopen.readlines()
    fopen.close()
    for line in fileread:
        t=re.search(b'Successfully triggered bug (\d*), crashing now!',line)
        if t:
            bug_num.add(t.group())
    print(len(bug_num))
    print(bug_num)

if __name__ == "__main__" :
    if len(sys.argv) != 2:
        print("usage: get_bug_num.py <filename>")
    else :
        file_name = sys.argv[1]
        get_bug_number(file_name)
