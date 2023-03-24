# Bigfoot Data Project

![Getting Started](images/cool_pic.png)


### The Mission Statement

This project is an attempt to assist the cryptozoology community in their hunt for the elusive and legendary creature- Bigfoot. 
With the data provided by eyewitness accounts, I have created visualizations that these intrepid explorers and hunters can use to ascertain 
the best conditions under which to go about the search. The tools provided here will enable us to search the best possible day, season, etc., 
to locate our subject. We will also explore sighitngs over several decades to answer the question, "Have sighitng amounts varied over the years?".
It is my hope that with this scientific and graphical analysis we can finally locate this rare and evasive cryptid and finally put to bed this 
age-old question. 

#### Libraries Needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#### Read in CSV code
df = pd.read_csv('data_main/merged_data.csv')

For each of my visualizations, I pulled from different columns within my CSV. This file itself was the merger of three different sets of data. This was done within excel. I went through and cleaned various 
aspects of the data, such as cells formatted to 'numbers' rather than dates. Typos, ranges of dates, 
misspellings, swapped rows etc. were all part of the cleaning process as well. 

#Data Project Requirements 
1.) Loaded in my csv data with pandas 
2.) Used the .drop() funciton to clean data in second visualization, eliminating values that don't fit.
3.)Used nsmallest() and nlargest()
4.)
5.)
6.)
7.)


# The Visuals 
![Getting Started](images/IMG_6833.tiff)
### Analysis
This pie chart shows us that you are scientifically most likely to encounter Bigfoot on a Sunday. Presently we are unsure whether to interpret 
this as a consequence of any religious affiliation that the mysterious crypitd might have, but with more studies that may be determined. Saturday
is the day you are least likely to encounter such a creature. This may be due to any number of factors, but we suspect self-care is a common practice
in the sasquatch community. 

![Getting Started](images/IMG_6206.tiff)

###  Analysis 
This bar chart attempts to show, in wonderful pastel colors, during which season Bigfoot is most likely to be spotted. It appears from our rigorous 
collection and analysis that this is most likely to occur in the Summer months. Based on this research, it is likely that Bigfoot is a "Sun's out, guns out' 
type of guy, a proper chill dude. The winter is the least likely month to spot one of these guys. The only logical possible explanation for this is that Bigfoot
sleeps through most of this time like a bear or something. 

![Getting Started](images/IMG_6501.tiff)

### Analysis 
This area graph displays the frequency of sightings over the years. We have data going back to the 19th century, but the bulk of it is from the last 70 or so years. 
This chart seems to say that sightings peaked in the mid 2000's and has fallen since then. The 60's to the 90's show a steady increase in sightings. By the 2010's Bigfoot is 
becoming more difficult to glimpse than the decade prior. The 2020's have seen a return to 90's level encounters. It is speculated that the Sars-CoV-2 pandemic early in this decade 
contributed to scarcity of sighitngs. Professional social-distancers, Sasquatch populations likely were unaffected by the global health emergency. 

![Getting Started](images/highest.png)

### Analysis

![Getting Started](images/lowest.png)

### Analysis