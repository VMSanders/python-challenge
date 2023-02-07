'''
This Python script is meant to analyze financial records in the form of a csv file composed of two columns: "Date" and "Profit/Losses".

This script will calculate, print, and export a text file with:

    The total number of months included in the dataset

    The net total amount of "Profit/Losses" over the entire period

    The changes in "Profit/Losses" over the entire period, and then the average of those changes

    The greatest increase in profits (date and amount) over the entire period

    The greatest decrease in profits (date and amount) over the entire period
'''

import os
import csv

# Store the relative file path. The example file is located in the Resources folder.
budget_csv = os.path.join("Resources","budget_data.csv")

# Initialize a bunch of variables...
# To hold the total number of months:
total_months = 0
# To hold the net total of profit/loss:
net_total = 0
# To hold the individual dates and profits since I don't know how to figure out the average in the csv reader. Instead, I'll use 2 lists, since they're ordered and friendly:
profit_values_list = []
dates_list = []

with open(budget_csv) as csvFile:
    # Use the open command to read the csv file. This file has a header.
    csvReader = csv.reader(csvFile,delimiter=",")
    csvHeader = next(csvReader)

    # In the resource file, each row has only 2 elements: the month, and the profit/loss that month.
    for row in csvReader:
        # Increment total_months counter.
        total_months+=1
        # Add current profit/loss to net_total counter.
        net_total+=float(row[1])
        # Add current date to list of dates.
        dates_list.append(row[0])
        # Add current profit/loss to list of profit values.
        profit_values_list.append(float(row[1]))
        
# Now we should have 2 lists (dates_list and profit_values_list) of the same length making up the columns of the resource dataset.
# Initialize variables...
# To hold the greatest increase and associated date:
greatest_increase = 0
increase_date = 0
# To hold the greatest decrease and associated date:
greatest_decrease = 0
decrease_date = 0
# To hold the total in changes:
total_change = 0

# Iterate through the lists to find the change in values.
for i in range(0,len(profit_values_list)-1):
    # Calculate the change in profit from current month to next month.
    change_in_profit = profit_values_list[i+1]-profit_values_list[i]
    # Add this change to the total_change counter.
    total_change += change_in_profit
    # Check to see if this change is the biggest increase (or decrease) so far. If so, overwrite the relevant variables.
    if change_in_profit > greatest_increase:
        greatest_increase = change_in_profit
        increase_date = dates_list[i+1]
    if change_in_profit < greatest_decrease:
        greatest_decrease = change_in_profit
        decrease_date = dates_list[i+1]

# Print the analysis to the terminal and write the same lines to a text file.
'''
The analysis format should look like this:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)


'''
# Store each line of the analysis as a string in a list.
lines = ["Financial Analysis",
         "----------------------------",
         "Total Months: "+str(total_months),
         "Total: $"+str(net_total),
         "Average Change: $"+str(total_change/total_months),
         "Greatest Increase in Profits: "+str(increase_date)+" ($"+str(int(greatest_increase))+")",
         "Greatest Decrease in Profits: "+str(decrease_date)+" ($"+str(int(greatest_decrease))+")"]

# Store the relative file path for the new analysis text file. 
analysis_txt = os.path.join("analysis","financial_analysis.txt")

with open(analysis_txt,'w') as f:
    for line in lines:
        print(line)
        f.write(line)
        f.write('\n')