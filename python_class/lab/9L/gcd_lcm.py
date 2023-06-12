# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:56:37 2022

@author: David Luby

# CS 410P - Lab assignment 9L


# have function take numbers
    # create list for integers below
        # loop through and find common factor
    # create two lists of multiples until list[i] = list2[i]


"""


def gcd(number1, number2):
    nums = list(range(1,number1+1))
    nums2 = list(range(1,number2+1))
    if max(nums) < max(nums2):
        nums3 = nums
        nums = nums2
        nums2 = nums3
    div = []
    div2 = []
    for i in nums:
        div.append(max(nums)% i)
    for j in nums2:
        div2.append(max(nums2)% j)
    k = -1
    r = 1
    while r < len(div):
        r += 1
        k += 1
        if (div[k] == 0) and (div2[k] == 0):
            result = nums[k]
    return(result)


def lcm(number1, number2):
    result = 0
    k = -1
    j = 1
    nums = []
    nums2 = []
    flag = False
    while flag == False:
        j += 1
        k += 1
        nums.append(number1*j)
        nums2.append(number2*j)
        for i in nums:
            for q in nums2:
                if i == q:
                    result = i
                    flag = True
                    break

    return(result)

