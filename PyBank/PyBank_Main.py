# Import modules
import os
import csv

# Locate the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Setup variables
total_months = 0
net_revenue = 0
change_in_profit = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    csv_header = next(csvreader)

    # Calculate total months and net revenue
    for row in csvreader:
        total_months += 1

        net_revenue = net_revenue + int(row[1])

    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_revenue}")



    # print(f"Average Change: ${average_change}")
    # print(f"Greatest Increase in Profits: ")
    # print(f"Greatest Decrease in Profits: ")