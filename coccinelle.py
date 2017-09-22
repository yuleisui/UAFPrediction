#!/usr/bin/env python3
import subprocess
import sys
import os

def cocci(args):
    cocci_result = [0]
    if len(args) >= 2:
        cocci_args=["spatch", "--sp-file", "/home/antheny/UAFPrediction/uaf.cocci"]
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
