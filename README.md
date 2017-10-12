# UAFPrediction
UAFPrediction is a tool which uses the SVM machine learning model to determine the likelihood of a use-after-free bug within  C/C++ source files. 

There are numerous C/C++ static bug detectors which aim to locate the existance of use-after-free bugs, though not all tools are perfect and there are some limitations when utilising static analysis such as filtering false positives

[![IMAGE ALT TEXT](https://www.dropbox.com/s/shqbdrbdouxnpzi/Screenshot-2017-10-12%201%20of%201%20uploaded%20-%20YouTube.png)](http://www.youtube.com/watch?v=MtAFBDPzhx4 "UAFPrediction")

## Installation
This tool requires 
1. python3 installed and the python modules Scikit-learn and its associated dependencies
2. Cbmc tool
3. Coccinelle tool
4. Stc tool 
5. Clang 3.8

## Usage
1. Modify coccinelle.py, cbmc.py and stc.py to show where coccinelle, cbmc and stc is installed on your system. 
    * If you have followed the default instructions on where coccinelle is installed, then it may not be necessary to change the cocci_loc string.
    * If you have followed the default instructions on where stc is installed, then it may not be necessary to change the cbmc_loc string.
    * If you have followed the default instructions on where clang is installed, then it may not be necessary to change clang_loc string.
    * It may be required to change the stc_loc string, as the binary file may be in a different location.
2. Invoke the UAFPrediction.py program using python3 from the base folder of where C source files are located.
    * E.g. python3 /path/to/UAFPrediction.py file1.c file2.c …
3. After execution the tool will report if a Use-After-Free bug has been predicted. If a bug has been predicted, then the output of the tools will be report. Otherwise the message “No Use-After-Free bugs have been predicted” message will appear.

## Test folder
Under the test folder, there are some examples to showcase the program in action.
* To use the CWE416_Use_After_Free__return_freed_ptr_18_bad.c test case, it must be called with io.c.
    * e.g. python3 /path/to/UAFPrediction.py CWE416_Use_After_Free__return_freed_ptr_18_bad.c io.c
