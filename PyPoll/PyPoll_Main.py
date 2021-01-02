# Import modules
import os
import csv

# Location of the csv file
csvpath = os.path.join ("Resources", "election_data.csv")

# Set Variables
vote_count = 0
candidates = []
candidate_votes = []
winner_votes = 0

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
    print("------------------------")

    # Calculate the percent votes for each candidate
    for x in range(len(candidate_votes)):
        percent_votes = round((candidate_votes[x]/vote_count)*100, 1)
        print(f"{candidates[x]}: {percent_votes}% ({candidate_votes[x]})")

        # Determine the winner
        if winner_votes < candidate_votes[x]:
            winner_votes = candidate_votes[x]
            winner = candidates[x]
    print("------------------------")
    print(f"Winner: {winner}")
    print("------------------------")

# Print results to a text file

analysis = os.path.join("Analysis", "PyPoll_Output.txt")
file= open(analysis, 'w')

file.write("Election Results")
file.write("\n------------------------")
file.write(f"\nTotal Votes: {vote_count}")
file.write("\n------------------------")
file.write(f"\n{candidates[0]}: {round((candidate_votes[0]/vote_count)*100, 3)}% ({candidate_votes[0]})")
file.write(f"\n{candidates[0]}: {round((candidate_votes[1]/vote_count)*100, 3)}% ({candidate_votes[1]})")
file.write(f"\n{candidates[0]}: {round((candidate_votes[2]/vote_count)*100, 3)}% ({candidate_votes[2]})")
file.write(f"\n{candidates[0]}: {round((candidate_votes[3]/vote_count)*100, 3)}% ({candidate_votes[3]})")
file.write("\n------------------------")
file.write(f"\nWinner: {winner}")
file.write("\n------------------------")

file.close()
