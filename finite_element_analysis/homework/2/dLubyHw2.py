# David Luby
# ME 786
# HW 2
# 9-21-2022

##solution to hw2 no 1

A = [[500, 0, -500, 0, 0], [0, 900, -900, 0, 0], [-500, -900, 1700, -300, 0], [0, 0, -300, 1100, -800], [0, 0, 0, -800, 800]] # stiffness matrix

u = [0, 0, .4637, .1265, 0]

force = []

for row in A:
    sum = 0
    i = -1
    for col in row:
        i += 1
        sum += row[i]*u[i]
    force.append(sum)
print()
print('Forces (in order) = ',force)
print('The numbers are slightly off due to rounding errors. 1st, 2nd, and 5th are reactions.')

##solution to hw2 no 2
import numpy as np
from scipy.linalg import solve 
A = np.array([[220, -130, 0], [-130, 250, -120], [0, -120, 195]]) # stiffness matrix)
b = np.array([125, -95, 0])
 
x = solve(A, b)
print('\nNodal displacements (from left to right): ',x)