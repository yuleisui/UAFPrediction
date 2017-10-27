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
#### Modifying coccinelle.py
  1. On line 6, modify `cocci_loc` to where Coccinelle is invoked on your system. If you have install Coccinelle using a package manager, the default invocation is `spatch`.
  2. On line 7, modify `uaf_cocci_loc` to where the uaf.cocci file is located on your system. The uaf.cocci file is apart of the git repository. 
   ![alt text](https://www.dropbox.com/s/eyqrrbpuqbx1f0n/coccinelle.png?raw=1 "Coccinelle Setup")
#### Modifying cbmc.py
  2. On line 6, modify `cbmc_loc` to where CBMC is invoked on your system. If you have installed CBMC using a package manager, the default invocation is `cbmc`.
   ![alt text](https://www.dropbox.com/s/0nr4f8zj3yrsso5/cbmc.png?raw=1 "CBMC setup")
#### Modifying svf.py
  3. On line 7, modify `clang_loc` to where the LLVM Clang 3.8 compiler is invoked on your system.
  4. On line 9, modify `stc_loc` to where the SVF binary is located on your system.
   ![alt text](https://www.dropbox.com/s/kepenluprnwayvk/svf.png?raw=1 "SVF setup")
### Using UAFPrediction.py
2. Invoke the UAFPrediction.py program using python3 from the base folder of where C source files are located.
    * E.g. python3 /path/to/UAFPrediction.py file1.c file2.c …
![alt text](https://www.dropbox.com/s/nz32fv6v0bsaegu/invoke.png?raw=1 "invoking UAFPrediction")
3. After execution the tool will report if a Use-After-Free bug has been predicted. If a bug has been predicted, then the output of the tools will be report. Otherwise the message “No Use-After-Free bugs have been predicted” message will appear.
![alt text](https://www.dropbox.com/s/h1qh1nazf4024c3/uafPred.png?dl=0 "reporting bugs")

## Test folder
Under the test folder, there are some examples to showcase the program in action.
* To use the CWE416_Use_After_Free__return_freed_ptr_18_bad.c test case, it must be called with io.c.
    * e.g. python3 /path/to/UAFPrediction.py CWE416_Use_After_Free__return_freed_ptr_18_bad.c io.c
