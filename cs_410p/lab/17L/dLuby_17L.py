# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:07:09 2022

@author: David Luby

# CS 410P - Program assignment 8P


"""
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import math

# intake function to put file data into lists
def intake(filename):
    x = []
    y = []
    i = -1
    data = open(filename)
    for lines in data:
        i +=1
        xDta,yDta = lines.strip().split(",")
        x.append(xDta)
        y.append(yDta)
    x1 = np.array(x,float)
    y1 = np.array(y,float)
    data.close()
    return(x1,y1)

i = -1
x = []
y = []
while i < 3:
    i +=1
    a,b = intake("in"+str(i+1)+".txt")
    x.append(a)
    y.append(b)

# manual regression
def manualReg(x,y):
    sX = np.sum(x)
    sY = np.sum(y)
    sXY = np.sum(x*y)
    sXX = np.sum(x**2)
    m = (sX*sY -sXY*len(x)) /(sX**2 -sXX*(len(x)))
    b = (sY -sX*m) /len(x)
    return(m*x+b,m,b)

i = -1
fMan = []
mMan = []
bMan = []
while i < 3:
    i +=1
    f,m,b = manualReg(x[i],y[i])
    fMan.append(f)
    mMan.append(m)
    bMan.append(b)

# SciPy regression
def scipyReg(x,y):
    A = np.vstack([x,np.ones(len(x))]).T
    m,c = np.linalg.lstsq(A,y)[0]
    return(m*x+c,m,c)

i = -1
fSci = []
mSci = []
bSci = []
while i < 3:
    i +=1
    f,m,c = scipyReg(x[i],y[i])
    fSci.append(f)
    mSci.append(m)
    bSci.append(b)

# plotting function
def graph(x,y,f,m,b,fS,mS,bS,i):
    ax = fig.add_subplot(2,2,i+1)
    ax.plot(x,y,'bo',x,f,'r',x,fS,'go')
    ax.set_title('in'+str(i+1)+'.txt | m = '+str(round(m,3))+' | b = '+str(round(b,3)))
    ax.set_ylabel('y-data')
    ax.set_xlabel('x-data')
    ax.legend(('y vs x','fMan vs x','fSci vs x'),loc='upper left',fontsize='xx-small')
    #ax.set_figheight(5)
    #ax.set_figwidth(5)

i = -1
fig = plt.figure(figsize=(15,10))
fig.subplots_adjust(hspace=.3, wspace=.3)
#fig.subplots(2,2,figsize=(15,15))
while i < 3:
   i +=1
   graph(x[i],y[i],fMan[i],mMan[i],bMan[i],fSci[i],mSci[i],bSci[i],i)





