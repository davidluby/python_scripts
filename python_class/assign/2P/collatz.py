# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:50:03 2022

@author: David Luby

# CS 410P - Program Assignment 2P


# while n != 1
    # if integer is even, divide by two
        # else multiply by three and add one
            # print history and count            
"""
n = ""
count = 0
hist = []
while n == "":
    try:
        n = int(input("Enter an integer: "))
        if n <= 0:
            n = ""
            print("Enter a positive integer")
    except:
        n = ""
        print("Please enter an integer.")
    else:
        if n == "":
            n = n
        else:
            hist.extend([n])
            while n != 1:
                count = count+1
                idx = count-1
                if (n % 2) == 0:
                    n = n/2
                    hist.extend([n])
                    print(hist[idx],end='\t')
                else:
                    n = n*3 +1
                    hist.extend([n])
                    print(hist[idx],end='\t')
            print(hist[idx+1],end="\t")
            print("\n",count, "transformations")