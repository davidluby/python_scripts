# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 02:59:55 2022

@author: David Luby

# CS 410P - Program assignment 3P


# create program that has main script to call on four other functions to:
    # compute value of sin, cos tan
    # display table computation in formatted in rows
    # display table computation formatted in columns
    # sum of negative sin, cos, and indeterminate tangent values

"""

flag = 0
while flag == 0:
    try:
        x,y = input("Enter integers between 0 and 360 degrees "
                              "separated by a space: ").split()
        x = int(x)
        y = int(y)
        if 0 <= x <= 360 and 0 <= y <= 360 and x < y and (y-x <= 90):
            flag = 1
            print("x = ",x,"y = ",y)
        else:
            print("Make integers between 0 and 360, first smaller than "
                  "second, and difference <= 90.")
            flag = 0
    except:
        print("Terminated.")
        flag = 1

import sincostan
sin, cos, tan = sincostan.find_sin_cos_tan(x,y)
sincostan.display_rows(x,y,sin,cos,tan)
sincostan.display_columns(x,y,sin,cos,tan)
sincostan.display_totals(sin,cos,tan)
        
        