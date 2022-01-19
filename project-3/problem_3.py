def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    n1 = ""
    n2 = ""

    quicksort(input_list, reverse=True)

    i = 0

    while i < len(input_list):
        n1 = f"{n1}{input_list[i]}"
        if i + 1 < len(input_list):
            n2 = f"{n2}{input_list[i + 1]}"
        i = i + 2

    n1 = int(n1) if len(n1) else -1
    n2 = int(n2) if len(n2) else -1
    
    return [n1, n2]

def quicksort(arr, reverse=False):
    return _quicksort(arr, 0, len(arr) - 1, reverse)

def _quicksort(arr, start_index, end_index, reverse = False):
    if end_index <= start_index:
        return

    pivot_index = end_index
    pivot_item = arr[pivot_index]
    curr_index = start_index

    while curr_index < pivot_index:
        item = arr[curr_index]

        if ((item <= pivot_item) and not reverse) or ((item > pivot_item) and reverse):
            curr_index += 1
            continue

        arr[curr_index] = arr[pivot_index - 1]
        arr[pivot_index - 1] = pivot_item
        arr[pivot_index] = item
        pivot_index -= 1
    
    _quicksort(arr, start_index, pivot_index - 1, reverse)
    _quicksort(arr, pivot_index + 1, end_index, reverse)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

#
# Main
#
import random

print(f"\nTest1: test_function([[1, 2, 3, 4, 5], [542, 31]])")
#[542, 31]
test_function([[1, 2, 3, 4, 5], [542, 31]])

print(f"\nTest2: test_function([[4, 6, 2, 5, 9, 8], [964, 852]])")
#[964, 852]
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

print(f"\nTest3: test_function([[], [-1, -1]])")  # Empty array
#[-1, -1]
test_function([[], [-1, -1]])

print(f"\nTest3: test_function([[1], [1, -1]])")  # Single element array
#[1, -1]
test_function([[1], [1, -1]])

l = [2, 3, 2, 9, 5, 0, 8, 2, 7, 4, 5, 2, 8, 1, 7, 0, 7, 7, 7, 9, 2, 6, 0, 8, 8, 7, 1, 7, 0, 4, 6, 2, 1, 1, 7, 1, 0, 1, 6, 8, 1, 0, 0, 2, 9, 6, 0, 3, 3, 7, 8, 5, 2, 4, 0, 2, 1, 2, 9, 9, 0, 4, 2, 3, 7, 8, 2, 8, 1, 3, 4, 2, 8, 2, 5, 4, 2, 4, 2, 5, 1, 4, 0, 2, 8, 4, 4, 3, 0, 9, 9, 9, 2, 5, 7, 3, 2, 5, 0, 9]
a = [99999888887777766555544444333222222222211111000000, 99998888877777766555444443333222222222111110000000]
print(f"\nTest4: test_function([{l}, {a}])")   # Large array of ints btwn 0-9
#[99999888887777766555544444333222222222211111000000, 99998888877777766555444443333222222222111110000000]
test_function([l, a])
