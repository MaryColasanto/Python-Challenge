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

        # Add candidates to the list and create an empty list to add candidate votes
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes.append(0)

        # Add votes to the vote list 
        # https://codedestine.com/python-list-index-count-example/
        # https://www.reddit.com/r/learnpython/comments/12a452/checking_if_an_object_inside_a_list_meets_a/
        # Identify the candidate location in the list for each row
        candidate_index = candidates.index(row[2])
        # Add a vote for the candidate by adding 1 in same index in the vote list
        candidate_votes[candidate_index] +=1

    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {vote_count}")
    print(f"candidates: {candidates}")
    print(f"candidate votes: {candidate_votes}")
