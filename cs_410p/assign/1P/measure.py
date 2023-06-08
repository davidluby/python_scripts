# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 01:07:53 2022

@author: David Luby

# CS 410P - Program Assignment 1P
    # measure.py

# store two coordinates in 4 variables
    # compute distance between points
        # pythagorean
    # compute bearing angle from first to second point
        # clockwise unit circle starting at positive y axis
    # compute sweep angle from first point to second
        # bearing angle from origin to 2nd point then subtract
        # bearing angle from origin to 1st point from that
# display results in table according to specifications

"""
# imports
import math

# taking user inputs
x1 = float(input("Please enter a value for x1: "))
y1 = float(input("Please enter a value for y1: "))
x2 = float(input("Please enter a value for x2: "))
y2 = float(input("Please enter a value for y2: "))

# difference constants
x12 = x2 - x1
y12 = y2 - y1


# distance calculation (meters)
dist = ((x12)**2 + (y12)**2)**.5

# bearing angle (radians)
b12 = math.atan2(x12,y12)

# sweep angle
b01 = math.atan2(x1,y1) # bearing origin - 1
b02 = math.atan2(x2,y2) # bearing origin - 2
s02 = b02-b01 # sweep



# table 1: meters (25) radians (25.3) radians (25.3)
print("\n{0:^75s}".format("----------------------------------------------------------------------"))
print("{0:^25s}{1:^25s}{2:^25s}".format("Distance (meters)", "Bearing Angle (radians)","Sweep Angle (radians)"))
print("{0:^25.0f}{1:^25.3f}{2:^25.3f}".format(dist, b12, s02))
print("{0:^75s}".format("----------------------------------------------------------------------"))

#table 2: meters (25.5) degrees (25.3) degrees (25.2)
print("\n{0:^75s}".format("----------------------------------------------------------------------"))
print("{0:^25s}{1:^25s}{2:^25s}".format("Distance (meters)","Bearing Angle (degrees)","Sweep Angle (degrees)"))
print("{0:^25.5f}{1:^25.3f}{2:^25.2f}".format(dist, b12*180/math.pi,s02*180/math.pi))
print("{0:^75s}".format("----------------------------------------------------------------------"))

#table 3: feet (25.2) degrees (25.0) degrees (25.1)
print("\n{0:^75s}".format("----------------------------------------------------------------------"))
print("{0:^25s}{1:^25s}{2:^25s}".format("Distance (feet)","Bearing Angle (degrees)","Sweep Angle (degrees)"))
print("{0:^25.2f}{1:^25.0f}{2:^25.1f}".format(dist*3.28084,b12*180/math.pi,s02*180/math.pi))
print("{0:^75s}".format("----------------------------------------------------------------------"))




















