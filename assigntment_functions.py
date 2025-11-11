# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 17:41:03 2025

@author: Alish
"""

# import pandas packagae so that a data frame can be created later
import pandas as pd
# function to let the user know how many dta's they have started the day with 
def start_of_day_dta(dta):
    print("You have started your day with the following amount of patients in A+E awaiting beds in each division:" )
    dta_df = pd.DataFrame(dta) # converts the data frame dictionary in to a data frame
    print(dta_df)

        
 # function to allow the user to update their dta values       
def update_dta_numbers(dta):
    for key, values in dta.items(): # calls the dta dictionary to be updated using a loop
    
        # f funtion pulls values from the dicitonary
        # requesting input from bed manager if their data on required beds is up to date
        
        response = input(f"do you need to update your dta value for '{key}' ? yes/no... :")
        
        # if bed manager answers yes it requestes the update for each keys value
        # each key is a division in this dictionary 
        if response == 'yes' or 'y':
           new_value = int(input(f"enter the new value for '{key}' :"))
           # as the dictionary as a nested dictionary this calls the value inside the nested dictionary to be updated
           dta[key]['Patients awaiting beds'] = new_value
         # if response is no it informs the user it has not been updated  
         
        elif response == 'no':
            print(f"'{key}' not updated ")
            
            # if neither yes or no it alerts the user that their response is invalid and will not update the divisions value
        else:
             print("invalid resposne skipping to next division")       
    print("your updated dta numbers are:")
    # converts to a dataframe as will need to be used in a calculation later
    
    update_dta_df = pd.DataFrame(dta)
    
    # printing the updated dta dataframe
    
    print(update_dta_df)
    return update_dta_df


# function to calculate the remaining patients in A+E using the 2 dataframes created
def bed_availability_calc (bed_availability_df, update_dta_df):
    
    #  loop for all the divisions in the bed avalibility data frame
    # columns have been called 
    for division in bed_availability_df.columns:
        
        # calling the current beds row for the current division column being looped
        current = bed_availability_df.loc['current beds', division] 
        
        # calling the confirmed discharges row in the current division column being looped
        confirmed = bed_availability_df.loc['confirmed discharges', division]
        
        # calculating the exact number of confirmed bed spaces for each division
        total_beds = current + confirmed 
        
        # calls the dta dataframe to recall the amount of patients a+e for the same division in the bed avalibility dataframe
        awaiting = update_dta_df.loc['Patients awaiting beds', division] 
        
        # calculates how many patients from a+e that will still need to be place
        remaining = awaiting - total_beds
        
        # printing a summary of the above calculations for each division utilising the f function to pull in the required variables
        print (f"{division} you currently have {total_beds} beds to move patients in to and {remaining} continue to wait in A+E\n")
        
        # creates an alert and instruction for when 5 of more patients continue to wait for beds
        if remaining >= 5:
            print(f"Please contact {division}'s medical reps to complete extra board rounds to help clear A+E\n".upper())