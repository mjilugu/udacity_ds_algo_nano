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
    
    return [int(n1), int(n2)]

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

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
