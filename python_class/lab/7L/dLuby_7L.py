# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 20:49:53 2022

@author: David Luby


CS 410P - Lab Assignment 7L

# take number series input from user and store them in a list
    # stop intake when user presses enter
        # print number of items in list
        # print list sorted in ascending order
            # print sum, average, max, and min values of list
                # use methods/functions supported by the list object
            # print first half of list w/ index slicing
            # print list one by one using while loop
"""


# initializing variables/objects
end = 0
nums = []
while end == 0: # establishing recursion
    new = input("Enter a number to be stored in a list: ") # input intake
    if new == "": # process input for enter termination
        end = 1
        break
    else:
        try: # input for nums list
            nums.extend([int(new)]) # extending numbs by each new input
        except: # fielding other exceptions
            print("Numbers only")

# length
length = len(nums)
if length == 0:
    print("\nThe list is empty")
else:
    print("\nThe list is",length,"items long")

# sorting
    nums.sort();
    print(nums)

# sum, avg, max, min
    print("Sum = ",sum(nums))
    avg = sum(nums)/length
    print("Average = %1.2f"% avg)
    print("Maximum = ",max(nums))
    print("Minimum = ",min(nums))
    half = round(length/2)
    print(nums[0:half])
# loop printing
    print("List printed with a while loop: ")
    x = -1
    while x < length-1:
        x = x + 1 # creating counter for ith index
        print(nums[x], end='\t')



