# Import modules
import os
import csv

# Location of the csv file
csvpath = os.path.join ("Resources", "election_data.csv")

# Set Variables
vote_count = 0

# Read the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    header = next(csvreader)

    for row in csvreader:
        
        # Count the votes
        vote_count += 1

    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {vote_count}")