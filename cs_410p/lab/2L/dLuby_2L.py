# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 19:17:42 2022

@author: David Luby

#CS 410p - Lab Assignment 2L

# Prompt input for box(es) a,b,d,d (floats)
# Display inputs in order of inputs
# Swap a with b, b with c, c with d, d with a
# Display variable contents in the same order

#   10 total spaces and 2 digits after decimal
#       "%6.2f""% - 6 places correct to 2 decimals


# Compute c*d - a*b correct to 3 decimals (for final variables)

# Compute a**3 + 3*b*a**2 +3*a*b**2 + b**3 (for original values)

"""

#user inputs
a = float(input("Enter a value for box A: "))
b = float(input("Enter a value for box B: "))
c = float(input("Enter a value for box C: "))
d = float(input("Enter a value for box D: "))

#user feedback
print("\nYou entered: %10.2f" % a, "for box A")
print("You entered: %10.2f" % b," for box B")
print("You entered: %10.2f" % c," for box C")
print("You entered: %10.2f" % d," for box D")

#swaps
a1 = b
b1 = c
c1 = d
d1 = a

print("\nBox A changed to: %10.2f" % a1)
print("Box B changed to: %10.2f" % b1)
print("Box C changed to: %10.2f" % c1)
print("Box D changed to: %10.2f" % d1)

#computation 1
print("\nComputation 1: %10.3f" % (c1*d1 - a1*b1))

#computation 2
print("Computation 2: %10.2f" % (a**3 + 3*a**2*b + 3*a*b**2 + b**3))