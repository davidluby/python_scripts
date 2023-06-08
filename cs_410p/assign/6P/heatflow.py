# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:58:13 2022

@author: David luby

# CS 410P - Program assignment - 6P


"""
import heatflow_functions as h

def main():
    proceed = False
    while(not proceed):
        try:
            filename = input("Enter input file name:")
            hc_A, hc_B, initialA, initialB, stab = h.read_data(filename)
            proceed = True
        except:
            print("Invalid filename")
        
    print()
    print("Heater/Cooler Temperature A:", hc_A)
    print("Heater/Cooler Temperature B:", hc_B)
    print("Initial Temperature #1:", initialA)
    print("Initial Temperature #2:", initialB)
    print("Stability Criteria:", stab)
    
    plateA = h.initialize_plate(initialA, initialB) #set up initial plate
    plate_count = 0
    h.print_plate(plateA, hc_A, hc_B, plate_count) #print initial plate
    
    done = False
    while(not done):        #keep going until we are done
        plate_count += 1    #bump up plate count
        plateB = h.calculate_new_plate(plateA, hc_A, hc_B)  #compute new plate
        h.print_plate(plateB, hc_A, hc_B, plate_count)      #print new plate
        done = h.check_stable_state(plateA, plateB, stab)   #check stable state

main()
