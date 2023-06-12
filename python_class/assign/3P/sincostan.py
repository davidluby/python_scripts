# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:59:46 2022

@author: David Luby

"""


import math

def find_sin_cos_tan(x,y):
    rads = []
    nums = list(range(x,y+5,5))
    for x in nums:
        rads.append(math.pi/180*x)

    sin = []
    cos = []
    tan = []
    for x in rads:
        sin.append(round(math.sin(x),4))
        cos.append(round(math.cos(x),4))
        if -100 <= math.tan(x) <= 100:
            tan.append(round(math.tan(x),4))
        else:
            tan.append(int(99999))
    return(sin, cos, tan)

def display_rows(x,y,sin,cos,tan):
    nums = list(range(x,y+5,5))
    i = -1
    print('\nDegrees: ',end='\t')
    while i < len(sin)-1:
        i += 1
        print("%6.0f"%nums[i],end= '\t')
    i = -1
    print('\nSin:      ',end='\t')
    while i < len(sin)-1:
        i += 1
        print("%2.4f"%sin[i],end= '\t')
    i = -1
    print('\nCos:     ',end='\t')
    while i < len(sin)-1:
        i += 1    
        print("%2.4f"%cos[i],end= '\t')
    i = -1
    print('\nTan:     ',end='\t')
    while i < len(sin)-1:
        i += 1
        print("%2.4f"%tan[i],end= '\t')

def display_columns(x,y,sin,cos,tan):
    nums = list(range(x,y+5,5))
    print("{0:^10s}{1:^10s}{2:^10s}{3:^10s}".format("\nDegrees","Sin","Cos","Tan"))
    i = -1
    while i < len(sin)-1:
        i += 1
        print("{0:^10.4f}{1:^10.4f}{2:^10.4f}{3:^10.4f}"
              .format(nums[i],sin[i],cos[i],tan[i]))
                        


def display_totals(sin,cos,tan):
    sCount = 0
    cCount = 0
    tCount = 0
    for x in sin:
        if x < 0:
            sCount += 1
    for x in cos:
        if x < 0:
            cCount += 1
    for x in tan:
        if x == 99999:
            tCount += 1
    print("\nNegative sin: ",sCount)
    print("Negative cos: ",cCount)
    print("Indeterminant tan: ",tCount) 