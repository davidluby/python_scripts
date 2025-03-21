# David Luby
# ME 786
# HW 1 -- No. 6 -- Jacobi approximation
# 9-13-2022

## this is the jacobi algorithm for the SLE in hw 1 part 6

def jacobi(A,b,x): # jacobi function
    soln = [] # initialize empty solution matrix
    i = -1
    for row in A:
        i +=1
        j = -1
        sum = 0 # initialize dot product sum
        for col in row:
            j +=1
            if j != i: # ignore i == jth a[i][j] and x[j]
                sum += col*x[j] # sum a[i][j]*x[j]
        soln.append(round(1/A[i][i] * (b[i]-sum),3)) # compute and append x[i]^(k+1) to new solution vector
    print(soln)
    return(soln) # return x^(k+1) solution vector for recursion and accuracy

A = [[7, -3, 2], [1, 5, -3], [-1, -1, -6]] # coefficient matrix

b = [-4, 12, 11] # solution matrix

xGuess = [0, 0, 0] # initial x guess matrix

soln = jacobi(A,b,xGuess) # initial iteration

for x in range(0,10): # recursion for a few more iterations
    soln = jacobi(A,b,soln)


