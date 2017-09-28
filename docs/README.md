[![Build Status](https://travis-ci.org/jl3392/bme590hrm.png?branch=master)](https://travis-ci.org/jl3392/bme590hrm)

Heart Rate Monitor
======================
This project works on designing the software of a heart rate monitor, aiming to estimate three main parts of the heart ECG signal:
- Estimate the instantaneous heart rate
- Estimate average heart rate over a user-specified time
- Indicate whether there is a brady/tachycardia condition occurred in the ECG signal

Running method
===============
The main file to run is called "hrm1.py", the input is "ecg_data.csv" and the output is "hr_Information.txt ", which is 
a txt file providing the estimation results of the ECG signal. 

During the running process, it will ask user's input of "user-specified time". It will be used to average the heart rate under 
the specified time range. 
Please be sure to convert the time input into minutes.
For example:
If user wants to put in time as 300 seconds, please convert it to 5 minutes.

License
==============
We choose to use Apache License, Version 2.0 for our project's license. Because this license provides an express grant of patent rights
from contributors to users.

Documentation
==============
The latest documentation is automatically generated using Sphinx and can be found through the link below:
http://bme590hrm.readthedocs.io/en/latest/


Contributors
============
Jing-Rui Li (jl714@duke.edu)
Inje Lee (inje.lee@duke.edu)
Niranjana Shashikumar (niranjana.shashikumar@duke.edu)

