#!/usr/bin/env python3
import subprocess
import sys
import re
import errno
import os
import shutil

def printReport(report):
    for i in report:
        print(i)

def stc(args):
    stc_result = [1]
#currently only works with 1 C source file, will try to attempt to work with multiple files.
    filename = ''

# Need to change where clang is install on your system
    clang="/home/ysui/llvm-3.8.0/llvm-3.8.0.obj/Release+Asserts/bin/clang"
# Need to change where stc is installed on your system
    stc='/home/stc/stc/Release+Asserts/bin/stc'

# Extract filename from .c source file
    try:
        filename = re.search('(.+?)\.c$', args[1]).group(1)
    except AttributeError:
        filename = ''
        print("Filename not valid")

    if len(args) >= 2:
        # Create a directory containing the compiled and stc files
        try:
            os.makedirs(filename)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        # Compile the files to get .bc file
        clang_args = [clang, "-g", "-flto", "-o", filename+"/"+filename]
        for i in range(1,len(args)):
            clang_args.append(args[i])
        p = subprocess.Popen(clang_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        parse = p.communicate()
        if p.returncode:
            raise Exception(parse[1])
        #print("stderr:\n" + parse[1].decode("utf-8"))
        #print("stdout:\n" + parse[0].decode("utf-8"))

        # Use stc on the .bc files generated
        stc_args = [stc, "-uaf" , "-flowbg=300000", "-cxtbg=300000", "-pathbg=300000", "-stccxt=100", "-singleVFG", "-dbg=false", "-mb", filename+"/"+filename+".bc"]
        c = subprocess.Popen(stc_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        parse2 = c.communicate()
        if c.returncode:
            raise Exception(parse2[1])
        #print("stderr:\n" + parse2[1].decode("utf-8"))
        #print("stdout: \n" + parse2[0].decode("utf-8"))

        #output = [s.strip() for s in parse2[0].splitlines()]

        report = [s.strip() for s in open(filename+"/"+filename+".report")]
        #printReport(report)
        no_warning_check = re.search('^No warning issued',report[0])
        if no_warning_check:
            stc_result[0] = 0

        shutil.rmtree(filename)
        #print "Removed Directory"
    return stc_result, report

if __name__ == "__main__":
    stc(sys.argv)


