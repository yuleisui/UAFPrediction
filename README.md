# UAFPrediction
UAFPrediction is a tool which uses the Support Vector Machine learning model to determine the likelihood of a use-after-free bug within C source files. 

There are numerous C static bug detectors which aim to locate the existance of use-after-free bugs, though not all tools are perfect and there are some limitations when utilising static analysis such as filtering false positives

## Video Demonstration of UAFPrediction
[![IMAGE ALT TEXT](https://www.dropbox.com/s/shqbdrbdouxnpzi/Screenshot-2017-10-12%201%20of%201%20uploaded%20-%20YouTube.png?raw=1)](https://youtu.be/pA4Sb4w1TRg "UAFPrediction")

## Installation
This tool requires 
1. python3 installed and the python modules Scikit-learn and its associated dependencies
2. CBMC tool: [http://www.cprover.org/cbmc/](http://www.cprover.org/cbmc/)
3. Coccinelle tool [http://coccinelle.lip6.fr/download.php](http://coccinelle.lip6.fr/download.php)
4. Clang 3.8 [http://releases.llvm.org/download.html](http://releases.llvm.org/download.html)
5. SVF tool [https://github.com/yuleisui/SVF](https://github.com/yuleisui/SVF) 

## Usage
### Setting up UAFPrediction
Modify coccinelle.py, cbmc.py and stc.py to show where coccinelle, cbmc and SVF is installed on your system. 
  1. If you have installed Coccinelle using a package manager, then the command to invoke will be "spatch".
   ![alt text](https://www.dropbox.com/s/eyqrrbpuqbx1f0n/coccinelle.png?raw=1 "Coccinelle Setup")
  2. If you have followed the default instructions on where stc is installed, then it may not be necessary to change the cbmc_loc string.
   ![alt text](https://www.dropbox.com/s/0nr4f8zj3yrsso5/cbmc.png?raw=1 "CBMC setup")
  3. If you have followed the default instructions on where clang is installed, then it may not be necessary to change clang_loc string.
  4. It may be required to change the stc_loc string, as the binary file may be in a different location.
   ![alt text](https://www.dropbox.com/s/kepenluprnwayvk/svf.png?raw=1 "SVF setup")
2. Invoke the UAFPrediction.py program using python3 from the base folder of where C source files are located.
    * E.g. python3 /path/to/UAFPrediction.py file1.c file2.c …
![alt text](https://www.dropbox.com/s/nz32fv6v0bsaegu/invoke.png?raw=1 "invoking UAFPrediction")
3. After execution the tool will report if a Use-After-Free bug has been predicted. If a bug has been predicted, then the output of the tools will be report. Otherwise the message “No Use-After-Free bugs have been predicted” message will appear.
[!alt text](https://www.dropbox.com/s/h1qh1nazf4024c3/uafPred.png?dl=0 "reporting bugs")

## Test folder
Under the test folder, there are some examples to showcase the program in action.
* To use the CWE416_Use_After_Free__return_freed_ptr_18_bad.c test case, it must be called with io.c.
    * e.g. python3 /path/to/UAFPrediction.py CWE416_Use_After_Free__return_freed_ptr_18_bad.c io.c
