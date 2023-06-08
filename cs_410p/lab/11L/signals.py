# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:21:15 2022

@author: David Luby

# CS 410P - Lab assignment 11L

# functions
    # variance
    # std dev
    # zero xing

"""

def read_data(name):
    nums = []
    file = open(name,"r")
    for line in file:
        nums.append((float(line.rstrip())))
        file.close
    count = len(nums)
    return(nums,count)

def compute_variance_std(nums):

    tot = 0
    for x in nums:
        tot += x
    mu = tot/len(nums)

    spread = 0
    for x in nums:
        spread = spread + (x-mu)**2
        var = spread/(len(nums)-1)

    std = var**.5
    return(var,std)

def  computer_zero(nums):

    i = -1
    j = 0
    count = 0
    while j < len(nums)-1:
        i +=1
        j +=1
        if (nums[i]-nums[j] > nums[i]) or (nums[j]-nums[i] > nums[j]):
            count +=1
            if nums[i] < 0 and nums[j] < 0:
                count -=1
    return(count)