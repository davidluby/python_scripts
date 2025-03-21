# David Luby
# ME 786
# HW 1 -- No. 6 -- Gauss-Seidel approximation
# 9-13-2022

## this is the gauss-seidel algorithm for the SLE in hw 1 part 6

def gaussSeidel(A,b,x): # gauss-seidel function
    new = []
    i = -1
    for row in A:
        i += 1
        j = -1
        sum = 0
        for col in row:
            j += 1
            if i != j and j < len(new):
                sum += col*new[j]
            elif i != j:
                sum += col*x[j]

        new.append(round(1/A[i][i] * (b[i]- sum),3)) # x[i]^(k+1) vector

    print(new)
    return(new)

A = [[7, -3, 2], [1, 5, -3], [-1, -1, -6]] # coefficient matrix

b = [-4, 12, 11] # solution matrix

xGuess = [0, 0, 0] # initial x guess

soln = gaussSeidel(A,b,xGuess) # initial iteration

for x in range(0,10): # recursion for a few more iterations
    soln = gaussSeidel(A,b,soln)


