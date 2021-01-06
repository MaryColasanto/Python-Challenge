# Python Challenge #

This exercise consists of two separate challenges, PyBank and PyPoll. Both require analyzing data in a csv file and reporting the output in both terminal and a text file using only python. 

## PyBank ##

The provided csv file contained two column: month and profit. This exercise asks you to calculate the total number of months in the dataset, the net profit, the average change in profit month to month, and report the month and amount for both greatest increase and greatest decrease in monthly profit. 

I utilized the os and csv modules to locate, open and read the csv file. I used the csv reader to skip the header and iterate over the rows. For each row I added 1 to the variable "total_months" to count the total months and added the value in column 1 to the variable "net_revenue" to count the to revenue over the time period covered by the dataset. During the same iteration I also added the month from column 0 to a list and added the profit from column 1 to a separate list. 

To calculate the change in profit, I found the difference between successive months and added them to a third list whose first value was 0 to account for the absence of a change in profit corresponding to the index of the corresponding date and profit. 










## PyPoll ##


 # https://codedestine.com/python-list-index-count-example/
 # https://www.reddit.com/r/learnpython/comments/12a452/checking_if_an_object_inside_a_list_meets_a/
