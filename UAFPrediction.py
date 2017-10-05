#!/usr/bin/env python3
import sys,re, errno, os

from sklearn import svm
from juliet_test_data import data
from juliet_test_data import target

from coccinelle import cocci
from cbmc import cbmc
from stc import stc

def printArray(report):
    for i in report:
        print(i)

def run_programs(args):
    result = []

    cocci_res, cocci_out, cocci_err = cocci(args)
    for a in cocci_res:
        result.append(a)

    cbmc_res, cbmc_out, cbmc_err = cbmc(args)
    for a in cbmc_res:
        result.append(a)
    #print(cbmc_stdout)
    #print(cbmc_stderr)

    stc_res, stc_report = stc(args)
    for a in stc_res:
        result.append(a)

    svm_prediction = predict(result)
    if svm_prediction[0] == -1:
        print("did not change value")
    if svm_prediction[0] == 1:
        print("Coccinelle LOG")
        print(cocci_err)
        print(cocci_out)
        print("CBMC LOG")
        print(cbmc_err)
        print(cbmc_out)
        print("STC LOG")
        printArray(stc_report)
    else:
        print("No Use-After-Free bugs have been predicted")


def predict(result):
    clf = svm.SVC(gamma=0.001, C=100)

    X = data()
    y = target()

    clf.fit(X,y)

    #print(len(X))
    #print(len(y))

    #print(clf.predict([data_[-1]]))
    return clf.predict([result])


if __name__ == "__main__":

    #try:
    #    filename = re.search('(.+?)\.c$', args[1]).group(1)
    #except AttributeError:
    #    print("Filename not valid")

    run_programs(sys.argv)


