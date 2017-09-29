#!/usr/bin/env python3
import subprocess, sys, os, errno, shutil

#TODO before execution
# Need to change where coccinelle is executed from
cocci_loc = "spatch"
# Need to change where the location of the uaf.cocci patch file
uaf_cocci_loc = "/home/antheny/UAFPrediction/uaf.cocci"

def cocci(args):
    if not shutil.which(cocci_loc):
        raise Exception("Coccinelle / Spatch command not found, change cocci_loc string in coccinelle.py")
    if not os.path.exists(uaf_cocci_loc):
        raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), uaf_cocci_loc )
    cocci_result = [0]
    if len(args) >= 2:
        cocci_args=[cocci_loc, "--sp-file", uaf_cocci_loc]
        if os.path.isdir(args[1]):
            cocci_args.append("-dir")
            cocci_args.append(args[1])
            p = subprocess.Popen(cocci_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            for i in range(1,len(args)):
                cocci_args.append(args[i])
                p = subprocess.Popen(cocci_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        parse = p.communicate()
        #if p.returncode:
        #    raise Exception(parse[1])
        #print("stderr:\n" + parse[1].decode("utf-8"))
        #print("stdout: \n" + parse[0].decode("utf-8"))
        stdout = parse[0].decode("utf-8")
        stderr = parse[1].decode("utf-8")

        output = [s.decode("utf-8").strip() for s in parse[0].splitlines()]
        if output:
            cocci_result[0] = 1

    return cocci_result, stdout, stderr

if __name__ == "__main__":
    cocci(sys.argv)
