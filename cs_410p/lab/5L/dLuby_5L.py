# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 03:38:48 2022

@author: David Luby

CS 410P - Lab Assignment 5L

# takes decible input
    quiet @ x <50
    intrusive @ 51< x <70
    annnoying @ 71< x < 90
    very annoying @ 91< x < 110
    uncomfortable @ 111< x < 150
    unacceptable @ 150< x
# returns decible perception
        # nested ifs
        #exception handler for non-integers
        # constants for values that never change
        
"""

#defining range constants for easy programming
low = 0
qui = 50
intr = 70
ann = 90
vAn = 110
unc = 150

try:
    dec = int(input("Enter a decible mangitude: "))
   
except: #broad exception handler (no specification)
    print("\nYou must enter an integer decibel value next time.")
else:
    if dec < low: #brute-force exception handler for negative integers
        out = "less than 0 and invalid."
    else:
        if dec >= low: #nested if statement
            if dec <= qui:
                out = "quiet."
            else: #more than one possibility, so cannot yet assign to out here
                if qui < dec <= intr:
                    out = "intrusive."
                elif intr < dec <= ann:
                    out = "annoying."
                elif ann < dec <= vAn:
                    out = "very annoying."
                elif vAn < dec <= unc:
                    out = "uncomfortable."
                elif dec > unc:
                    out = "unacceptable."
    print("\n",dec,"decibles is",out) #return results
