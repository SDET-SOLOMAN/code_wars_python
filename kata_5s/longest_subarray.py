# Longest Subarray with No Repeating Numbers Task: Given an array, return the longest contiguous subarray with
# unique values. Input: [7, 6, 52, 372, 7, 6, 52627, 22, 348, 2, 6, 5, 7, 6] Output: [52, 372, 7, 6, 52627, 22, 348, 2]
# function longestUniqueSubarray(arr) { }


def sliding_window(arr):

    seen = {}
    best_len = 0
    best_start = 0
    start = 0

    for i, num in enumerate(arr):

        if num in seen and seen[num] > start:
            start = seen[num] + 1
        seen[num] = i
        length = i - start + 1

        if length > best_len:
            best_len = length
            best_start = start
    return arr[best_start:best_start + best_len]

def brutik(arr):

    n = len(arr)
    best_l = 0
    best_start = 0

    for i, num in enumerate(arr):
        for j in range(i + 1, n):
            sub = arr[i:j + 1]
            if len(sub) == len(set(sub)) and len(sub) > best_l:
                best_l = len(sub)
                best_start = i
    return arr[best_start:best_start + best_l]


# sliding window
def subbik(nums):

    last = {}
    start = 0
    best_start = 0
    best_length = 0

    for i, num in enumerate(nums):
        if num in last and last[num] > start:
            start = last[num] + 1
        last[num] = i
        length = i - start + 1
        if length > best_length:
            best_length = length
            best_start = start
    return nums[best_start:best_start + best_length]


# brute force

def subbik2(nums):
    best_start = 0
    best_len = 0
    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            sub = nums[i:j + 1]
            if len(sub) == len(set(sub)) and len(sub) > best_len:
                best_len = len(sub)
                best_start = i
    return nums[best_start: best_start + best_len]



arr = [7, 6, 52, 372, 6, 7, 6, 52627, 22, 348, 2, 6, 5, 7, 6]
print(sliding_window(arr))
print(brutik(arr))
print(subbik(arr))
print(subbik2(arr))