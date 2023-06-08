# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:43:19 2022

@author: David Luby

# set of function to be called on from main.py to:
    # read function to intake first file
    # update function to add three elemental properties from second file
    # print function to print the entire table
"""

# intial reading/establishment function
def read(elem):
    starter = []
    eFile = open(elem)
    alph = ['a','b','c','d']
    for lines in eFile:
        element = []
        i = -1
        a,b,c,d = lines.strip().split()
        element.append(a)
        element.append(b)
        element.append(int(round(float((c)))))
        element.append(float(d))
        starter.append(element)
    eFile.close()
    return(starter)

# table updating function
def update(elem,prop,pTable):
    nTab = []
    pFile = open(prop)
    for line in pFile:
        xTraDta = []
        name,a,b,c = line.strip().split()
        xTraDta.append(name)
        xTraDta.append(float(a))
        xTraDta.append(float(b))
        xTraDta.append(float(c))
        nTab.append(xTraDta)
    pFile.close()
    i = -1
    while i < len(pTable)-1:
        i +=1
        for row in nTab:
            if row[0] == pTable[i][0]:
                pTable[i].append(row[1])
                pTable[i].append(row[2])
                pTable[i].append(row[3])
    return(pTable)

# full periodic table printing function
def tPrint(pTable):
    print('{0:<15s}{1:<15s}{2:<15s}{3:<15s}{4:<15s}{5:<15s}{6:<15s}'.format(
        'Element','Symbol','Atomic Number','Atomic Weight','Melting Point',
        'Boiling Point','Density'))
    for row in pTable:
        print('{0:<15s}{1:<15s}{2:<15.2f}{3:<15.2f}{4:<15.2f}{5:<15.2f}'
              '{6:<15.2f}'.format(row[0],row[1],row[2],row[3],row[4],row[5],
                                  row[6]))

# element printing function
def ePrint(aNum,pTable):
    names = ['Element-','Symbol-','Atomic Number-','Atomic Weight',
         'Melting Point-','Boiling Point-','Density-']
    for rows in pTable:
        if rows[2] == aNum:
            i = -1
            print()
            for cols in rows:
                i +=1
                if cols == -9999:
                    cols = 'Unknown'
                    print(names[i],cols)
                else:
                    print(names[i],cols)
