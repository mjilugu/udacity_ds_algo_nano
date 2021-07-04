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

telephone_numbers = []

for record in texts + calls:
    if record[0] not in telephone_numbers:
        telephone_numbers.append(record[0])
    if record[1] not in telephone_numbers:
        telephone_numbers.append(record[1])

count = len(telephone_numbers)
print(f"There are { count } different telephone numbers in the records.")
