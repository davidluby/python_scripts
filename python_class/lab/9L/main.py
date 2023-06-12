# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:46:52 2022

@author: David Luby

# CS 410P - Lab assignment 9L

"""



import gcd_lcm
#Below is the "main" function which acts as the entry point
if __name__ == '__main__':
    
    n = ""
    n1 = 0
    n2 = 1
    while n == "":
        try:
            n1 = int(input("Enter an integer: "))
            n2 = int(input("Enter an integer: "))
            if (n1 <1) or (n2 <1):
                n = ""
                print("Enter integers greater than 0")
            else:
                n = "z"
        except:
            n = ""
            print("Enter an integer")
                

    gcd_result = gcd_lcm.gcd(n1, n2)
    lcm_result = gcd_lcm.lcm(n1, n2)
    print("gcd = ", gcd_result)
    print("lcm = ", lcm_result)




