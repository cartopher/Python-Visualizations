#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libaries

# seaborn is the visual theme
import seaborn as sns

# matplotlib plots the data and sets the visual perferences 
import matplotlib.pyplot as plt

# graph color perferences
from matplotlib.colors import ListedColormap

# set the graph font
plt.rcParams["font.family"] = "Verdana"

# set the graph parameters
w = 30
h = 40
d = 100

# x-axis lables (test years)
x_axis_labels = ['2017','2019','2021']

# y-axis labels (analytes)
y_axis_labels = ['Soil pH',
                 'Soil Organic Matter',
                 'Soil Respiration',
                 'Water Extractable Organic Carbon',
                 'Water Extractable Organic Nitrogen',
                 'Organic C to Organic N Ratio',
                 'Organic N to Inorganic N Ratio',
                 'Organic Nitrogen Release',
                 'Organic Nitrogen Reserve',
                 'Organic Phosphorus',
                 'Organic Phosphorus Release',
                 'Organic Phosphorus Reserve',
                 'Soil Health Score',
                 'Total Living Biomass',
                 'Fung: Bacteria',
                 'Protozoa Bacterial',
                 'Microaggregate',
                 'Macroaggregates',
                 'β-glucosidase enzyme - carbon enzyme',
                 'Permanganate Oxidizable Carbon - labile carbon',
                 'Water Holding Capacity, inch H2O inch soil¯¹']

# plot the heat map 
plt.figure(figsize=(w, h), dpi=d)

# add the data in pivot format
data =  [[7.9,8.2,8.3],
        [4.3,4.1,3.1],
        [0,26,0],
        [0,0,0],
        [0,16.7,6.39],
        [0,18.7,14],
        [0,1.2,1.81],
        [0,5.6,5.54],
        [0,11.2,0.9],
        [0,1.7,0.5],
        [0,0.4,0.4],
        [0,1.2,0.2],
        [0,10.54,4.4],
        [2000.01,3319.47,2126.31],
        [0.1511,0.418,0.2151],
        [1,1,2],
        [0,0,16.7],
        [0,0,31.6],
        [0,0,36.4],
        [0,0,0],
        [0,0.21,0.19]]

# set the seaborn theme
s = sns.heatmap(data, 
                vmin=None, 
                vmax=None, 
                cbar=False,
                xticklabels=x_axis_labels, 
                yticklabels=y_axis_labels, 
                annot=True,
                fmt="g", #changed for keeping the values you require to be exact as dataset
                cmap=ListedColormap(['ivory']),
                linewidth=6,
                linecolor='gainsboro',
                square=False, 
                center=0, 
                annot_kws={"size":45, "color":'black'})

# manipulate the graph 
# adding for masking the values 0
for text in s.texts:
    if text.get_text() == '0':
        #text.set_weight('')
        text.set_size(40)
    # -------- Added -----------#
    if text.get_text() == '1':
        text.set_text('ALL PREY')
    if text.get_text() == '2':
        text.set_text('all Bact')
    if text.get_text() == '0':
        text.set_text('n/a')
    # -------- ------ -----------#
    
# primary title
plt.title('Bamberger Ranch''\n', loc='center', fontsize=80, fontweight="bold")

# sub title
plt.title('    Transect Soil Results: Wildlife Preserve', loc='left', fontsize=65, fontweight="bold")

# tick mark parameters (x and y-axis)
plt.tick_params(which='major', length=25, width=2, direction='out')

# x-axis format perferences
plt.xticks(rotation = 0, fontsize=65) 

# x-axis title & perferences
plt.xlabel('\n''Test Years', fontsize=75, fontweight="bold")

# y-axis format perferences
plt.yticks(fontsize=45, style='italic')

# x-axis title & perferences
plt.ylabel('Analytes', rotation = 0, fontsize=75, fontweight="bold")

# graph color and boarder perferences
s.axhline(y = 0, color = 'darkblue', linewidth = 15) # top
s.axhline(y = 21, color = 'darkblue',linewidth = 15) # bottom
s.axvline(x = 3, color = 'darkblue',linewidth = 15)
s.axvline(x = 0, color = 'darkblue',linewidth = 15)

# show plot
plt.show()

# save results to C:\Users
plt.savefig("Bamberger Soil Results - Wildlife Preserve.png")

# https://seaborn.pydata.org/generated/seaborn.heatmap.html
# https://matplotlib.org/stable/gallery/color/named_colors.html


# In[ ]:





# In[ ]:




