# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:56:28 2022

@author: David Luby

# CS 410P - Program Assignment 2P

# prompt for integer 1-1000
    # less than 1 or greater than 1000 print invalid and reprompt
    # = 1000, terminate
    # catch non integers
    # all other cases:
        # print fibonacci list
            # 10 items per line
            # print list size
        # print prime number list
            # 10 per line
            # print list size
        # print list where fib list is found in prime list
            # print list size and list
"""
# error initialization
n = ""

# fibonacci initialization
n1 = 0
n2 = 1
fib_count = 1


fib = []
while n == "":
    try:
        n = int(input("Enter an integer: "))
        if (n <1) or (n >1000):
            n = ""
            print("Enter an integer between 0 and 1001")
        elif n == 1000:
            n = "z"
    except:
        n = ""
        print("Please enter an integer.")
    else:
        if n == "":
            n = n
        elif n == "z":
            n = "z"
        else:
            fib.extend([n1])
            fib.extend([n2])
            while n2 <= n:
                # fibonacci sequence
                fib_count = fib_count+1
                n3 = n2
                n2 = n2 +n1
                n1 = n3
                fib.extend([n2])

j = 0
i = 0
k = 0
print("\nFibonacci list:")
while j < len(fib):
    i = 0   
    while (i < 10) and (k < len(fib)-1):
        print(fib[k],end='\t')
        k += 1
        i += 1
        if i == 10:
            print("")
    j += 1        
print("\nTotal Fibonacci:", fib_count)
       

# primes
i = 2 # number iteration start
primes = []
while i <= n: # continuation through n
    j = 2 # division iteration reset
    flag = False # flag reset
    while (flag == False) and (j < i): # continuation until break sequence
        if i % j == 0:
            flag = True
        else:
            flag == False
        j += 1 # division iteration counter
    if flag == False:
        primes.extend([i]) # append primes if false flag & j = i
    i += 1 # iterate next number

j = 0
i = 0
k = 0
print("\nPrimes list:")
while j < len(primes):
    i = 0   
    while (i < 10) and (k < len(primes)):
        print(primes[k],end='\t')
        k += 1
        i += 1
        if i == 10:
            print("")
    j += 1


prime_count = len(primes)
print("\nTotal Prime:", prime_count)         


# combined values
q = 0
shared = []            
while q < len(primes):
    z = 0
    flag = False
    while (flag == False) and (z < len(fib)):            
        if primes[q] == fib[z]:
            shared.extend([primes[q]])
            flag = True
        else:
            flag == False
            z += 1
    q += 1

j = 0
i = 0
k = 0
print("\nCombined list:")
while j < len(shared):
    i = 0   
    while (i < 10) and (k < len(shared)):
        print(shared[k],end='\t')
        k += 1
        i += 1
        if i == 10:
            print("")
    j += 1

combined_count = len(shared)
print("\nTotal Combined:", combined_count)

            
            