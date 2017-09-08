#!/usr/bin/env python
import subprocess
import sys
import os

if len(sys.argv) >= 2:

    cocci_args=["spatch", "--sp-file", "uaf.cocci"]
    if os.path.isdir(sys.argv[1]):
        print "Using directory"
        cocci_args.append("-dir")
        cocci_args.append(sys.argv[1])
        p = subprocess.Popen(cocci_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        for i in range(1,len(sys.argv)):
            cocci_args.append(sys.argv[i])
            p = subprocess.Popen(cocci_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    parse = p.communicate()
    print "stderr: "
    print parse[1]
    print "stdout: "
    print parse[0]

#print "start of stderr -----------------------"
#print parse[1]
