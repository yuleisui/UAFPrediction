#!/usr/bin/env python3
import glob, subprocess, sys, re, errno, os, shutil

#TODO before executing program
# Need to change where clang is install on your system
#clang_loc = "clang" # If clang can be invoked from the terminal
clang_loc="/home/ysui/llvm-3.8.0/llvm-3.8.0.obj/Release+Asserts/bin/clang"
# Need to change where stc is installed on your system
stc_loc='/home/stc/stc/Release+Asserts/bin/stc'


def printReport(report):
    for i in report:
        print(i)

def findBC(args):
    try:
        path_arg = args
        if not os.path.isdir(path_arg):
            raise ValueError("the path is not valid: "+path_arg)
    except OSError as e:
        exit(e)
    except ValueError as e:
        exit(e)

    #print(path_arg)
    temp_list = glob.glob(path_arg+"/**/*.bc", recursive=True)
    #print(temp_list)

    bc_list = []

    for item in temp_list:
        # dont match filenames with opt or out in the file extension
        optbc = re.search('\/.+\.(opt|out)\.bc$', item)
        if not optbc:
            bc_list.append(item)
    return bc_list


def c_compile(args, filename):
    # Compile the files to get .bc file
    clang_args = [clang_loc, "-g", "-flto", "-o", filename+"/"+filename]
    for i in range(0,len(args)):
        clang_args.append(args[i])
    p = subprocess.Popen(clang_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    parse = p.communicate()
    if p.returncode:
        raise Exception(parse[1])
    #print("stderr:\n" + parse[1].decode("utf-8"))
    #print("stdout:\n" + parse[0].decode("utf-8"))

def run_stc(cur_dir, stc_result):
    bcFiles_list = findBC(cur_dir)

    for i in bcFiles_list:
        # Use stc on the .bc files generated
        stc_args = [stc_loc, "-uaf" , "-flowbg=300000", "-cxtbg=300000", "-pathbg=300000", "-stccxt=100", "-singleVFG", "-dbg=false", "-mb", i]
        c = subprocess.Popen(stc_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        parse2 = c.communicate()
        if c.returncode:
            raise Exception(parse2[1])
        #print("stderr:\n" + parse2[1].decode("utf-8"))
        #print("stdout: \n" + parse2[0].decode("utf-8"))

        #output = [s.strip() for s in parse2[0].splitlines()]

        # Extract filename from .bc source file to find report file
        try:
            filename = re.search('(.+?)\.bc$', i).group(1)
            print(filename)
        except AttributeError:
            filename = ''
            print("Filename not valid")

        report = [s.strip() for s in open(filename+".report")]
        #printReport(report)
        no_warning_check = re.search('^No warning issued',report[0])

        if no_warning_check:
            stc_result[0] = 0
        else:
            stc_result[0] = 1

    return(report)




def stc(args):
    stc_result = [-1]

    if len(args) >= 2:
        filename = ''

        # Extract filename from .c source file
        try:
            filename = re.search('(.+?)\.c$', args[1]).group(1)
        except AttributeError:
            filename = ''
            print("Filename not valid")

        # Create a directory containing the compiled and stc files
        try:
            cur_dir = os.getcwd()
            os.makedirs(cur_dir+"/"+filename)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        if not shutil.which(clang_loc):
            shutil.rmtree(cur_dir+"/"+filename)
            raise Exception("Clang does not exist, change clang string in stc.py")
        c_compile(args, filename)

        if not shutil.which(stc_loc):
            shutil.rmtree(cur_dir+"/"+filename)
            raise Exception("STC does not exist, change stc string in stc.py")
        report = run_stc(cur_dir+"/"+filename,stc_result)

        shutil.rmtree(cur_dir+"/"+filename)
    return stc_result, report

if __name__ == "__main__":
    stc_res, rep = stc(sys.argv)
    printReport(rep)


