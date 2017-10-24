#!/usr/bin/env python3
import subprocess, sys, re, shutil

# TODO
# Need to change for where cbmc is to be executed from
cbmc_loc = "cbmc"

def cbmc(args):
    if not shutil.which(cbmc_loc):
        raise Exception("CBMC is not found, change cbmc_loc string in cbmc.py")

    cbmc_result = [0]
    cbmc_args=[cbmc_loc, "--memory-leak-check", "--pointer-overflow-check", "--pointer-check", "--bounds-check", "--unwind", "100"]

    cbmc_args = cbmc_args + args
    p = subprocess.Popen(cbmc_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    parse = p.communicate()

    #if p.returncode:
    #    raise Exception(parse[1])

    #print("stderr:\n" + parse[1].decode("utf-8"))
    #print("stdout: \n" + parse[0].decode("utf-8"))
    cbmc_stdout = parse[0].decode("utf-8")
    cbmc_stderr = parse[1].decode("utf-8")

    output = [s.decode("utf-8").strip() for s in parse[0].splitlines()]
    for line in output:
        match = re.search("dereference\ failure\:\ deallo.+?FAILURE$", line)
        if match:
            cbmc_result[0] = 1
        #match = re.search("FAILURE$",line)
        #time_match = re.search("^\[time\.pointer",line)
        #if match and not time_match:
            #print line

    return(cbmc_result, cbmc_stdout, cbmc_stderr)

if __name__ == "__main__":
    res, out, err = cbmc(sys.argv[1:])
    print(err)
    print(out)

def cbmc_dir(args):
    if not shutil.which(cbmc_loc):
        raise Exception("CBMC is not found, change cbmc_loc string in cbmc.py")

    cbmc_result = [0]
    #make sure cbmc is linked
    cbmc_args=[cbmc_loc, "--memory-leak-check", "--pointer-overflow-check", "--pointer-check", "--bounds-check", "--unwind", "100"]

    for i in range(0,len(args)):
        temp_cbmc = list(cbmc_args)
        temp_cbmc.append(args[i])
        print("Running: " + " ".join(temp_cbmc))
        p = subprocess.Popen(temp_cbmc, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        parse = p.communicate()
        print("#####\nstderr:\n" + parse[1].decode("utf-8"))
        print("stdout: \n" + parse[0].decode("utf-8"))
        #cbmc_stdout = parse[0].decode("utf-8")
        #cbmc_stderr = parse[1].decode("utf-8")



