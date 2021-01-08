# Python Challenge #

This exercise consists of two separate challenges, PyBank and PyPoll. Both require analyzing data in a csv file and reporting the output in both terminal and a text file using only python. 

## PyBank ##

The provided csv file contained two column: month and profit. This exercise asks you to calculate the total number of months in the dataset, the net profit, the average change in profit month to month, and report the month and amount for both greatest increase and greatest decrease in monthly profit. 

### Total months, net revenue, and average change in profit ###

I utilized the os and csv modules to locate, open and read the csv file. I used the csv reader to skip the header and iterate over the rows. For each row I added one to the variable "total_months" to count the total months and added the value in column 1 to the variable "net_revenue" to count the to revenue over the time period covered by the dataset. During the same iteration I also added the month from column 0 to a list and added the profit from column 1 to a separate list. 

To calculate the change in profit, I found the difference between profit in successive months and added each value to a third list. The first value of this list is 0 to account for the absence of a change in profit corresponding to the index of the first entry in the dataset.

To determine the average change, I divided the sum of the profit change list by the number of entries minus one, which accounts for the lack of a value for the first month. I rounded this value to two decimal places using the round function.

### Maximum and minumum changes in profit ###

The next task was to find the maximum and minimum profits in the list of profit change between months. I used the max and min functions on this list to return the corresponding values. To report the corresponding date, I indexed into the change in profit list using the max profit value, and used that index value to return the corresponding month from the month list. I found the month corresponding to the minimum change in profit using the same code. 

[Tutorial I used to further understand how indexing works] (https://codedestine.com/python-list-index-count-example/)
[Message board that helped me understand how to index into a list from another list] (https://www.reddit.com/r/learnpython/comments/12a452/checking_if_an_object_inside_a_list_meets_a/)

### Reporting the results in a text file ###

To write the output file, I specificed the path and used the open function. Using the file.write function, I added the same terminal output to the text file and then closed the file. 

## PyPoll ##

The provided csv file contained three columns: voter ID, County, and Candidate. This exercise asks you to calculate the total number of votes, display for each candidate the percentage and total votes received, and to comment the election winners name. 

### Counting the votes ###

To determine the total number of votes needed, I used the csv reader to iterate over the rows and for each row I added one to the vote_count variable. I reported the final number at the total number of votes. I used an if statement to add each unique candidate's name to a list, (candidates) and made a second list (candiates_votes) with an initial value of zero for each candidate. I tallyed the candidate's votes by iterating over each row. For each row I used the value in the Candidate column to determine the index of the candidate in the candidates list, and then I added +1 to the corresponding index in the candidate_votes list. 

### Determine percentage of votes and the winner ###

The percentage of votes was determiened by looping through the candidates list and dividing each candidate's votes by teh total votes. I tried to use the round function to format the percentage with three decimal places, but for a second argument of 1-4 it would only return 1 decimal place, but at 5 it would return 5 decimal places. I deconstructed the code, but even on separate lines it gave the same error. Instead I used the format function that I don't enjoy do to the weird syntax and inability to use f strings in the print function. 

To determine the winner I used an if statement to compare the candidate_votes to the variable winner_votes, which was originally set to zero. If the candidate_votes were greater than the winner_votes, then the candidate_votes value became the new winner_votes value and the winner was the corresponding candidate in the candidate list. 

### Reporting the results in a text file ###

To write the output file, I specificed the path and used the open function. Using the file.write function, I added the same terminal output to the text file and then closed the file. 
