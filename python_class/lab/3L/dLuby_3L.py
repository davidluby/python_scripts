# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 14:59:56 2022

@author: David Luby

CS 410p - Lab assignment 3L
"""

"""
# take P principal, interest rate, n # years to find future value
    # annually compounding

# take future value, interest rate, n# years to determine principal
    # anually compounding

"""

#for determining the future amount based on principal
principal = float(input("Enter a principal dollar amount: "))
term = int(input("Enter a term length in years: "))
rate = float(input("Enter an interest rate (as %): "))/100

#computation and display
futureValue = principal*(1+rate)**term

print("\nTerm length =",term,"years")
print("Interest rate = {:1.2%}".format(rate))
print("Your money will be worth ${:1,.2f}"
      .format(futureValue),"at the term's end")


#for determining the principal based on future amount
future = float(input("Enter a future dollar amount: "))
term2 = int(input("Enter a term length in years: "))
rate2 = float(input("Enter an interest rate (as %): "))/100

#computation and display
principalValue = future/(1+rate2)**term2


print("\nTerm length =", term2,"years")
print("Interest rate = {:1.2%}".format(rate2))
print("You need to invest ${:1,.2f}"
      .format(principalValue),"to satisfy your earning goal")