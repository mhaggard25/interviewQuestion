'''

SOLVED


We are running a catering service, and we'd like to run a report of how much money each of our customers have spent on us.

For example, we might have a list of transactions that looks like this:

transactions_1 = [
    ['customer_4', 'event_34', '7000'],  # customer_4 spent $7000 catering event_34
    ['customer_4', 'event_37', '6000'],
    ['customer_6', 'event_15', '3000'],
    ['customer_6', 'event_36', '7000'],
    ['customer_6', 'event_49', '4000'],
    ['customer_6', 'event_67', '6000'],
    ['customer_6', 'event_85', '6000']
]

We would like to know how many events each customer had catered, and how much they spent in total. Here, customer_4 had two events totaling 7000 + 6000 = $13000, and customer_6 had five events totaling $26000.

Write a function that takes a transaction list and outputs how many events each customer had and how much they spent in total in a suitable data structure.

All inputs:

transactions_1 = [
    ["customer_4", "event_34", "7000"],
    ["customer_4", "event_37", "6000"],
    ["customer_6", "event_15", "3000"],
    ["customer_6", "event_36", "7000"],
    ["customer_6", "event_49", "4000"],
    ["customer_6", "event_67", "6000"],
    ["customer_6", "event_85", "6000"]
]
transactions_2 = [
    ["customer_6", "event_49", "4000"],
    ["customer_6", "event_85", "6000"],
    ["customer_4", "event_34", "7000"],
    ["customer_6", "event_67", "6000"],
    ["customer_6", "event_15", "3000"],
    ["customer_6", "event_36", "7000"],
    ["customer_4", "event_37", "6000"]
]
transactions_3 = [
    ["customer_3", "event_70", "4000"],
    ["customer_3", "event_71", "6900"],
    ["customer_1", "event_40", "1600"],
    ["customer_6", "event_74", "6900"],
    ["customer_8", "event_75", "7400"],
    ["customer_1", "event_43", "6400"],
    ["customer_3", "event_52", "6300"],
    ["customer_6", "event_25", "3500"],
    ["customer_1", "event_62", "2500"]
]

All test cases (results be in any order):

report_sales(transactions_1) => customer_4: (2, 13000), customer_6: (5, 26000)
report_sales(transactions_2) => customer_4: (2, 13000), customer_6: (5, 26000)
report_sales(transactions_3) => customer_1: (3, 10500), customer_3: (3, 17200), customer_6: (2, 10400), customer_8: (1, 7400)

Complexity variables:
N = the number of transactions

'''
# define function
def numEventsCalculator(trans):
    
    # Create a new list to hold the customer information in the desired format.
    customerList =[]

    
    # iterate throught the list of transaction
    for item in trans:

        # Flag to help determine whether or not the customer exists in the list already
        foundCustomer = False  

        # Check to see if the current list is empty, if it is, fill it with the information in the first item of the argument list 
        if len(customerList) == 0:
            customerList.append([item[0], 1, int(item[2])])

        else:
            for newListItem in customerList:

                # determine if item[0] (or customer name) is in the new list. If yes, increment the number of events by 1 and sum the dollars spent
                if item[0] == newListItem[0]:
                    newListItem[1] = int(newListItem[1]) + 1
                    newListItem[2] = int(newListItem[2]) + int(item[2])
                    foundCustomer = True
                    break
            
            # If the customer is not found, add the customer to the list in the correct format.
            if not foundCustomer:
                customerList.append([item[0], 1, int(item[2])])


    return customerList
        
        

transactions_1 = [
  ["customer_4", "event_34", "7000"],
  ["customer_4", "event_37", "6000"],
  ["customer_6", "event_15", "3000"],
  ["customer_6", "event_36", "7000"],
  ["customer_6", "event_49", "4000"],
  ["customer_6", "event_67", "6000"],
  ["customer_6", "event_85", "6000"]
]
transactions_2 = [
  ["customer_6", "event_49", "4000"],
  ["customer_6", "event_85", "6000"],
  ["customer_4", "event_34", "7000"],
  ["customer_6", "event_67", "6000"],
  ["customer_6", "event_15", "3000"],
  ["customer_6", "event_36", "7000"],
  ["customer_4", "event_37", "6000"]
]
transactions_3 = [
  ["customer_3", "event_70", "4000"],
  ["customer_3", "event_71", "6900"],
  ["customer_1", "event_40", "1600"],
  ["customer_6", "event_74", "6900"],
  ["customer_8", "event_75", "7400"],
  ["customer_1", "event_43", "6400"],
  ["customer_3", "event_52", "6300"],
  ["customer_6", "event_25", "3500"],
  ["customer_1", "event_62", "2500"]
]

print('Transactions_1: ')
print(numEventsCalculator(transactions_1))

print('\nTransactions_2: ')
print(numEventsCalculator(transactions_2))

print('\nTransactions_3: ')
print(numEventsCalculator(transactions_3))
