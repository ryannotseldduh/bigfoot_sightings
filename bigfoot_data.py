# My various libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Here's where my I'm pulling my data from
df = pd.read_csv('data_main/merged_data.csv')

# This should return a pie chart that tells us the day of the week most spotters 

y = df['day_of_the_week'].value_counts(normalize=True) * 100
colors = ["#CCBFE9", "#B8E9E4", "#FEF3D8", "#FFD3CC", "#FFF8C2", "#CFF3CA" ,"#FFE5B8"]
mylabels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
plt.pie(y, labels = mylabels,autopct='%1.1f%%', colors=colors)
#myexplode = [0.2, 0, 0, 0]
plt.title("On Which Day Are You Most Likely to\n" + "See a real-life Bigfoot?")
plt.show()  

#Summer 'Squatch graph

season_data = df['season'].value_counts().drop('Unknown').plot.bar(color=colors)
plt.ylabel("Number of Sightings")
plt.ylim(0, 4000)
plt.title("Sasquatch by Season")
plt.grid(True, color='#FCF5DB')
plt.show()

#What happened in the 2000's?

year_data = df['year'].value_counts(ascending=True, sort=True).plot.area(color='#FEC1C1', xlabel='Years', ylabel="number of sightings").set_xlim(1960,2022)
plt.title("Year of the Yeti")
plt.grid(True, color='#779CDB')
plt.show()  