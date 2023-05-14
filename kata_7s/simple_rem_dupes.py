# Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.
#
# Example:
#
# For input: [3, 4, 4, 3, 6, 3]
#
# remove the 3 at index 0
# remove the 4 at index 1
# remove the 3 at index 3
# Expected output: [4, 6, 3]
#
# More examples can be found in the test cases.
#
# Good luck!

def solve(arr):
    my_l = []
    for char in range(len(arr)):
        if char < len(arr) - 1 and arr[char] not in arr[char + 1:]:
            my_l.append(arr[char])
        if char == len(arr) - 1 and arr[char] not in my_l:
            my_l.append(arr[char])
    return my_l


def solve2(arr):
    index = 0
    while index < len(arr):
        if arr.count(arr[index]) > 1:
            arr.pop(index)
            index -= 1
        index += 1
    return arr


solve3 = lambda arr: [num for index, num in enumerate(arr)
                     if num not in arr[index + 1:]]
