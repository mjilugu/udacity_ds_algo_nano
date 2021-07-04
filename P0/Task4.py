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
possible_telemarketers = [ record[0] for record in calls ]

# remove callees
for record in calls:
    if record[1] in possible_telemarketers:
        possible_telemarketers.remove(record[1])

# remove sms senders and receivers
for record in texts:
    if record[0] in possible_telemarketers:
        possible_telemarketers.remove(record[0])
    if record[1] in possible_telemarketers:
        possible_telemarketers.remove(record[1])

uniq_possible_telemarketers = []
for entry in possible_telemarketers:
    if entry not in uniq_possible_telemarketers:
        uniq_possible_telemarketers.append(entry)


uniq_possible_telemarketers.sort()
print("These numbers could be telemarketers: ")
for entry in uniq_possible_telemarketers:
    print(entry)
