# My various libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This should return a pie chart 

df = pd.read_csv('data_main/merged_data.csv')
y = df['day_of_the_week'].value_counts(normalize=True) * 100
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800000" ,"#FFFF00"]
mylabels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
plt.pie(y, labels = mylabels,autopct='%1.1f%%')
myexplode = [0.2, 0, 0, 0]
plt.title("On Which Day Are You Most Likely to\n" + "See a real-life Bigfoot?")
plt.show()  

#This should return a histogram
#df = pd.read_csv('data_main/merged_data.csv')
season_data = df['season'].value_counts().plot(kind='bar')
plt.hist(colors2 = ['#F6FF43', '#FB8908', '#39FC00', '#0089FC'])
label = 'Unknown'
#df.drop(label='Unknown', inplace=True)
plt.title("Sasquatch by Season")
plt.ylabel("Number of Sightings")
plt.ylim(0, 4000)   
plt.show()







