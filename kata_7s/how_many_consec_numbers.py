# Write a function that takes an array of unique integers and returns the minimum number of
# integers needed to make the values of the array consecutive from the lowest number to the highest number.
#
# Example
# [4, 8, 6] --> 2
# Because 5 and 7 need to be added to have [4, 5, 6, 7, 8]
#
# [-1, -5] --> 3
# Because -2, -3, -4 need to be added to have [-5, -4, -3, -2, -1]
#
# [1] --> 0
# []  --> 0

def consecutive3(arr):
    if not arr or len(arr) == 1:
        return 0
    n, m = min(arr), max(arr)
    return sum(1 for x in range(n, m + 1) if x not in arr)


def consecutive(arr):
    if not arr or len(arr) == 1:
        return 0
    n, m = min(arr), max(arr)
    missing = 0
    for num in range(n, m + 1):
        if num not in arr:
            missing += 1
    return missing


def consecutive2(arr):
    if len(arr) <= 1:
        return 0

    arr.sort()
    print(arr)

    m_min = arr[0]
    m_max = arr[-1]
    numbers = 0

    while m_min < m_max:

        m_min += 1

        if m_min not in arr:
            numbers += 1

    return numbers
