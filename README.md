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

[Tutorial I used to further understand how indexing works.](https://codedestine.com/python-list-index-count-example/)[Message board that helped me understand how to index into a list from another list.] (https://www.reddit.com/r/learnpython/comments/12a452/checking_if_an_object_inside_a_list_meets_a/)


To write the output file, I specificed the path and used the open function. Using the file.write function, I added the same terminal output to the text file and then closed the file. 











## PyPoll ##


 
