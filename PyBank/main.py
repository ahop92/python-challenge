# Main script to evalute budget data for PyBank
#Importing necessary libraries for code operation

import os 
import inspect 
import csv
import numpy as np
from pathlib import Path

# Checking for the location of the script's working directory, re-directing to
# the location of the program and reading financial csv file into main program
#ref: https://stackoverflow.com/questions/50499/how-do-i-get-the-path-and-name-of-the-file-that-is-currently-executing
#ref: https://stackoverflow.com/questions/12201928/python-open-gives-filenotfounderror-ioerror-errno-2-no-such-file-or-directory

script_location = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_location)
#print('Your current working directory is ', os.listdir())

budget_data_path = os.path.join(script_location, 'Resources', 'budget_data.csv')
#print('You are going to open the file in the following path: ', budget_data_path)

with open(budget_data_path) as budget_csv:

    # CSV reader specifies delimiter and variable that holds contents
    budget_data_reader = csv.reader(budget_csv, delimiter=',')
    #print(budget_data_reader)

    #csv_header = next(budget_data_reader)
    #print(f"CSV Header: {csv_header}")

    # Organize data arrays into two separate lists: one for the date and one for profit/losses
    budget_data = []
    dates = []
    profit_losses = []
    row_index = 0

    for row in budget_data_reader:
        #print(row)
        budget_data.append(row)
        dates.append(row[0])
        profit_losses.append(row[1])
        
    # print(budget_data)
    # print(dates)
    # print(profit_losses)    
    


    
# Sum the instances of each cell in the 'Date' Column 
# to calculate the total number of months in the dataset


# Sum the the values in the 'Profit/Losses' column
# to determine the net total of Profit/Losses over the entire period 

# From one month to the next, calculte the change 
# and store the value in a new array; then, find the sum of that array

# Find the maximum value in the array that contains all of the calcualted changes
# to calculate the greatest increase in profits over the entire period. Determine the associated
# month as well. 

# Find the minimum value in the array that contains all of the calculated changes
# to calculate the greatest decrease in losses over the entire period. Determine the associated 
# month as well. 

