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

time_on_the_phone = {}

for record in calls:
    time_on_the_phone[record[0]] = time_on_the_phone.get(record[0], 0) + int(record[-1])
    time_on_the_phone[record[1]] = time_on_the_phone.get(record[1], 0) + int(record[-1])

n1 = max(time_on_the_phone,key=lambda item : time_on_the_phone[item]) 

print(f"{n1} spent the longest time, {time_on_the_phone[n1]} seconds, on the phone during September 2016.")