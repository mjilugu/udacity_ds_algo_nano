def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    idx = 0
    idx_0 = 0
    idx_2 = len(input_list) - 1

    while idx <= idx_2:
        if input_list[idx] == 0:
            if input_list[idx_0] != 0:
                input_list[idx],input_list[idx_0] = input_list[idx_0], input_list[idx]
            idx_0 += 1
            idx += 1
        elif input_list[idx] == 2:
            if input_list[idx_2] != 2:
                input_list[idx],input_list[idx_2] = input_list[idx_2], input_list[idx]
            idx_2 -= 1
        else:
            idx += 1
    
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

print(f"\nTest1: test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])")
#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

print(f"\nTest2: test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])")
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

print(f"\nTest3: test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])")
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])