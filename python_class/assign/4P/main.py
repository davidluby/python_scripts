# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:02:32 2022

@author: David Luby

# CS 410P - Program assignment 4P

# create a function to take two inputs for temperatures
    # first smaller than second
    # feed through to functions to compute:
        # wind chill
        # relative humidity
    # handle exceptions and integers only


"""
import functions
flag = 0
numx = []
numy = []
while flag == 0:
    try:
        x,y = input("Enter integers between 20 and 50 C: ").split()
        x = int(x)
        y = int(y)
        if -20 <= x <= 50 and -20 <= y <= 50 and x < y:
            numx.append(x)
            numy.append(y)
            print("x = ",x,"y = ",y,"\n")
        else:
            print("Make integers between 20 and 50, first smaller than "
                  "second.")
            flag = 0
    except:
        print("Terminated.")
        flag = 1
        break

i = -1
while i < len(numx)-1:
    i +=1
    functions.compute_wind_chill(numx[i],numy[i])
    functions.compute_heat_index(numx[i],numy[i])



