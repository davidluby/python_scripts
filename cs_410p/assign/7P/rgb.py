# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:10:54 2022

@author: David Luby

# CS 410P - Program assignemtnt 7P


"""
import numpy as np
import matplotlib.pyplot as plt

red = np.array([220,255,165,65,180,238,57,192,255])
green = np.array([20,219,42,224,105,130,255,192,255])
blue = np.array([60,88,42,208,180,238,20,192,255])
names = ['crimson','mustard','brown','turquoise','pink','violet','neon',
         'silver','white']


bars = plt.figure(2)
ax = bars.add_subplot(111)

n = len(red)
ind = np.arange(n)
width = .175


ax.set_xlim(-width,n+width)
ax.set_ylim(0,300 )
ax.set_ylabel('RGB Values')
ax.set_xticks(ind+2*width)
i = -1
ticks = []
while i < n-1:
    i +=1
    ticks.append(names[i]+'\n'+str(red[i])+','+str(green[i])+','+str(blue[i]))
xTicks = ax.set_xticklabels(ticks)
plt.setp(xTicks,rotation = 45,fontsize = 7)

rBars = ax.bar(ind,red,width,color="red")
gBars = ax.bar(ind+width,green,width,color="green")
bBars = ax.bar(ind+2*width,blue,width,color="blue")

ax.legend((rBars[0],gBars[0],bBars[0]),('Red','Green','Blue'),loc = 
          'upper left',fontsize = 'xx-small') 

plt.show()


