#!/usr/bin/env python3
import glob, subprocess, sys, re, errno, os, shutil

from cbmc import *
from coccinelle import *
from stc import *

def run_programs(args):

    curdir = os.getcwd()

    if not os.path.isdir(args):
        raise("the directory does not exist" + args)

    #print(curdir+"#"+args)
    if args == ".":
        temp_list = glob.glob(curdir+"/**/*.c", recursive=True)
    else:
        temp_list = glob.glob(curdir+"/"+args+"/**/*.c", recursive=True)
    #print(temp_list)

    ##res, out, err = cbmc(temp_list)
    ##print(err)
    ##print(out)

    cbmc_dir(temp_list)
    #print(err)
    #print(out)

if __name__ == "__main__":

    #try:
    #    filename = re.search('(.+?)\.c$', args[1]).group(1)
    #except AttributeError:
    #    print("Filename not valid")

    run_programs(sys.argv[1])


