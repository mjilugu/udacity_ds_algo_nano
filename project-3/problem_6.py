def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) < 1:
       return ()
    min = ints[0]
    max = ints[0]

    for n in ints:
       if n < min:
          min = n
       elif n > max:
          max = n

    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print(f"\nTest1: get_min_max({l})")
#(0, 9)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print(f"\nTest2: get_min_max([])")
#()
print ("Pass" if (() == get_min_max([])) else "Fail")

print(f"\nTest3: get_min_max([0])")
#(0, 0)
print ("Pass" if ((0,0) == get_min_max([0])) else "Fail")
