# -*- coding: utf-8 -*-
"""
Created on Sun Mar 2 15:06:58 

@author: anarayan
"""

#regression analysis using Least squares approximation and Pearson correlation
import regression_functions as regress


def main():
    fname = input("Enter Input Filename: ")

    x, y = regress.read_data(fname)
    print()
    print("Input File: ", fname)
    print("Data points: ", len(x))
    
    #compute coefficients m and b
    m, b = regress.compute_m_and_b(x, y)
    
    #compute fx and residual
    fx, residual = regress.compute_fx_residual(x, y, m, b)
    
    #compute sum of squared residuals
    least_squares_r = regress.compute_sum_of_squared_residuals(residual)
    
    #compute sum of squares
    sum_squares = regress.compute_total_sum_of_squares(y)
    
    #compute coefficeint of determination
    coeff_of_d = regress.compute_coeff_of_determination(least_squares_r, sum_squares)
    
    regress.print_least_squares(x, y, m, b, fx, residual, least_squares_r, sum_squares, coeff_of_d)
    
    #compute pearson coefficient
    pearson_r = regress.compute_pearson_coefficient(x, y)

    regress.print_pearson(pearson_r)


    return

    
main()