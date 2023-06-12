# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:30:39 2022

@author: David Luby

# CS 410P - Lab assignment 12L


"""
import functions_2D as f

def main():
    #accept number of rows and columns for the 2-D list
    #both values must be integers between 1 and 10
    done = False
    while(not done):
        try:
            rows = int(input("Rows:"))
            columns = int(input("Columns:"))
            if 1 < rows < 11 and 1 < columns < 11:
                done = True
            else:
                print("Rows and Columns must be between 1 and 10!")
        except:
            print("Rows and Columns must be between 1 and 10!")
    
    #print()
    #initialize matrix with random values between 0 and 100
    matrix = f.initialize_matrix(rows, columns)
    print("Matrix:", rows, "Rows,", columns, "Columns")
    #print initial matrix
    f.print_matrix(matrix, rows, columns)
    #compute the sums of all 4 edges
    t, b, l, r = f.compute_edge_sums(matrix, rows, columns)
    print("\nSums:")
    print("\tTop row:", t)
    print("\tBottom row:", b)
    print("\tLeft column:", l)
    print("\tRight column:", r)
    print()
    #modify diagonal elements if applicable
    if rows == columns:
        print("Diagonal elements doubled:")
        f.double_diagonal_elements(matrix, rows, columns)
        f.print_matrix(matrix, rows, columns)
    else:
        print("Not a Square matrix")
main()