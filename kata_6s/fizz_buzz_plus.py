# There is a common problem given to interviewees in software, called FizzBuzz. It works as follows:
# for the numbers between 1 and 100, print "fizz" if it is a multiple of 3 and "buzz" if it is a mutiple of 5,
# else print the number itself.
#
# You are in an interview and they ask you to complete fizzbuzz (which can be done in a one-liner in a few langs)
# and you knock it out of the park.
#
# Task
# Surprised by your ability, the interviewer gives you a harder problem. Given a list of coprime numbers,
# (that is that the greatest common divisor of all the numbers = 1) and an equally sized list of words, compute
# its fizzbuzz representation up until the pattern of strings repeats itself.
#
# Notes:
#
# Your function should return a list/array, not print it.
# The list of numbers should start from 1.
# The strings are always concatenated from left to right in the appearance of the given list of words.
# The list of numbers may not always be sorted - just use the given order of the numbers.
# All numbers in the first array will always be coprime. This is a safe assumption for your program.
# The list stops where it does because if you were to filter the numbers out, the remaining strings
# would repeat after this point.
# Hint: What is the relation to the numbers given in the list and the length of the list?
#
# Example
# fizzbuzz_plusplus([2, 3, 5], ['fizz', 'buzz', 'bazz'])
# should return
#
# [1, 'fizz', 'buzz', 'fizz', 'bazz', 'fizzbuzz', 7, 'fizz', 'buzz', 'fizzbazz', 11, 'fizzbuzz', 13, 'fizz',
# 'buzzbazz', 'fizz', 17, 'fizzbuzz', 19, 'fizzbazz', 'buzz', 'fizz', 23, 'fizzbuzz', 'bazz', 'fizz', 'buzz', '
# fizz', 29 , 'fizzbuzzbazz']

from math import gcd
from functools import reduce


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_list(numbers):
    return reduce(lcm, numbers)


def fizzbuzz_plusplus(n, w):
    result = []
    lcm_val = lcm_list(n)

    for i in range(1, lcm_val + 1):
        word = ''
        for idx in range(len(n)):
            if i % n[idx] == 0:
                word += w[idx]
        if word == '':
            result.append(i)
        else:
            result.append(word)

    return result


from functools import reduce


def fizzbuzz_plusplus2(n, w):
    my_range = reduce(lambda a, b: a * b, n)
    re = []

    for i in range(1, my_range + 1):
        x = ""
        for k, v in zip(n, w):
            if not i % k:
                x = x + v
                print(x)
        re.append(x if x else i)
    return re