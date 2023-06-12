# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 05:25:53 2022

@author: David Luby

# CS 410P - Lab assignment 10L


# make a function script for x and y that says where they are from list
    


"""

# function definition and coordinate intake
def where_is_xy(x,y):
    
    #logical path
    if y == 0 and x == 0:
        location = "on origin"
    elif y == 0 and x > 0:
        location = "on positive x-axis"
    elif y == 0 and x < 0:
        location = "on negative x-axis"
    elif y > 0 and x == 0:
        location = "on positive y-axis"
    elif y < 0 and x == 0:
        location = "on negative y-axis"
    elif y > 0 and x > 0:
        location = "in 1st quadrant"
    elif y > 0 and x < 0:
        location = "in 2nd quadrant"
    elif y < 0 and x < 0:
        location = "in 3rd quadrant"
    else:
        location = "in 4th quadrant"
    return(location)