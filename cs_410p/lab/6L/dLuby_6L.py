# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:15:33 2022

@author: David Luby

CS 410P - Lab Assignment 6L


# take inputs of coefficient of restitution and height of drop
    # catch invalid inputs with exceptions
        # c.o.r. must be between 0 and 1
        # height initial must be greater than 10 cm
            # loop invalid inputs to reprompt, not terminate prog
    # output coefficient, drop height, number of bounces to 10 cm
        meters traveled
"""

# initializing while loop variables
cor = -1
h = 0
while cor <= 0 or 1 <= cor: # creating restitution recursion
    try: # try for float input
        cor = float(input("Enter Coefficient of Restitution between 0 and 1: "))
        if cor <= 0 or 1 <= cor: # print error if out of range
            print("Invalid, make C.O.R. between 0 and 1.")
    except: # field exceptions
        cor = -1 # placeholder for recursion and error message
        print("\nInvalid, make a floating point or integer value.")
        
while h < .1: # creating height recursion
    try: # try for float
        h = float(input("Enter drop height of at least .1 m: "))
        if h < .1: # print error for our of range
            print("\nMake height greater than .1 m.")
    except:# field exceptions
        h = 0 # placeholder for recursion and error message
        print("\nMake height a floating point or integer value.")

# print before manipulation
print("\nThe C.O.R. is", cor)
print("The starting height is", h, "meters")

# defining "storage" variables
hNew = 1
count = 0
distTot = 0
while h >= .1: # while recursion for ball until less than .1 meter bounce
    hNew = h*cor # create bounce height from drop height
    dist = h + hNew # distance per drop and bounce cycle
    distTot = distTot + dist # sum of previous and current cycle
    h = hNew # reassign h for next calculation
    count = count + 1 # add 1 to bounce count per cycle
distTot = distTot - hNew # subtract final bounce up from distance since < .1 m

# print remaining results
print("The number of bounces is", count)
print("The distance traveled is %1.5f"% distTot, "meters")








