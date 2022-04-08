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
w = 15
h = 10
d = 70

# x-axis lables (water years)
x_axis_labels = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,'10 Yr Average']

# y-axis labels (stations)
y_axis_labels = ['TX-BLC-1','TX-BLC-10','TX-BLC-12','TX-BLC-16','TX-BLC-18','TX-BLC-2','TX-BLC-20','TX-BLC-21','TX-BLC-24','TX-BLC-30','TX-BLC-31','TX-BLC-36','TX-BLC-37','TX-BLC-38','TX-BLC-4','TX-BLC-40','TX-BLC-43','TX-BLC-45'] # labels for y-axis

# plot the heat map 
plt.figure(figsize=(w, h), dpi=d)

# add the data in pivot format
data = [[7.6,42.6,30.7,31.2,37.8,51.0,36.5,32.8,42.4,32.3,23.8,33.5],
        [7.4,40.0,24.1,35.0,34.3,47.3,33.6,28.5,32.2,28.9,36.1,31.6],
        [9.1,40.3,25.2,29.0,44.6,45.9,34.7,26.7,34.4,30.7,17.4,33.7],
        [7.1,40.4,25.5,10.7,34.5,45.3,33.4,26.7,34.3,30.8,19.7,28.0],
        [0.1,31.5,11.3,16.6,14.2,44.1,31.0,26.8,34.1,31.2,24.3,24.1],
        [5.0,21.2,21.1,24.2,18.3,42.9,28.6,26.9,33.9,31.6,29.0,25.7],
        [4.5,15.4,19.8,28.8,32.5,42.3,27.4,27.0,33.8,31.8,31.3,26.8],
        [4.0,18.8,1.0,21.3,40.1,46.8,19.5,28.0,34.1,35.4,30.6,25.4],
        [3.1,20.9,3.7,14.6,33.8,27.5,13.4,30.0,34.8,36.7,28.6,22.5],
        [1.1,25.2,9.3,18.3,33.4,29.1,6.7,29.5,26.7,30.6,25.0,21.3],
        [0.6,26.3,10.6,19.2,33.4,30.6,8.8,3.0,33.9,36.5,26.0,20.8],
        [3.5,30.5,16.2,22.8,33.0,36.4,17.5,13.5,15.3,7.7,21.5,19.8],
        [4.7,31.6,17.5,23.7,33.0,37.9,19.7,16.2,20.1,6.5,28.2,21.7],
        [5.8,32.7,18.9,24.6,32.9,39.3,21.8,18.8,24.9,10.5,34.9,24.1],
        [8.1,34.8,21.7,26.4,32.7,42.2,26.2,24.1,34.5,35.2,32.7,29.0],
        [8.1,35.5,21.7,26.4,34.3,42.4,27.3,24.5,33.7,0.4,28.8,25.7],
        [8.3,37.4,21.9,26.5,39.2,42.9,30.5,25.8,31.2,9.5,24.8,27.1],
        [8.4,38.0,21.9,26.6,40.8,43.1,31.6,26.2,30.4,12.5,4.0,25.8]]

# set the seaborn theme
s = sns.heatmap(data, xticklabels=x_axis_labels, yticklabels=y_axis_labels, annot=True, cmap='RdYlGn')

# primary title & perferences
plt.title('Bamberger Ranch''\n', loc='center', fontsize=30, fontweight="bold")

# sub title & perferences
plt.title('         Average Annual Precipitation (inches)', loc='left', fontsize=24, fontweight="bold")

# x-axis label placement rotation (water years)
plt.xticks(rotation = 45)

# x-axis title & perferences
plt.xlabel('Water Years - Oct. 2011 - Sept. 2021', fontsize=16)

# y-axis title & perferences
plt.ylabel('Monitoring Stations (within 10 mile buffer zone)', fontsize=16)

# save results to C:\Users
plt.savefig("Bamberger Precipitation Heat Map.png")

