# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 00:19:22 2022

@author: David Luby

#CS 410p - Assignnment 0P

# Approximate ellipse circumference
#   area = pi*a*b

# Use each approximation formula to estimate circumference
#   **based on user prompt
"""

import math

#user prompt
a = float(input("Input major axis: "))
b = float(input("Input minor axis: "))

#approximations

#ramanujan's first
ramOne = math.pi* (3*(a+b)- math.sqrt((3*a+b)* (a+3*b)))

#ramanujan's second
h = (a-b)**2/(a+b)**2
ramTwo = math.pi* (a+b)* (1+ 3*h/ (10+ (4- 3*h)**.5))

#muir's
muir = 2*math.pi* (a**1.5/2+ b**1.5/2)**(1/1.5)

#hudson's
hud = math.pi/4*(a+b)* (3*(1+ h/4)+ 1/(1-h/4))

#holder's
s = math.log(2)/math.log(math.pi/2)
hold = 4* (a**s+b**s)**(1/s)

#centrell's
s = .825056
cant = 4*(a+b)- 2*(4-math.pi)*a*b/ (a**s/2 + b**s/2)**(1/s)


print("\n{0:^25}{1:^25}"
      .format("Major axis input =%5.2f"%a, "Minor axis input =%5.2f"%b))
print("--------------------------------------------------")
print("{0:^25}{1:^25}"
      .format("Approximation Method", "Circumference"))
print("{0:^25}{1:^25}"
      .format("First Ramanujan", "%10.6f"%ramOne))
print("{0:^25}{1:^25}"
      .format("Second Ramanujan", "%10.6f"%ramTwo))
print("{0:^25}{1:^25}"
      .format("Muir", "%10.6f"%muir))
print("{0:^25}{1:^25}"
      .format("Hudson","%10.6f"%hud))
print("{0:^25}{1:^25}"
      .format("Holder", "%10.6f"%hold))
print("{0:^25}{1:^25}"
      .format("Cantrell", "%10.6f"%cant))