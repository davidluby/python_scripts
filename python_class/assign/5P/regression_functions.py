# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:17:19 2022

@author: David luby

# CS 410P - Program assignment 5P

# create functions to:
    # read and return x and y list objects
    # compute m and b coefficients using x and y matricies
    # compute fx residual
    # compute sum of squared residuals
    # compute sum of total squares
    # compute coefficient of  determination
    # compute least squares
    # compute pearson coefficient
"""

# intake function
def read_data(fname):
    name = fname +".txt"
    txt = open(name,'r')
    x = []
    y = []
    for line in txt:
        a,b = line.strip().split(",")
        x.append(float(a))
        y.append(float(b))
    return(x,y)
# linear regression
def compute_m_and_b(x, y):
    i = -1
    sX = 0
    sY = 0
    sXY = 0
    sXX = 0
    while i < len(x)-1:
        i +=1
        sX +=x[i]
        sY +=y[i]
        sXY +=x[i]*y[i]
        sXX +=x[i]**2

    m = (sX*sY -sXY *len(x)) /(sX**2 -sXX *len(x))
    b = (sY -sX *m)/len(x)
    return(m,b)

# fX and residuals
def compute_fx_residual(x, y, m, b):
    i = -1
    fX = []
    res = []
    while i < len(x)-1:
        i +=1
        fX.append(m *x[i] +b)
        res.append(y[i] -fX[i])
    return(fX,res)

# sum squares
def compute_sum_of_squared_residuals(residual):
    i = -1
    sSq = 0
    while i < len(residual)-1:
        i +=1
        sSq +=(residual[i])**2
    return(sSq)

def compute_total_sum_of_squares(y):
    i = -1
    sSq = 0
    yAv = sum(y)/len(y)
    while i < len(y)-1:
        i +=1
        sSq +=(y[i]-yAv)**2
    return(sSq)

# coefficient of determination
def compute_coeff_of_determination(least_squares_r, sum_squares):
    cD = 1-(least_squares_r/sum_squares)
    return(cD)

def print_least_squares(x, y, m, b, fx, residual, least_squares_r, sum_squares, coeff_of_d):
    print()
    print("Coefficients: m = %1.3f"%m,"    b = %1.3f"%b)
    print()
    print("{0:<8}""{1:<8}""{2:<8}""{3:<8}".format("x","y","f(x)","res"))
    i = -1
    while i < len(x)-1:
        i +=1
        print("%1.3f"%x[i],"%1.3f"%y[i],"%1.3f"%fx[i],"%1.3f"%residual[i],sep="   ")
    print()
    print("Sum of squared residuals: %1.3f"%least_squares_r)
    print("Total sum of squares: %1.3f"%sum_squares)
    print("Coefficient of determination: %1.3f"%coeff_of_d)
# pearson
def compute_pearson_coefficient(x, y):
    i = -1
    num = 0
    denL = 0
    denR = 0
    xAv = sum(x)/len(x)
    yAv = sum(y)/len(y)
    while i < len(x)-1:
        i +=1
        num += (x[i] -xAv) *(y[i] -yAv)
        denL += (x[i]-xAv)**2
        denR += (y[i]-yAv)**2
    pearson_r = num /((denL**.5) *denR**.5)
    return(pearson_r)
        
def print_pearson(pearson_r):
    print()       
    print("Pearson correlation coefficient: %1.3f"%pearson_r)










