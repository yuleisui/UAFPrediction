#!/usr/bin/env python
import subprocess
import sys

print "start"

if len(sys.argv) >= 2:
#make sure cbmc is linked
    cbmc_args=["cbmc", "--memory-leak-check", "--pointer-overflow-check", "--pointer-check"]
    for i in range(1,len(sys.argv)):
        cbmc_args.append(sys.argv[i])

    p = subprocess.Popen(cbmc_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    parse = p.communicate()

    print parse[0]
    print cbmc_args

    print "start of stderr -----------------------"
    print parse[1]

print "success"
