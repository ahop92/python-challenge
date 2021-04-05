# Main script to evalute budget data for PyBank
#Importing necessary libraries for code operation

import os 
import inspect 
import csv
import numpy as np
import statistics
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

    # Organize data array into two separate lists: one for the date and one for profit/losses
    budget_data = []
    dates = []
    profit_losses = []
    

    for row in budget_data_reader:
        #print(row)
        budget_data.append(row)
        dates.append(row[0])
        profit_losses.append(row[1])

# Eliminating the data titles from the raw data to simplify arithmetic analysis
profit_losses.pop(0)
dates.pop(0)

# Initializing variables for loops below
profit_float = []
profit_change = []

# Converting string data to float and storing in a new list
for value in profit_losses: 

    profit_float.append(float(value))


# From one month to the next, calculte the change in profit/losses
# and store the value in a new array
for value in profit_float: 
   
    nextvalueindex = profit_float.index(value) + 1 
    
    if nextvalueindex > len(profit_float) - 1:
        break 

    nextvalue = profit_float[nextvalueindex]
    profit_change.append(nextvalue - value)
    #print(profit_float[nextvalueindex])
    

# print(budget_data)
# print(dates)
# print(profit_float) 
# print(profit_change)

# Calculate the length of the dates array to identify the number of months
total_months = len(dates)

# Sum the the values in the 'Profit/Losses' column
# to determine the net total of Profit/Losses over the entire period 
nettotal_profit = sum(profit_float)

# Find the average change in profit/losses by finding the mean of the profit_change
# array established in the previous for loop
average_profitlosses = statistics.mean(profit_change)
# print(profit_change)
# print(sum_pchange)

greatest_increase = max(profit_change)
max_index = profit_change.index(greatest_increase)
max_date = dates[max_index + 1]
greatest_decrease = min(profit_change)
min_index = profit_change.index(greatest_decrease)
min_date = dates[min_index + 1]

# Formatting the values as strings with corresponding currency notation
# ref: https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python 

total_months_str = str(total_months)
nettotal_profit_str = "${:,.2f}".format(nettotal_profit)
average_profitlosses_str = "${:,.2f}".format(round(average_profitlosses, 2))
greatest_increase_str = "${:,.2f}".format(greatest_increase)
greatest_decrease_str = "${:,.2f}".format(greatest_decrease)
max_date_str = str(max_date)
min_date_str = str(min_date)

print("Total Months: " + total_months_str)
print("Net Total Profit/Losses: " + nettotal_profit_str)
print("Average Change in Profit/Losses: " + average_profitlosses_str)
print("Greatest Increase: " + max_date_str + " " + greatest_increase_str)
print("Greatest Decrease: " + min_date_str + " " + greatest_decrease_str)

 # Writing results to a textfile that is stored in the specified analysis folder 
 # Ref: https://stackoverflow.com/questions/5214578/print-string-to-text-file
 # Ref: https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
   
output_path = os.path.join(script_location, 'Analysis', 'PyBankOutput.txt')

with open(output_path, "w", newline='') as analysis_file:
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("-------------------------\n")
    analysis_file.write("Total Months: " + total_months_str + "\n")
    analysis_file.write("Net Total Profit/Losses: " + nettotal_profit_str + "\n")
    analysis_file.write("Average Change in Profit/Losses: " + average_profitlosses_str + "\n")
    analysis_file.write("Greatest Increase in Profits: " + max_date_str + " " + "(" + greatest_increase_str + ")" + "\n")
    analysis_file.write("Greatest Decrease in Profits: " + min_date_str + " " + "(" + greatest_decrease_str + ")" + "\n")




