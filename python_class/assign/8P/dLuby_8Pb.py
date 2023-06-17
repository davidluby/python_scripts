# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:26:39 2022

@author: David Luby

# bouncing ball program
    # create program to model bounding ball with:
        # perfect reflection
        # 90%
        % 70%
            # individual plots for 100% and 90%
            # all three plotted on the same for third plot
                # adhere to modularity requirements
"""
import math
import numpy as np
import matplotlib.pyplot as plt


# algorithm
def euler(t,x,v,g,ref,i):
    delT = t[i]-t[i-1]
    vStep = v[i-1] - g*delT
    xStep = x[i-1] + v[-1]*delT
    if xStep < 0:
        vStep = abs(ref*v[i-1])
        xStep = xStep = x[i-1] + v[-1]*delT
        x.append(xStep)
        v.append(vStep)
    else:
        x.append(xStep)
        v.append(vStep)
    return(x,v)


# first figure
g = 9.8
x = [1]
v = [0]
t = np.linspace(0,3,500)
ref = 1
i = 1
plt.figure(1)
while i < len(t)-2:
    x,v = euler(t,x,v,g,ref,i) # call
    i +=1
plt.plot(t[0:498],x)
plt.title('Perfect Reflection')
plt.legend(['1.0'])
plt.ylabel('Position (m)')
plt.xlabel('time (s)')

# second figure
x = [1]
v = [0]
ref = .9
i = 1
plt.figure(2)
while i < len(t)-2:
    x,v = euler(t,x,v,g,ref,i) # call
    i +=1
plt.plot(t[0:498],x)
plt.title('90% Reflection')
plt.legend(['0.9'])
plt.ylabel('Position (m)')
plt.xlabel('time (s)')

# third figure
g = 9.8
x = [1]
v = [0]
t = np.linspace(0,3,500)
ref = 1
i = 1
plt.figure(3)
plt.title('All Reflections')
plt.ylabel('Position (m)')
plt.xlabel('time (s)')
while i < len(t)-2:
    x,v = euler(t,x,v,g,ref,i) # first call
    i +=1

x1 = [1]
v1 = [0]
ref = .9
i = 1
while i < len(t)-2:
    x1,v1 = euler(t,x1,v1,g,ref,i) # second call
    i +=1

x2 = [1]
v2 = [0]
ref = .7
i = 1
while i < len(t)-2:
    x2,v2 = euler(t,x2,v2,g,ref,i) # third call
    i +=1
plt.plot(t[0:498],x,t[0:498],x1,t[0:498],x2)
plt.legend(['1.0','0.9','0.7'],loc='lower left')

plt.show()