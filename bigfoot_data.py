# My various libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Here's where my I'm pulling my data from

df = pd.read_csv('data_main/merged_data.csv')

# This should return a pie chart 

y = df['day_of_the_week'].value_counts(normalize=True) * 100
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#800000" ,"#FFFF00"]
mylabels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
plt.pie(y, labels = mylabels,autopct='%1.1f%%')
#myexplode = [0.2, 0, 0, 0]
plt.title("On Which Day Are You Most Likely to\n" + "See a real-life Bigfoot?")
plt.show()  

#This should return a bar graph

season_data = df['season'].value_counts().drop('Unknown').plot(kind='bar')
colors2 = ["#2ca02c", "#ff7f0e", "#39FC00", "#1f77b4"]
plt.ylabel("Number of Sightings")
plt.ylim(0, 4000)
plt.title("Sasquatch by Season")
plt.show()

#this chart is going to show how sightings have varied over the years 

year_data = df['year'].value_counts()
plt.ylim(0,200)
plt.xlim(1900,2022)
plt.ylabel("year")
plt.ylabel("number of sightings")
plt.title("Year of the Yeti")
plt.grid(True)
plt.show()