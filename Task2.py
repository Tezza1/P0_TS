"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# UNDERSTAND INPUTS
# get all sent numbers from calls
# get the time spent on a call

# UNDERSTAND THE OUTPUTS
# get the number that spent the longest time on a call

# CONSIDER SYSTEMATICALLY HOW A HUMAN SOLVES THE PROBLEM
# set the first number as the benchmark
# go through the list and if a call duration is the longer, set it as the benchmark
num = ''
duration = 0


def getData(data):
    num = data[0][0]
    duration = int(data[0][3])
    for i in data:
        if(int(i[3]) > duration):
            num = i[0]
            duration = int(i[3])
    print(f"{num} spent the longest time, {duration} seconds, on the phone during September 2016.")


getData(calls)


# def test():
#     print("Tests finished")


# test()
