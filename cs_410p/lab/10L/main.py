# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 05:34:46 2022

@author: David Luby

# CS 410P - Lab Assignment 10L

# make function call that will print the results of where_is_xy
    # until non-numeric is entered
        # store every coordinate PAIR in tuple
            # print each pair and distance between i : i+1
            
    
    
    
    
    
"""
import xy
import math

#coordinate intake    
n = ""
coords = []
while n == "":
    nums = input("Enter x and y separated by a space: ")
    try:
        x, y = nums.split()
        x = float(x)
        y = float(y)
    except:
        n = "z"
        print("Terminated")
    else:
        n = ""
        coords.append(nums)
print("\n\nPoints: \n",coords,"\n\nLocations:")
for x in coords:
    a, b = x.split()
    a = float(a)
    b = float(b)
    print("(",a,",",b, ") is", xy.where_is_xy(a,b))
print("\nDistances:")

trail = -1
lead = 0
while lead < len(coords)-1:
    trail += 1
    lead += 1
    a1, b1 = coords[trail].split()
    a2, b2 = coords[lead].split()
    dx = (float(a2)-float(a1))**2
    dy = (float(b2)-float(b1))**2
    print("Distance",lead,"is %1.2f"%math.sqrt(dx+dy))
if lead == 0:
    print("No distance")

print("\nIt was unclear to me what could and could not be in the main script.\n"
      "I ended up doing everything but where_is_xy locations")