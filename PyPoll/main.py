'''
This Python script will, given a dataset of election data in a csv file, calculate: 

    The total number of votes cast

    A complete list of candidates who received votes

    The percentage of votes each candidate won

    The total number of votes each candidate won

    The winner of the election based on popular vote

The dataset is composed of three columns: "Voter ID", "County", and "Candidate"     
'''

import os
import csv

# Store the relative file path. The example file is located in the Resources folder.
election_csv = os.path.join("Resources","election_data.csv")

# Initialize variables...
# To hold the total number of votes:
total_votes = 0
# A dictionary to hold the candidates and the number of votes they received:
votes_dict = {}

with open(election_csv) as csvFile:
    # Use the open command to read the csv file. This file has a header.
    csvReader = csv.reader(csvFile,delimiter=",")
    csvHeader = next(csvReader)

    # In the resource file, each row has 3 elements: ballot ID, county, and candidate. We only care about the candidate.
    for row in csvReader:
        # Increment the count of total votes.
        total_votes+=1
        candidate = row[2]
        # Check to see if the candidate is already in the dictionary.
        if candidate in votes_dict:
            # If yes, increment the candidate's value by 1.
            votes_dict[candidate]+=1
        else:
            votes_dict[candidate]=1

'''
Create a list to store the lines to print in the analysis.
The analysis should look like this:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

Add these lines to the list
'''
lines = ["Election Results",
         "-------------------------",
         "Total Votes: "+str(total_votes),
         "-------------------------"]

# Initialize a variable to hold the number of votes of the winner of the election.
winning_votes = 0

# Iterate through all candidates and check who got the most votes.
# While we're at it, we'll go ahead and add vote percentages/amounts to the analysis lines as well.
for candidate in votes_dict:
    if votes_dict[candidate] > winning_votes:
        winning_votes = votes_dict[candidate]
        winner = candidate
    percentage = str((votes_dict[candidate]/total_votes)*100)[0:5]
    line = '{}: {}% ({})'.format(candidate,percentage,votes_dict[candidate])
    lines.append(line)

# Add the last few lines for the analysis formatting.
lines+=["-------------------------",
        "Winner: "+winner,
        "-------------------------"]

# Store the relative file path for the new analysis text file. 
analysis_txt = os.path.join("analysis","election_analysis.txt")

# Print the analysis lines to the terminal and write them to a text file.
with open(analysis_txt,'w') as f:
    for line in lines:
        print(line)
        f.write(line)
        f.write('\n')
