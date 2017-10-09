#! /usr/bin/python
#ls -1 . | egrep '^[^C]' | xargs cp -t bad/
import sys, re, errno, os, shutil, glob

src_list = glob.glob("*.c")
restricted_files = ['io.c'
                    ,'main.cpp'
                    ,'main_linux.cpp'
                    ,'split.py'
                    ,'std_testcase.h'
                    ,'std_testcase_io.h'
                    ,'std_thread.c'
                    ,'std_thread.h'
                    ,'testcases.h']
#print src_list
try:
    os.makedirs('good')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

try:
    os.makedirs('bad')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

for src in src_list:

    if src not in restricted_files:
        good = re.sub(r'(.+?)\.c$', r'\1_good.c', src)
        bad = re.sub(r'(.+?)\.c$', r'\1_bad.c', src)
        helper_flag = False
        match = re.search(".+?b.c$", src)
        if match:
            helper_flag = True
        #print src
        #print good
        #print bad

        with open(src) as f:
            lines = f.readlines()
        #print lines

        f1 = open("good/"+good, "a+")
        f2 = open("bad/"+bad, "a+")

        start = 0
        #wchar = 0
        bad_start = 0
        bad_end = 0
        good_start = 0
        good_end = 0
        seen_good = False
        seen_bad = False
        mgood_start = 0
        mgood_end = 0
        mbad_start = 0
        mbad_end = 0



        for index, s in enumerate(lines):
            #match = re.search("\#include\ \<wchar\.h\>",s)
            #if match:
            #    wchar = index

            match = re.search("\#ifndef\ OMITBAD", s)
            if match and not seen_bad:
                bad_start = index

            match = re.search("\#endif\ \/\*\ OMITBAD\ \*\/", s)
            if match and not seen_bad:
                bad_end = index
                seen_bad = True

            match = re.search("\#ifndef\ OMITGOOD",s)
            if match and not seen_good:
                good_start = index

            match = re.search("\#endif\ \/\*\ OMITGOOD\ \*\/",s)
            if match and not seen_good:
                good_end = index
                seen_good = True

            match = re.search("\#ifndef\ OMITBAD", s)
            if match:
                mbad_start = index

            match = re.search("\#endif\ \/\*\ OMITBAD\ \*\/", s)
            if match:
                mbad_end = index

            match = re.search("\#ifndef\ OMITGOOD",s)
            if match:
                mgood_start = index

            match = re.search("\#endif\ \/\*\ OMITGOOD\ \*\/",s)
            if match:
                mgood_end = index

        f1.writelines(lines[start:bad_start])
        f1.writelines(lines[good_start:good_end+1])
        f1.writelines(lines[good_end+1:mgood_end+1])
        if not helper_flag:
            f1.writelines(lines[mbad_end+1:])

        f2.writelines(lines[start:bad_end+1])
        #f2.writelines(lines[bad_start:bad_end+1])
        f2.writelines(lines[good_end+1:mgood_start])
        if not helper_flag:
            f2.writelines(lines[mbad_start:])
