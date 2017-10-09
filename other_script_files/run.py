#!/usr/bin/env python3
import glob, re, sys
from coccinelle import cocci
from cbmc import cbmc
from stc import stc
restricted_files = ['io.c'
                    ,'main.cpp'
                    ,'main_linux.cpp'
                    ,'split.py'
                    ,'std_testcase.h'
                    ,'std_testcase_io.h'
                    ,'std_thread.c'
                    ,'std_thread.h'
                    ,'testcases.h']

src_list = glob.glob("*.c")

###
# 0 for no bug, 1 for bug exists
###
#cocci_data = []
#cbmc_data = []
#stc_data = []
data = []
target = []

g_f = False ## checking which folder we are in good or bad
b_f = False

def append_target():
    if g_f:
        target.append(0)
    if b_f:
        target.append(1)

def run(args):
    for src in src_list:

        b_bad = re.search("b_bad.c$",src)
        b_good = re.search("b_good.c$",src)

        if b_bad or b_good:
            continue

        a_bad = re.search("a_bad.c$",src)
        a_good = re.search("a_good.c$",src)

        result = []

        if a_good:
            b_str = re.sub(r"(.+?)a_good.c$", r'\1b_good.c', src)

            cocci_result = cocci([src,b_str,'io.c'])
            #cocci_data.append(cocci_result)
            for a in cocci_result:
                result.append(a)

            cbmc_result = cbmc([src,b_str,'io.c'])
            #cbmc_data.append(cbmc_result)
            for a in cbmc_result:
                result.append(a)

            stc_result = stc([src,b_str,'io.c'])
            #stc_data.append(stc_result)
            for a in stc_result:
                result.append(a)

            data.append(result)
            append_target()

        elif a_bad:
            b_str = re.sub(r"(.+?)a_bad.c$", r'\1b_bad.c', src)

            cocci_result = cocci([src,b_str,'io.c'])
            #cocci_data.append(cocci_result)
            #result.append(cocci_result)
            for a in cocci_result:
                result.append(a)

            cbmc_result = cbmc([src,b_str,'io.c'])
            #cbmc_data.append(cbmc_result)
            #result.append(cbmc_result)
            for a in cbmc_result:
                result.append(a)

            stc_result = stc([src,b_str,'io.c'])
            #stc_data.append(stc_result)
            #result.append(stc_result)
            for a in stc_result:
                result.append(a)

            data.append(result)
            append_target()

        elif src not in restricted_files:
            cocci_result = cocci(['1',src,'io.c'])
            #cocci_data.append(cocci_result)
            #result.append(cocci_result)
            for a in cocci_result:
                result.append(a)

            cbmc_result = cbmc(['1',src,'io.c'])
            #cbmc_data.append(cbmc_result)
            #result.append(cbmc_result)
            for a in cbmc_result:
                result.append(a)

            stc_result = stc(['1',src,'io.c'])
            #stc_data.append(stc_result)
            #result.append(stc_result)
            for a in stc_result:
                result.append(a)

            data.append(result)
            append_target()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "good":
            g_f = True
        if sys.argv[1] == "bad":
            b_f = True
    run(sys.argv)

    #data = list(zip(cocci_data,cbmc_data,stc_data))
    print(data)
    print(target)



# Uncomment the blocks to test the tools 1 by 1
#print("####################\nCoccinelle\n####################")
#for src in src_list:
#
#    b_bad = re.search("b_bad.c$",src)
#    b_good = re.search("b_good.c$",src)
#
#    if b_bad or b_good:
#        continue
#
#    a_bad = re.search("a_bad.c$",src)
#    a_good = re.search("a_good.c$",src)
#    bstr = ""
#
#    if a_good:
#        b_str = re.sub(r"(.+?)a_good.c$", r'\1b_good.c', src)
#        cocci_result = cocci(['1',src,b_str,'io.c'])
#        cocci_data.append(cocci_result)
#    elif a_bad:
#        b_str = re.sub(r"(.+?)a_bad.c$", r'\1b_bad.c', src)
#        cocci_result = cocci(['1',src,b_str,'io.c'])
#        cocci_data.append(cocci_result)
#    elif src not in restricted_files:
#        cocci_result = cocci(['1',src,'io.c'])
#        cocci_data.append(cocci_result)
#

#print("####################\nCBMC\n####################")
#for src in src_list:
#    b_bad = re.search("b_bad.c$",src)
#    b_good = re.search("b_good.c$",src)
#
#    if b_bad or b_good:
#        continue
#
#    a_bad = re.search("a_bad.c$",src)
#    a_good = re.search("a_good.c$",src)
#    bstr = ""
#
#    if a_good:
#        b_str = re.sub(r"(.+?)a_good.c$", r'\1b_good.c', src)
#        cbmc_result = cbmc(['1',src,b_str,'io.c'])
#        cbmc_data.append(cbmc_result)
#    elif a_bad:
#        b_str = re.sub(r"(.+?)a_bad.c$", r'\1b_bad.c', src)
#        cbmc_result = cbmc(['1',src,b_str,'io.c'])
#        cbmc_data.append(cbmc_result)
#    elif src not in restricted_files:
#        cbmc_result = cbmc(['1',src,'io.c'])
#        cbmc_data.append(cbmc_result)
#
#
#print("####################\nSTC\n####################")
#for src in src_list:
#    b_bad = re.search("b_bad.c$",src)
#    b_good = re.search("b_good.c$",src)
#
#    if b_bad or b_good:
#        continue
#
#    a_bad = re.search("a_bad.c$",src)
#    a_good = re.search("a_good.c$",src)
#    bstr = ""
#
#    if a_good:
#        b_str = re.sub(r"(.+?)a_good.c$", r'\1b_good.c', src)
#        stc_result = stc(['1',src,b_str,'io.c'])
#        stc_data.append(stc_result)
#    elif a_bad:
#        b_str = re.sub(r"(.+?)a_bad.c$", r'\1b_bad.c', src)
#        stc_result = stc(['1',src,b_str,'io.c'])
#        stc_data.append(stc_result)
#    elif src not in restricted_files:
#        stc_result = stc(['1',src,'io.c'])
#        stc_data.append(stc_result)
#


#print(cocci_data)
#print(cbmc_data)
#print(stc_data)


