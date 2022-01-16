def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    n = len(input_list)
    high = n - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2

        if input_list[mid] == number:
            return mid 
        
        if input_list[low] <= input_list[mid]:                          # Left half is sorted 
            if number < input_list[mid] and number >= input_list[low]:  # Target number is in left half
                high = mid - 1
            else:
                low = mid + 1
        else:                                                           # Right half is sorted
            if number > input_list[mid] and number <= input_list[high]: # Target number is in right half
                low = mid + 1
            else:
                high = mid - 1

    return -1
        

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print(f"Test1: test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])")
#0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

print(f"Test1: test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])")
#5
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

print(f"Test1: test_function([[6, 7, 8, 1, 2, 3, 4], 8])")
#2
test_function([[6, 7, 8, 1, 2, 3, 4], 8])

print(f"Test1: test_function([[6, 7, 8, 1, 2, 3, 4], 1])")
#3
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

print(f"Test1: test_function([[6, 7, 8, 1, 2, 3, 4], 10])")
#-1
test_function([[6, 7, 8, 1, 2, 3, 4], 10])