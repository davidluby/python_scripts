# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:33:26 2022

@author: David Luby

# CS 410P - Program assignment 9P

# create modular program to:
    # intake matrix file
    # display matrix dimensions
    # print initial matrix
    # transpose matrix (flip columns and rows) in new matrix
    # multiply matricies
    # display new matrix
    # sentences for total participants to attend each presentation
    # find upper triangular matrix and:
        # pairs of presentations to avoid double booking
        # output pairs if three or more participants involved
"""

name = input('Input the file name:')
import numpy as np
# intake function
def intake(name):
    file = open(name)
    row = -1
    mat = []
    for lins in file:
        row +=1
        if row == 0:
            dims = lins.strip()
            a,b = dims.split(" ")
            y = int(a)
            x = int(b)
        else:
            col = -1
            rows = []
            mat.append(lins.strip().split())
    return(mat,y,x)
mat,x,y = intake(name)

# printing function
def printer(x,y,mat):
    if x == 0:
        print()
    else:
        print('\n',x,y,"\n")
        for lins in mat:
            for cols in lins:
                print(cols,end='\t')
            print()
printer(x,y,mat) # transpose print

import numpy as np
# transpose fucntion
def trans(x,y,M):
    matN = np.array(mat,dtype='int')
    mat1 = matN.transpose()
    return(matN,mat1)
mat1,mat2 = trans(x,y,mat)
#printer(y,x,mat2) #transpose print

# product function
def prod(mat1,mat2):
    product = mat2.dot(mat1)
    return(product)
mat12 = prod(mat1,mat2)


def npPrint(x,mat12):
    print()
    for rows in mat12:
        for cols in rows:
            print(cols,end='\t')
        print() 
npPrint(x,mat12)

def diag(mat12):
    pres = []
    idx = []
    i = -1
    while i < y-1:
        i +=1
        if mat12[i][i] >= 3:
            pres.append(mat12[i][i])
            idx.append(i+1)
    return(pres,idx)
pres,idx = diag(mat12)

print('\nThere are ',y,'presentations and ',x,' participants')
print('These are who want to go to what:')
i = -1
for p in pres:
    i +=1
    print(p,'people want to go to presentation ',idx[i])
print()
i = -1
for p in pres:
    i +=1
    j = i
    while j < len(pres)-1:
        j +=1
        if p >3 and pres[j] >3:
            print('Do not schedule',idx[i],'and',idx[j],'since there will ' 
                  'be more than three participants attending each presentation')
            
            

pNums = []
for nums in pres:
    pNums.append(str(nums))
    
import matplotlib.pyplot as plt
plt.bar(idx,pres)
plt.xlabel('Presentation')
plt.ylabel('Participants')
plt.xticks()
plt.title('Participants Interested in Presentations')

    
    
    
    
    
    
