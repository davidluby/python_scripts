# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:21:30 2022

@author: David Luby

# CS 410P - Program assignment 10P


# define main function to intake atomic number and output element properties
    # read function to intake first file
    # update function to add three elemental properties from second file
    # print function to print the entire table

"""
import periodic as pPy
def main():
    
    # initializing first set of data
    starter = pPy.read('atomic_elements.txt')
    
    # adding extra data
    pTable = pPy.update('atomic_elements.txt','atomic_properties.txt',starter)
    
    # printing combined data in table
    pPy.tPrint(pTable)
    
    # loop for user input
    flag = 'false'
    while flag == 'false':
        try:                
            aNum = int(input("Enter an atomic weight from the periodic table: "))
            if aNum == 0:
                print('Terminated')
                flag = 'true'
            elif aNum < 1 or 118 < aNum:
                print('Error" no element corresponds to that number')
            else:
                pPy.ePrint(aNum,pTable)
                
        except:
               print("Make sure the value is an integer!")
               flag = 'false'
    
main()
