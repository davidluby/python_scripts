# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:16:16 2022

@author: David Luby

#CS 410p - Lab assignment 4L

# takes an x-y point
    # determines which quadrant or axis point lies on
        # using if-else-elseif
        
# origin or not
    # axis or not
        # north or south (y)
            # east ot west (x)
"""

#coordinate intake
x = float(input("Enter an x-coordinate: "))
y = float(input("Enter a y-coordinate: "))

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
    
print("\nPoint is", location)