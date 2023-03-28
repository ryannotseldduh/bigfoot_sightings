# My various libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Here's where my I'm pulling my data from
df = pd.read_csv('data_main/merged_data.csv').drop(columns=['count', 'observed','location_details', 'title', 'pressure', 'summary', 'uv_index', 'visibility', 'wind_bearing','wind_speed', 'temperature_mid', 'dew_point','humidity','cloud_cover','precip_intensity','precip_probability','precip_type', 'latitude', 'longitude', 'geohash'])

#Cleaning process

# This shows us our data frame minus some columns that affect how readable the information is. 

df.head(10)

df.tail(10)

df['county'].describe()

df['temperature_high'].mean()

df['temperature_low'].mean()


# This should return a pie chart that tells us the day of the week most spotters 

y = df['day_of_the_week'].value_counts(normalize=True) * 100
colors = ["#CCBFE9", "#B8E9E4", "#FEF3D8", "#FFD3CC", "#FFF8C2", "#CFF3CA" ,"#FFE5B8"]
mylabels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
myexplode = [0.1, 0, 0, 0, 0, 0, 0.1]
plt.pie(y, labels = mylabels,explode=myexplode, autopct='%1.1f%%', colors=colors)
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

#This code returns a graph that shows the top 5 states for sighitngs 
state_data= df['state'].value_counts().nlargest(5).plot.barh(color=["#E0BBE4", "#957DAD", "#D291BC", "#FEC8D8", "#FFDFD3"])
plt.xlabel('Number of Sighitngs')
plt.title('Top 5 States by Sightings')
plt.show()

#This code returns a graph that shows the bottom 5 states for sighitngs 
state_data= df['state'].value_counts().nsmallest(5).plot.barh(color=["#FBD0C3", "#BA8FDB", "#D291BC", "#F7F0CC", "#BBDBAB"])
plt.xlabel('Number of Sighitngs')
plt.xlim(3,20)
plt.title('Lowest 5 States by Sightings')
plt.show()