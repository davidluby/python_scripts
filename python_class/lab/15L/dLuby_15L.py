# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:29:20 2022

@author: David Luby

# CS 410P - Lab assignment 15L

# not much to comment here again--more of a tutorial lab

"""

import numpy as np

# number 1
a = np.random.randint(1,11,size=(5,5))
b = np.random.randint(1,11,size=(5,5))

print(a)
print()
print(b)
print()
trufal = a==b
print(trufal) # not sure if you just want the boolean or if you want me to do
              # something if there are no falses

# number 2
c = np.random.randint(1,11,50)
mean = sum(c)/len(c)
print()
print("Mean = ",mean)

# number 3
d = np.random.randint(1,101,100)
print()
print(d)
d.sort()
d[len(d)-1] = 0
print(d)

# number 4
x = np.random.rand(50)
y = np.random.rand(50)

sX = sum(x)
sY = sum(y)
sXY = sum(x*y)
sXX = sum(x**2)
m = (sX*sY -sXY*len(x))/(sX**2 -sXX*(len(x)))
b = (sY -sX*m)/len(x)
print()
print(x,y)
print("sX =",sX,"sY =",sY,"sXY =",sXY,"sXX =",sXX,"m =",m,"b =",b)

# number 5
regression = m*x +b
print()
print(regression)

# number 6
print()
r = sum((y -regression)**2)
print("r = ",r)

t = sum((y -sum(y)/len(y))**2)
print("t = ",t)

cD = 1-r/t
print("cD =",cD)

# number 7
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(x,y,'r*',x,regression,'b--')
plt.title('Random x vs y with regression')
plt.legend(['x vs y','x vs f(x)'])
plt.xlabel('x values')
plt.ylabel('y values')

# number 8
x = np.random.rand(100)
y = np.sin(x)

sX = sum(x)
sY = sum(y)
sXY = sum(x*y)
sXX = sum(x**2)
m = (sX*sY -sXY*len(x))/(sX**2 -sXX*(len(x)))
b = (sY -sX*m)/len(x)
print()
print(x,y)
print("sX =",sX,"sY =",sY,"sXY =",sXY,"sXX =",sXX,"m =",m,"b =",b)

regression = m*x +b
print()
print(regression)

print()
r = sum((y -regression)**2)
print("r = ",r)

t = sum((y -sum(y)/len(y))**2)
print("t = ",t)

cD = 1-r/t
print("cD =",cD)

import matplotlib.pyplot as plt
plt.figure(2)
plt.plot(x,y,'r*',x,regression,'b--')
plt.title('Random x vs sin(y) with regression')
plt.legend(['x vs sin(x)','x vs f(x)'])
plt.xlabel('x values')
plt.ylabel('y values')

