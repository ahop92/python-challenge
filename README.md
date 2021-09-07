# Voter Demographics and Bank Financial Analysis

## Background 

Two scripts were developed to evaluate different pools of information: corporate banking data and election data. The raw data in both cases was housed by CSV excel files. The goal was to develop indidivual python scripts that evaluate each set of data and offer a high level analysis that is output to a text file.

### Code Functionality

Both scripts change the present working directory to the location of the main script so that relative pathways can be employed to import the raw data.

### PyBank

The banking python script imports the data and stores the temporal information and financial infomration in separate lists. Using the raw data, the total profit and number of months were calculated. Additionally, the change in profit/losses was calculated from month to month and that information was stored in a new array. Using this new data, the average change in profit/loss, the greatest increase in profits, and greatest decrease in profit/loss was determined. 


### PyPoll 

The election python script imports the raw data and stores each value from the voter ID, county, and selected candidate in respective lists/arrays. Array length was the primary vehicle for determining different metrics, for instance the total number of votes. To identify the number of votes that each specific candidate received, the voter IDs associated with a vote per candidate were stored in new lists. The length of each voter ID list per candidate was then used to identify the number of votes they received. Lastly, the candidate voter ID list that had the greatest length was identified as the winner of the election. 


### Results 

For both scripts, the results were output to .txt files and saved to 'Analysis' folders that can be found in both the PyBank and PyPoll directories. 

