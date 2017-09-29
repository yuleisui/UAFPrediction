# UAFPrediction
UAFPrediction is a tool which uses the SVM machine learning model to determine the likelihood of a use-after-free bug within  C/C++ source files. 

There are numerous C/C++ static bug detectors which aim to locate the existance of use-after-free bugs, though not all tools are perfect and there are some limitations when utilising static analysis such as filtering false positives 

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
2. Invoke the svm.py program using python3 from the base folder of where C source files are located.
    * E.g. python3 svm.py file1.c file2.c …
3. After execution the tool will report if a Use-After-Free bug has been predicted. If a bug has been predicted, then the output of the tools will be report. Otherwise the message “No Use-After-Free bugs have been predicted” message will appear.


