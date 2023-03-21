# My various libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Having issues with path right now, can't seem to change path in settings from 'Users/rjhud' this is a work around I guess. 

# os.chdir('/Users/rjhud/Pluralsight/Projects/bigfoot_sightings/data_main')

# I'm using this as a test file kinda thing

df = pd.read_csv('data_main/best_data.csv')
#df = df[0:5]
#df. drop(['observed','location_details'],axis=1,inplace=True)
#print(df)

# This should return a pie chart 

y = df['day_of_the_week'].value_counts(normalize=True) * 100
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800000" ,"#FFFF00"]
mylabels = ['Sunday,', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
plt.pie(y, labels = mylabels,autopct='%1.1f%%')
myexplode = [0.2, 0, 0, 0]
plt.title("On Which Day Are You Most Likely to\n" + "See a real-life Bigfoot?")
plt.show()  







# plt.pie(, explode=explode, labels=labels colors=colors, shadow=True, startangle=140)
# labels = ['Sunday,', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']