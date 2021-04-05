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
    
    # Store raw data into python arrays/lists in order to complete arithmetic analysis
    for row in election_data_reader:
        #print(row)
        election_data.append(row)
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

print(voterID[0])
print(county[0])
print(candidate[0])

# Getting the length of the voterID list to tabulate the total number of votes
total_votes = len(voterID)

#Looping through candidate data to identify each unique candidate and their assoicated number 
# of votes
# Ref: https://www.geeksforgeeks.org/python-get-unique-values-list/

unique_candidate = []
candidate0_voterIDs = [] #Khan
candidate1_voterIDs = [] #Correy
candidate2_voterIDs = [] #Li
candidate3_voterIDs = [] #O'Tooley

for name in candidate: 

    if name not in unique_candidate: 
        unique_candidate.append(name)


print(unique_candidate)

for name in candidate: 

    index = candidate.index(name)

    if name == unique_candidate[0]: 
        candidate0_voterIDs.append(voterID[index])
    
    elif name == unique_candidate[1]:
        candidate1_voterIDs.append(voterID[index])

    elif name == unique_candidate[2]:
        candidate2_voterIDs.append(voterID[index])

    else: 
        candidate3_voterIDs.append(voterID[index])


       
khan_votes = len(candidate0_voterIDs)
correy_votes = len(candidate1_voterIDs)
li_votes = len(candidate2_voterIDs)
tooley_votes = len(candidate3_voterIDs)

print("Total Votes: ", total_votes)
print("Khan Votes: ", khan_votes)
print("Correy Votes: ", correy_votes)
print("Li Votes: ", li_votes)
print("O'Tooley Votes: ", tooley_votes)


        