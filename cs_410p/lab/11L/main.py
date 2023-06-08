# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:22:20 2022

@author: David Luby

# CS 410P - Lab Assignment 11L

# intake file with noise data and store in a list
    # output the number of points
    # variance
    # std. deviation
    # number of roots

"""

import signals

name = str(input("Enter the file name: "))


nums,count = signals.read_data(name)
var,std = signals.compute_variance_std(nums)
zeros = signals.computer_zero(nums)

print("Sample Size: ",count)
print("Variance: %1.6f"%var)
print("Std. Dev.: %1.6f"%std)
print("Zero Crossings: ",zeros)

