# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 02:00:27 2022

@author: David Luby

# CS 410P - Program Assignment 1P
    # leapyear.py
    
# handles year input of -46-5000 (integers only)
    # continuous prompting for inputs unless out of +-9999
    # exception handler for non-integers
        # if's for valid and breaking boundaries

# determine if julian or gregorian leap
    # julian leaps are divisible by 4
    # gregorian leaps are multiples of 4
        # unless multiple of 100 and not 400

# print out all outcomes for type of leap, invalid, and break

"""

# creating input recursion
year = 0
while -10000 < year < 10000:
    try:
        year = int(input("Enter a year to be tested as a leap-year: "))
    except:
        year = "recursion reassignment/placeholder"
        while isinstance(year, int) != True: # input exception recursion
            try:
                year = int(input('Make sure to enter a whole integer: '))
            except:
                if isinstance(year, int) != True:
                    year = "recursion reassignment/placeholder"
                else:
                    break # out of nested loop
    else: # continuation for parent loop

# now building output algorithm
# constants return year/divisor remainder
        four = year % 4
        hund = year % 100
        fohu = year % 400

        if year < -46 or year > 5000 or year ==0:
            out = "Invalid Year"
        elif -46 <= year <= 1752:
            if four == 0: # if remainder = 0, whole number
                out = "Julian Leap Year"
            else:
                out = "Julian Non Leap Year"
        elif 1753 <= year <= 5000:
            if four == 0:
                if hund == 0:
                    if fohu == 0:
                        out = "Gregorian Leap Year"
                    else:
                        out = "Gregorian Non Leap Year"
                else:
                    out = "Gregorian Leap Year"
            else:
                out = "Gregorian Non Leap Year"
        print("Year",year,out)