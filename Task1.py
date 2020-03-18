"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# UNDERSTAND INPUTS
# get all sent numbers from texts
# get all received numbers from texts
# get all sent numbers from calls
# get all received number from calls

# UNDERSTAND THE OUTPUTS
# get a list of all unique numbers
# count the list to get a final number

# CONSIDER SYSTEMATICALLY HOW A HUMAN SOLVES THE PROBLEM
# go through the list and make a list of new numbers
# each time a number comes up, compare it to the list
# if the number exists, ignore it
# if it is new, add it to the list
# initialize my_set
num_set = set()


def getData(data):
    for i in data:
        num_set.add(i[0])
        num_set.add(i[1])


getData(texts)
getData(calls)

print(f"There are {len(num_set)} different telephone numbers in the records.")


# def test():
#     print("Tests finished")


# test()
