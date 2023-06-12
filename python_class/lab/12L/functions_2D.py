# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:17:17 2022

@author: David Luby

# CS 410P - Lab assignment 12L

# intake to numbers which are x an y size of list
    # fill the list with random integers between 0-100
        # print row and column sums of:
            # first row, last row, first column, last column (sum edges)
        # for square matricies, double diagonals
            # if square matrix, use funciton to print matricies to print new

"""

def initialize_matrix(rows, columns):
    import random
    mat = []
    for row in range(0,rows): # for the number of rows
        mat.append([]) # create as many rows
        for column in range(0,columns): # for the number of columns
            val = random.randint(0,100) # create a value
            mat[row].append(val) # fill each row with value for each column
    return(mat)
            
def print_matrix(matrix, rows, columns):
    for row in range(0,rows):
        print("\n")
        for column in range(0,columns):
            print(matrix[row][column],end="\t")
    
def compute_edge_sums(matrix, rows, columns):
    i = -1
    t =0
    b =0
    l =0
    r =0
    while (i < rows-1) and (i < columns-1):
          i +=1
          t += matrix[0][i]
          b += matrix[rows-1][i]
          l += matrix[i][0]
          r += matrix[i][columns-1]
    return(t,b,l,r)

def double_diagonal_elements(matrix, rows, columns):
    i = -1
    while i < rows-1:
        i +=1
        matrix[i][i] = matrix[i][i]*2

    i = rows
    k = -1
    while i > 0:
        i -=1
        k +=1
        matrix[i][k] = matrix[i][k]*2
    if (rows%2 != 0) and (columns%2 !=0):
        x = int((rows/2)-.5)
        y = int((columns/2)-.5)
        matrix[x][y] = int(matrix[x][y]/2)
            
    return(matrix)