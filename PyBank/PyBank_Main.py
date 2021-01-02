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
change_in_profit = [0]

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

    # Calculate the average change in profit
    average_change = round(sum(change_in_profit)/len(change_in_profit), 2)

    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_revenue}")
    print(f"Average Change: ${average_change}")

    # Find max and min changes in profit
    max_profit = max(change_in_profit)
    min_profit = min(change_in_profit)

    for x in range(len(change_in_profit)):
        date_index = change_in_profit.index(max_profit)
        max_date = date[date_index]
    print(f"Greatest Increase in Profits: {max_date} ({max_profit})")

    for x in range(len(change_in_profit)):  
        date_index = change_in_profit.index(min_profit)
        min_date = date[date_index]
    print(f"Greatest Decrease in Profits: {min_date} ({min_profit})")
    