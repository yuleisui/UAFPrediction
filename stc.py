#!/usr/bin/env python
import subprocess
import sys
import re
import errno
import os
import shutil

filename = ''

# Need to change where clang is install on your system
clang="/home/ysui/llvm-3.8.0/llvm-3.8.0.obj/Release+Asserts/bin/clang"
# Need to change where stc is installed on your system
stc='/home/stc/stc/Release+Asserts/bin/stc'

try:
    filename = re.search('(.+?)\.c$', sys.argv[1]).group(1)
except AttributeError:
    filename = ''
    print "Filename not valid"

if len(sys.argv) == 2:
    print "Starting to compile " + filename + " " + sys.argv[1]
    try:
        os.makedirs(filename)
        print "Created directory"
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    clang_args = [clang, "-g", "-flto", "-o", filename+"/"+filename, sys.argv[1]]
    p = subprocess.Popen(clang_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    parse = p.communicate()
    print "stderr:\n" + parse[1]
    print "stdout: \n" + parse[0]

    stc_args = [stc, "-uaf" , "-flowbg=300000", "-cxtbg=300000", "-pathbg=300000", "-stccxt=100", "-singleVFG", "-dbg=false", "-mb", filename+"/"+filename+".bc"]
    c = subprocess.Popen(stc_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    parse2 = c.communicate()
    print "stderr:\n" + parse2[1]
    print "stdout: \n" + parse2[0]








    ##print " *** "
    ##shutil.rmtree(filename)
    ##print "Removed Directory"
