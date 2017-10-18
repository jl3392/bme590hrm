[![Build Status](https://travis-ci.org/jl3392/bme590hrm.png?branch=master_hw2)](https://travis-ci.org/jl3392/bme590hrm)

Class Based Heart Rate Monitor
======================
This project is the seond release of the heart rate monitoring software, outputting the following parameters:
- instantaneous heart rate
- average heart rate over a specified time
- indication of brady/tachycardia occurrances in the ECG signal

All modules that were part of the module based previous release have been refactored to be methods of a broad Ecg class. 

Running method
===============
The main file to run is called "hw2_main.py", which has the capability to run over multiple files found in a test folder and returns .txt files with the output parameters. 
The inputs required to initialize the class are: 
- input csv_file
- how often the instanteous heart rate will be updated in seconds 
- thresholds for tachycardia and bradycardia 
- time in minutes over which heart rate must be averaged

The main script calls all the methods needed to process the data contained in the csv file. The output .txt files will be saved by default into the working directory out of the which the main file is run. 

License
==============
We are using an Apache License, Version 2.0 for our project. This license grants patent rights
from contributors to users.

Documentation
==============
We are currently working on updating our documentation for the class based approach. Auto-generated Sphinx documentation for our previous release can be found through the link below:
http://bme590hrm.readthedocs.io/en/latest/

Contributors
============
Jing-Rui Li (jl714@duke.edu)
Inje Lee (inje.lee@duke.edu)
Niranjana Shashikumar (niranjana.shashikumar@duke.edu)

