# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:25:35 2022

@author: David Luby

# CS 410p - Lab Assignment 1L
#
# This program will prompt the user for 3 numbers:
#   Side, Radius and Height
# It will calculate and print the Area of the following shapes:
#   Square (side x side), Circle (pi x radius x radius), Cube Surface (6 x side x side)
#   Sphere (4 x pi x radius x radius), Cylinder Lateral Surface (2 x pi x radius x height)
#   Cone Lateral Surface (pi x radius x side)
# It will also calculate and print the Volume of the following shapes:
#   Cube (side x side x side), Sphere (4/3 x pi x radius x radius x radius)
#   Cylinder (pi x radius x radius x height), Cone (1/3 x pi x radius x radius x height)
"""

import math

"""
user inputs
"""
s = int(input("Enter value for Side: "))
print("\nYou entered: Side =", s)

r = int(input("Enter value for Radius: "))
print("\nYou entered: Radius =", r)

h = int(input("Enter value for Height: "))
print("\nYou entered: Height =",h)


'''
outputs/computations
'''
#areas
print("\nArea of a Square = ", s**2)
print("Area of a Circle = ", math.pi*r**2)
print("Surface Area of a Cube = ", 6*s**2)
print("Surface Area of a Sphere = ", 4*math.pi*r**2)
print("Lateral Surface Area of a Cylinder = ", 2*math.pi*r*h)
print("Lateral Surface Area of a Cone = ", math.pi*r*s)

#volumes
print("\nVolume of a Cube = ", s**3)
print("Volume of a Sphere = ",4/3*math.pi*r**3)
print("Volume of a Cylinder = ",math.pi*r**2*h)
print("Volume of a Cone = ", 1/3*math.pi*r**2*h)

