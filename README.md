# Bigfoot Data Project

![Getting Started](images/cool_pic.png)


## The Mission Statement

This project is an attempt to assist the cryptozoology community in their hunt for the elusive and legendary creature- Bigfoot. 
With the data provided by eyewitness accounts, I have created visualizations that these intrepid explorers and hunters can use to ascertain 
the best conditions under which to go about the search. The tools provided here will enable us to search the best possible day, season, etc., 
to locate our subject. We will also explore sighitngs over several decades to answer the question, "Have sighitng amounts varied over the years?".
It is my hope that with this scientific and graphical analysis we can finally locate this rare and evasive cryptid and finally put to bed this 
age-old question. 

## Libraries Needed
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
Use pip to install these and jupyter 

```python
#Data Project Requirements 
1.) Loaded in my csv data with pandas 
2.) Used .drop() in the context of the original CSV read to remove unwanted columns
3.) Used the .replace() function to get rid of NaN and replace with 'No info'
4.) Used nsmallest() and nlargest() to target specific values
5.) Used the .drop() funciton to clean data in second visualization, eliminating Unknown values
6.) Formated 'moon_phase' column into percentages
7.) used .mean() to analyze average high and low temperatures
```
