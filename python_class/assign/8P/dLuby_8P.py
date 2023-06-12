# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:52:24 2022

@author: David Luby

# CS 410P - Program assignment 8P


# create program to plot vertical vs horizontal displacement for projectile
    # for vInitial of 30 then 50
    # for angles of 25-60 (25-55)
    # then two bar plots with horizontal vs angle and vertical vs angle
        # for both velocities
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# initializing given variables
theta = np.arange(25,60,5)
thetaR = theta*np.pi/180
velocity = np.array([30,50])
time = []

# determining time intervals
i = -1
while i < 1:
    i +=1
    j = -1
    t = []
    while j < len(thetaR)-1:
        j +=1
        t.append(2*velocity[i]*math.sin(thetaR[j])/9.8)
    time.append(t)

def timeArr(t,i):
    t = []
    j = -1
    while j < len(time[i])-1:
        j +=1
        t.append(np.linspace(0,time[i][j],50))
    return(t)
 
t30 = timeArr(t[0],0)
t50 = timeArr(t[1],1)

# kinematic function
def kinemats(t,theta,velocity,j):
    xFin = []
    yFin = []
    i = -1
    while i < len(thetaR)-1:
        i +=1
        k = -1
        x = []
        y = []
        while k < len(t[0][:])-1:
            k +=1
            x.append(velocity[j]*(t[i][k])*math.cos(theta[i]))
            y.append(velocity[j]*(t[i][k])*math.sin(theta[i]) -.5*9.8*(t[i][k])**2)
        xFin.append(x)
        yFin.append(y)
        
    return(xFin,yFin)

x30,y30 = kinemats(t30,thetaR,velocity,0)
x50,y50 = kinemats(t50,thetaR,velocity,1)

# maximum function
def maxV(x,y):
    xM = []
    yM = []
    i=-1
    while i < len(x)-1:
        i +=1
        xM.append(max(x[i]))
        yM.append(max(y[i]))
    return(xM,yM)

xM,yM = maxV(x30,y30)
xM50, yM50 = maxV(x50,y50)
        
# projectile plots

i = -1
fig = plt.figure(figsize=(20,10))
fig.subplots_adjust(hspace=.3, wspace=.3)

ax = fig.add_subplot(2,2,1)
i = 0
leg = []
while i < len(x30):
    plt.plot(x30[i],y30[i])
    leg.append(str(theta[i]))
    i +=1
ax.set_title('Projectile Motion at V = 30')
ax.set_ylabel('Vertical Displacement')
ax.set_xlabel('Horizontal Displacement')
ax.legend(leg,loc='upper left',fontsize='small')

ax = fig.add_subplot(2,2,2)
i = 0
while i < len(x30):
    plt.plot(x50[i],y50[i])
    i +=1
ax.set_title('Projectile Motion at V = 50')
ax.set_ylabel('Vertical Displacement')
ax.set_xlabel('Horizontal Displacement')
ax.legend(leg,loc='upper left',fontsize='small')

# bar graphs
ax = fig.add_subplot(2,2,3)
n = len(xM)
ind = np.arange(n)
width = .175


ax.set_xlim(-width,n+width)
ax.set_ylim(0,275 )
ax.set_ylabel('X - Distance')
ax.set_xticks(ind+2*width)
i = -1
ticks = []
while i < n-1:
    i +=1
    ticks.append('Angle : '+str(theta[i]))
xTicks = ax.set_xticklabels(ticks)
plt.setp(xTicks,rotation = 45,fontsize = 7)

bBars = ax.bar(ind,xM,width,color="black")
rBars = ax.bar(ind+width,xM50,width,color="red")
ax.set_title('X - Distance for Varied Angles')
ax.legend((bBars[0],rBars[0]),('V = 30','V = 50'),loc ='upper left',
          fontsize = 'small') 

# bar 2
ax = fig.add_subplot(2,2,4)
n = len(xM)
ind = np.arange(n)
width = .175


ax.set_xlim(-width,n+width)
ax.set_ylim(0,90 )
ax.set_ylabel('Y - Distance')
ax.set_xticks(ind+2*width)
i = -1
ticks = []
while i < n-1:
    i +=1
    ticks.append('Angle : '+str(theta[i]))
xTicks = ax.set_xticklabels(ticks)
plt.setp(xTicks,rotation = 45,fontsize = 7)

bBars = ax.bar(ind,yM,width,color="black")
rBars = ax.bar(ind+width,yM50,width,color="red")
ax.set_title('Y - Distance for Varied Angles')
ax.legend((bBars[0],rBars[0]),('V = 30','V = 50'),loc ='upper left',
          fontsize = 'small') 









