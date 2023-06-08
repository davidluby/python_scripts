# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:38:37 2022

@author: David Luby

# CS 410P - Program assignment 6P

# model heat transfer on a 2d plate
    # create functions to:
        # take file as input w/ five conditions
        # print the plate temperatures from 0-99.99 (two decimals)
        # initialize the plate
        # calculate the plate temperatures for one iteration
        # check if the plate is stable (if i-1 resulted in a <1% change)
        
"""
# intake function

def read_data(filename):
    data = [1,2,3,4,5]
    intake = open(filename,'r')
    i = -1
    for lines in intake:
        i +=1
        data[i] = lines.strip() # why cant i do: float(lines.strip()) ?
        #data[i] = float(data[i]) # but can do it once its in a list?
    intake.close()
    
    cA = float(data[0])
    cB = float(data[1])
    t1 = float(data[2])
    t2 = float(data[3])
    tol = float(data[4])
    
    return(cA,cB,t1,t2,tol)

# plate initialization function
def initialize_plate(initialA, initialB):
    j = -1
    plate = []
    while j < 7:
        j +=1
        i = -1
        row = []
        if j < 4:
            while i < 5:
                i +=1
                if i < 3:
                    row.append(initialA)
                else:
                    row.append(initialB)
        else:
            while i < 5:
                i +=1
                if i < 3:
                    row.append(initialB)
                else:
                    row.append(initialA)
        plate.append(row)
    return(plate)


# print plate function
def print_plate(plateA, hc_A, hc_B, plate_count):
    print("\nPlate number ",plate_count)
    print("{0:^64.2f}".format(hc_A))
    i = -1
    while i < 7:
        i +=1
        print()
        if i == 4:
            print("{0:^5.2f}{1:^9.2f}{2:^9.2f}{3:^9.2f}{4:^9.2f}{5:^9.2f}"
                  "{6:^9.2f}{7:^5.2f}".format(hc_A,plateA[i][0],plateA[i][1],
                                  plateA[i][2],plateA[i][3],plateA[i][4],
                                  plateA[i][5],hc_B))
        else:
            print("{0:^5}{1:^9.2f}{2:^9.2f}{3:^9.2f}{4:^9.2f}{5:^9.2f}{6:^9.2f}"
                  "{7:^5}".format(" ",plateA[i][0],plateA[i][1],
                                  plateA[i][2],plateA[i][3],plateA[i][4],
                                  plateA[i][5]," "))
    print("{0:^64.2f}".format(hc_B))

    
# plate update function
def calculate_new_plate(plateA, hc_A, hc_B):
    nPlate = []
    for x in range(8):
        row = []
        for y in range(6):
            row.append(0)
        nPlate.append(row)
        
    i = -1
    while i < 7: # row
        i +=1
        j = -1
        while j < 5: # column
            j +=1
            if i == 0 and j == 0: # top left
                nPlate[i][j] = (plateA[i+1][j] +plateA[i][j+1] +2*hc_A) /4
            elif i == 0 and j == 5: # top right
                nPlate[i][j] = (plateA[i+1][j] +plateA[i][j-1] +hc_A +hc_B) /4 
            elif i == 7 and j == 0: # bottom left
                nPlate[i][j] = (plateA[i][j+1] +plateA[i-1][j] +hc_A +hc_B) /4  
            elif i == 7 and j == 5: # bottom right
                nPlate[i][j] = (plateA[i-1][j] +plateA[i][j-1] +2*hc_B) /4
                    
            elif i == 0 and 0 < j < 5: # top edge
                nPlate[i][j] = (plateA[i+1][j] +plateA[i][j-1] +plateA[i][j+1]
                                +hc_A) /4
            elif i == 7 and 0 < j < 5: # bottom edge
                nPlate[i][j] = (plateA[i][j-1] +plateA[i][j+1] +plateA[i-1][j]
                                +hc_B) /4
            elif j == 0 and 0 < i < 7: # left edge
                nPlate[i][j] = (plateA[i-1][j] +plateA[i+1][j] +plateA[i][j+1]
                                +hc_A) /4
            elif j == 5 and 0 < i < 7: # right edge
                nPlate[i][j] = (plateA[i+1][j] +plateA[i-1][j] +plateA[i][j-1]
                                +hc_B) /4
            
            elif (0 < i < 7) and (0 < j < 5): # interior
                    nPlate[i][j] = (plateA[i-1][j] +plateA[i][j+1]
                                    +plateA[i+1][j] +plateA[i][j-1]) /4            
    return(nPlate)

# stability function
def check_stable_state(plateA, plateB, stab):
    i = -1
    count = 0
    while i < 7: # row
        i +=1
        j = -1
        while j < 5: # column
            j +=1
            if (abs(plateA[i][j] -plateB[i][j])/plateA[i][j] < stab):
                count +=1
                
    if count == 48:
        done = True
    else:
        done = False

        i = -1
    while i < 7: # row
        i +=1
        j = -1
        while j < 5: # column
            j +=1
            plateA[i][j] = plateB[i][j]
    
    return(done)























