# Main script to evalute budget data for PyPoll
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

election_data_path = os.path.join(script_location, 'Resources', 'election_data.csv')
#print('You are going to open the file in the following path: ', budget_data_path)

with open(election_data_path) as election_csv:

    # CSV reader specifies delimiter and variable that holds contents
    election_data_reader = csv.reader(election_csv, delimiter=',')
    #print(election_data_reader)

    csv_header = next(election_data_reader)
    #print(f"CSV Header: {csv_header}")

    # Organize data array into three separate lists: voter ID, county, candidate
    election_data = []
    voterID = []
    county = []
    candidate = []
    

    for row in election_data_reader:
        #print(row)
        election_data.append(row)
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

