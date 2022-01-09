def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number in [0,1]:
        return number

    start = 0
    end = number // 2

    mid = (start + end) // 2

    while start < mid < end:
        if mid * mid == number:
            return mid
        elif mid * mid > number:
            end = mid
        else:
            start = mid
        mid = (start + end) // 2

    return mid

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (3 == sqrt(15)) else "Fail")