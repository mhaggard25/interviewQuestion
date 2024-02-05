# interviewQuestion

This is just a solution to the first interview question that I ever had. 

## Things that I learned during the interview. 
1. Slow down and work through the problem before ever writing code.
2. A working dumb solution is better that a solution that doesn't work.
3. The code can be simple. It doesn't have to be a masterpiece to function.

## The Problem
We are running a catering service, and we'd like to run a report of how much money each of our customers have spent on us.

For example, we might have a list of transactions that looks like this:
```
transactions_1 = [
    ['customer_4', 'event_34', '7000'],  # customer_4 spent $7000 catering event_34
    ['customer_4', 'event_37', '6000'],
    ['customer_6', 'event_15', '3000'],
    ['customer_6', 'event_36', '7000'],
    ['customer_6', 'event_49', '4000'],
    ['customer_6', 'event_67', '6000'],
    ['customer_6', 'event_85', '6000']
]
```
We would like to know how many events each customer had catered, and how much they spent in total. Here, customer_4 had two events totaling 7000 + 6000 = $13000, and customer_6 had five events totaling $26000.

Write a function that takes a transaction list and outputs how many events each customer had and how much they spent in total in a suitable data structure.

## My Solution
After defining the method, I created a new list called `customerList` to hold each customer's information. Then, I iterate through the list of transations that I was given as a method argument. I created a boolean flag called `foundCustomer` and set it to `False` so that in every iteration, I can determine whether or not a customer has been found in the `customerList`. I add the first customer to the list and set their event count to 1 and convert their dollars spent amount to an integer so that I can add to it easily later. 

Next, I iterate through `customerList` and check to see if `item[0]` (or the customer's name) is the same as `newListItem[0]` or the name of the customer in this iteration of the `customerList` loop. If it is, I increment the number of events by one, add this iterations dollar amount to the total dollar amount of this customer, set `foundCustomer` to `True`, and break out of the loop. 

Next, I check to see if `foundCustomer` is `True`. If is is not, I add the customer's information to my list in the correct format, initializing the event count to 1.

Finally, I return `customerList`

*note: the print statements at the end are just to show the output.*
