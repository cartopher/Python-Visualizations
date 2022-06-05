#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import libaries

# seaborn is the visual theme
import seaborn as sns

# matplotlib plots the data and sets the visual perferences 
import matplotlib.pyplot as plt

# set the graph font
plt.rcParams["font.family"] = "serif"

# set the graph parameters
w = 10
h = 3
d = 70

# x-axis lables (water years)
x_axis_labels = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,'10 Yr \n Average']

# y-axis labels (stations)
y_axis_labels = ['TX-CLY-1','TX-CLY-3','TX-CLY-4'] 

# plot the heat map 
plt.figure(figsize=(w, h), dpi=d)

# add the data in pivot format
data = [[9.6,29.6,22.9,25.1,45.3,47,32.3,20.3,26.7,27.6,31,28.9],
       [10.8,19,15,17.8,43.4,46.3,34.1,25.2,18.5,27.8,28.6,26.2],
       [11,22.1,8.3,10.6,41.5,45.7,35.9,30.1,10.4,28.1,26.1,24.5]]

# set the seaborn theme parameters & perferences
s = sns.heatmap(data,
                vmin=9,
                vmax=47, 
                xticklabels=x_axis_labels, 
                yticklabels=y_axis_labels, 
                annot=True, 
                cmap='RdYlGn')

# primary title & perferences
plt.title('Birdwell & Clark Ranch''\n', loc='center', fontsize=14.5, fontweight="bold")

# sub title & perferences
plt.title('                        Average Annual Precipitation (inches)', loc='left', fontsize=12, fontweight="bold")

# x-axis label placement rotation (water years)
plt.xticks(rotation = 45)

# x-axis title & perferences
plt.xlabel('Water Years - Oct. 2011 - Sept. 2021', fontsize=14.5)

# y-axis title & perferences
plt.ylabel('Monitoring Stations \n''(within 20 mile buffer zone)', fontsize=12)

# save results to C:\Users
plt.savefig("Birdwell & Clark Average Precipiation Heat Map.png")


# In[ ]:





# In[ ]:




