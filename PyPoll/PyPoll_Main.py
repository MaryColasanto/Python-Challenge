# Import modules
import os
import csv

# Location of the csv file
csvpath = os.path.join ("Resources", "election_data.csv")

# Set Variables
vote_count = 0
candidates = []
candidate_votes = []

# Read the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    header = next(csvreader)

    for row in csvreader:
        
        # Count the votes
        vote_count += 1

        # Add candidates and their respective votes to separate lists
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes.append(0)


    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {vote_count}")
    print(f"candidates: {candidates}")
    print(f"candidate votes: {candidate_votes}")
