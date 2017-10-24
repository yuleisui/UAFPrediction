#!/usr/bin/env python3
import subprocess, sys, os, errno, shutil

# TODO before execution
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

    cocci_result = [-1]
    cocci_args=[cocci_loc, "--sp-file", uaf_cocci_loc]

    cocci_args = cocci_args + args
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
    else:
        cocci_result[0] = 0


    return cocci_result, stdout, stderr

if __name__ == "__main__":
    res, stdout, stderr = cocci(sys.argv[1:])
    print(stderr)
    print(stdout)

def cocci_dir(args):
    if not shutil.which(cocci_loc):
            raise Exception("Coccinelle / Spatch command not found, \
                            change cocci_loc string in coccinelle.py")
    if not os.path.exists(uaf_cocci_loc):
            raise FileNotFoundError(
                        errno.ENOENT, os.strerror(errno.ENOENT), uaf_cocci_loc )

    cocci_result = [-1]
    cocci_args=[cocci_loc, "--sp-file", uaf_cocci_loc]
#    Testing a files one by one given a list #####
    for i in range(0,len(args)):
        temp_cocci = list(cocci_args)
        temp_cocci.append(args[i])
        print(" Running: " + " ".join(temp_cocci))

        p = subprocess.Popen(temp_cocci, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        parse = p.communicate()
        #if p.returncode:
        #    raise Exception(parse[1])

        output = [s.decode("utf-8").strip() for s in parse[0].splitlines()]
        if output:
            cocci_result[0] = 1
            print("stderr:\n" + parse[1].decode("utf-8"))
            print("stdout: \n" + parse[0].decode("utf-8"))
            stdout = parse[0].decode("utf-8")
            stderr = parse[1].decode("utf-8")



