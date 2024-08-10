# This kata is part of the collection Mary's Puzzle Books.
#
# Zero Terminated Sum
#
# Mary has another puzzle book, and it's up to you to help her out! This book is filled with
# zero-terminated substrings, and you have to find the substring with the largest sum of its digits.
# For example, one puzzle looks like this:
#
# "72102450111111090"
# Here, there are 4 different substrings: 721, 245, 111111, and 9. The sums of their digits are 10,
# 11, 6, and 9 respectively. Therefore, the substring with the largest sum of its digits is 245, and its sum is 11.
#
# Write a function largest_sum which takes a string and returns the maximum of the sums of the substrings.
# In the example above, your function should return 11.
#
# Notes:
#
# A substring can have length 0. For example, 123004560 has three substrings, and the middle one has length 0.
# All inputs will be valid strings of digits, and the last digit will always be 0.


def largest_sum(s):
    if not s:
        return 0

    calc = 0
    r_c = 0

    for char in s:
        if char != '0':
            calc += int(char)
        else:
            if calc > r_c:
                r_c = calc
            calc = 0
    return r_c


total = lambda xx: sum(int(x) for x in xx)


def largest_sum2(s):
    temp = ""
    max = 0

    for i, char in enumerate(s):
        if i <= len(s) - 1 and char != "0":
            temp += char
            if i == len(s) - 1 and temp:
                if max < total(temp):
                    max = total(temp)
        else:
            if max < total(temp):
                max = total(temp)
            temp = ""
    return max


largest_sum3 = lambda xx: max(sum(int(x) for x in n) for n in xx.split('0'))
