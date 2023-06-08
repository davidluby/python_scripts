# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:03:26 2022

@author: David Luby

# CS 410P - Lab Assignment 13P


# take input file of type csv\
    # process data and split into two categories
        # output each file category into two new files
            # output the top ten of each file for:
                # population and area
                # and country name
"""
# file intake function
def intake(name):
    file = open(name,'r')

    lines = []
    co = [',Asia,',',America,',',Europe,',',Antarctica,',',Australia,',
          ',Africa,',',South America,']
    for x in file:
        for y in co:
            if len(x.split(y)) > 1:
                lines.append(x.strip().split(y))
    file.close()
    return(lines)

# list creation function
def handle(data):
    i = -1
    popu = []
    area = []
    pCombo = []
    aCombo = []
    while i < len(data)-1:
        i +=1
        x,y = data[i][1].split(',')
        popu.append(float(x))
        area.append(float(y))
        tupP = (popu[i],data[i][0])
        tupA = (area[i],data[i][0])
        pCombo.append(tupP)
        aCombo.append(tupA)
    pCombo.sort(reverse=True)
    aCombo.sort(reverse=True)
    return(pCombo,aCombo)

# list printing function
def listP(a,b):
    print("{0:<17}{1:<25}".format('Population','Country'))
    print("-------------------------------------------------")
    i =-1
    while i < 10:
        i +=1
        numP, nameP = a[i]
        print("{0:<17.2f}{1:<25}".format(int(numP)*1000**2,nameP),sep='\t')
    print("\n{0:<17}{1:<25}".format('Area','Country'))
    print("-------------------------------------------------")
    i =-1
    while i < 10:
        i +=1
        numA, nameA = b[i]
        print("{0:<17.2f}{1:<25}".format(int(numA),nameA),sep='\t')

# file output function
def oFile(oName,inp):
    name = oName+'.txt'
    out = open(name,'w')
    for line in inp:
        l = str(line)
        a,b = l.split(",")
        x,y = a.split("(")
        z = b.split("'")
        out.write(y+","+z[1]+'\n')
    out.close()
















