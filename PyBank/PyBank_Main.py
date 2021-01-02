# Import modules
import os
import csv

# Locate the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Setup variables
date = []
profit = []
total_months = 0
net_revenue = 0
change = 0
change_in_profit = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Calculate total months and net profit
        total_months += 1
        net_revenue = net_revenue + int(row[1])

        # # Add date to one list and add profit to a second with the same index
        date.append(row[0])
        profit.append(row[1])

    # Calculate change in profit and store it to a new list
    for x in range(1, len(date)):
        change = int(profit[x]) - int(profit[x-1])
        change_in_profit.append(change)
        

    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_revenue}")
    print(f"change = {change_in_profit}")



    # print(f"Average Change: ${average_change}")
    # print(f"Greatest Increase in Profits: ")
    # print(f"Greatest Decrease in Profits: ")