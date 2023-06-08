# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 07:06:30 2022

@author: David Luby

CS 410P - Lab assignment 8

# take lower and upper farenheiht inputs
    # only integers; handle exceptions
# create farenheight list spaced by one degree
    # use to make celcius rankine kelvin list
# print each list in a for column set of rows after conversions
"""

flag = "bad"
while flag == "bad":
    try:
        start = int(input("Enter a low temp in farenheight: "))
        end = int(input("Enter a high temp in farenheight: "))
        if (start < end) and (start > -31) and (end < 131):
            flag = "good"
        else:
            flag = "bad"
    except:
        print("Please enter an integer temperature between -30 and 130 degrees")
        flag = "bad"

tempF = list(range(start,end+1))
tempC = []
tempK = []
tempR = []
for x in tempF:
    tempC.append(5/9*(x-32))
    tempK.append( 5/9*(x-32) +273.15)
    tempR.append(x +459.67)

print("F".center(8),"C".center(8),"K".center(8),"R".center(8))
i = 0
while i < len(tempF):
    print("\n{0:^8.2f}{1:^8.2f}{2:^8.2f}{3:^8.2f}".format(tempF[i],tempC[i],tempK[i],tempR[i]))
    i += 1
    
    
