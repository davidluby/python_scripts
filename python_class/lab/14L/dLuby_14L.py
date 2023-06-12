# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:52:35 2022

@author: David Luby

# CS 410P - Lab assignment 14L

#  follow tutorial lab
    # not much to commment
"""

import numpy as np

#no 1
print(np.__version__)

#no 2
nullV = np.zeros(10, int)
print()
print(nullV)
nullV[5:10] = 5
print()
print(nullV)

#no 3
oneD = np.arange(10,100)
print()
print(oneD)

#no 4
randV = np.random.randint(10,101,10)
print()
print(randV)

#no 5
randInt = np.random.randint(0,9,size=(3,3))
print()
print(randInt)

#no 6
new = np.array([1,2,0,0,4,0],int)
idx = new.nonzero()
print()
print(idx)

#no 7
idM = np.identity(3,dtype= int)
print()
print(idM)

#no 8
zeros = np.zeros(shape=(5,5),dtype=int)
print()
print(zeros)
zeros[:,0] = 5
zeros[4,:] = 5
print("\n",zeros)

#no 9
checker = np.zeros(shape=(8,8),dtype=int)
checker[0::2,0::2] = 1
checker[1::2,1::2] = 1
print()
print(checker)

#no 10
rArray = np.random.randint(0,10,25)
print()
print(rArray)
nArray = sorted(rArray)
print(nArray)


