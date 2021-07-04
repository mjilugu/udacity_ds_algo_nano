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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
import re

callee_codes = []
uniq_callee_codes = []
callee_pattern = re.compile('^(140|\(\d+\)|[789]\d{3})(\d+|\d*\s\d+)')

for record in calls:
  if record[0].startswith('(080)'):
    callee_match = callee_pattern.match(record[1])
    area_code = callee_match.group(1).strip('() ')
    callee_codes.append(area_code)

for code in callee_codes:
  if code not in uniq_callee_codes:
    uniq_callee_codes.append(code)

uniq_callee_codes.sort()

print("The numbers called by people in Bangalore have codes:")
for entry in uniq_callee_codes:
  print(entry)

# Part B
bangalore_callee_codes = [ entry for entry in callee_codes if entry == '080' ]
percent_calls_to_bangalore = (len(bangalore_callee_codes) / len(callee_codes)) * 100

print(f"{percent_calls_to_bangalore:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
