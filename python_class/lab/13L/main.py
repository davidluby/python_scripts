# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:25:51 2022

@author: David Luby

# CS 410P - Lab assignment 13L

# this is the main file used to call my four functions
"""
import dLuby_13L as funs

def main():
    name = input("Enter a file name with its .type specification: ")
    
    # run file through intake function to process data
    data = funs.intake(name)
    
    # run processed data through data handler to get sorted lists
    a,b = funs.handle(data)
    
    # run lists through printing function
    funs.listP(a,b)
    
    # run lists through file output (don't specify file type)
    oName = input("Name your output file: ")
    funs.oFile(oName,a)
    oName = input("Name your output file: ")
    funs.oFile(oName,b)
    
    return
main()
    


