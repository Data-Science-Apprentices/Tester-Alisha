# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 13:53:35 2025

@author: Alish
"""


# importing required packages and functions for the code

import pandas as pd
from assigntment_functions import start_of_day_dta, update_dta_numbers, bed_availability_calc

# start are day dta figures 
dta = {
       'medicine':{'Patients awaiting beds': 23}, 
       'psych': {'Patients awaiting beds': 9}, 
       'neuro': {'Patients awaiting beds':14}, 
       'cardiac':{'Patients awaiting beds': 9},
       'rho': {'Patients awaiting beds':3} 
       }

# calling the functions results in to this script

start_of_day_dta(dta)

# While loop to repeat the promgramme if confirmed at the end
while True:
    
    update_dta_df = update_dta_numbers(dta)
  
    # unfilled dictionary with current bed availability on the wards to be updated by the bed manager 
    print ("Following your visits to the wards how many beds available do you currently have and how many discharges or potential discharges do you have in each division")
    bed_availability = {
        'medicine':{'current beds': 0, 'potential discharges': 0, 'confirmed discharges':0 },
        'psych':{'current beds': 0, 'potential discharges': 0, 'confirmed discharges': 0 },
        'neuro' :{'current beds':0, 'potential discharges': 0, 'confirmed discharges': 0},
        'cardiac':{'current beds': 0, 'potential discharges': 0, 'confirmed discharges': 0},
        'rho':{'current beds': 0, 'potential discharges': 0, 'confirmed discharges': 0 }
        }

    # loop to allow the dictionary to be updated

    # calling the main key and it respective dictionaries to begin  the loop to update each key 
    for division, info in bed_availability.items(): 

        # f function used to call the division variable in to the print statement
        print(f"Enter data for {division.upper()}: ") 
     
        # calling the nested dictionary to update its key values
        for category in info: 
            while True:
                
                # try loop incase there is an error in the inputted figures
                try: 
                    # requesting  a figure in each discharge/bed availability category for the division listed at the start 
                    value = int(input(f" {category}: ")) # ensuring the input is converted to an interger to be utilised later
                    
                    # this line updates each divisions nested dictionaries values
                    bed_availability[division][category] = value
                    
                    # stops the try loop as it will repeat indefinitely if not in place. it the pushes python back to the for loop with division and info
                    break 
                
                except ValueError: # if a valid interger is not entered it requests an new value 
                     print("invalid input please enter a number")

    print(" Your current bed availability is: ")

    # converted the updated dictionary to a dataframe to allow further calculations
    bed_availability_df = pd.DataFrame(bed_availability) 
    print(bed_availability_df)



    print("Following your ward rounds your current bed state for each division is: \n")

    # calls the function that calculates how many patients you will have left in A+E
    bed_availability_calc(bed_availability_df, update_dta_df)
     
    # Ask's the user if they would like repeat the task of updating DTA and discharge numbers
    repeat = input("\n Would you like to update your DTA numbers and avalible beds again? yes or no :")
    
    # ends the programme if the user does not state yes or y
    if repeat != 'yes'or 'y':
        print("Exiting update system! Have a good day!")
        break

        
            
            
     