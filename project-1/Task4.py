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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# include all callers
possible_telemarketers = set([ record[0] for record in calls ])

# remove callees
for record in calls:
    possible_telemarketers = set(filter(lambda x: x not in [record[1]], possible_telemarketers))

# remove sms senders and receivers
for record in texts:
    possible_telemarketers = set(filter(lambda x: x not in [record[0], record[1]], possible_telemarketers))


possible_telemarketers = sorted(possible_telemarketers)
print("These numbers could be telemarketers: ")
for entry in possible_telemarketers:
    print(entry)
