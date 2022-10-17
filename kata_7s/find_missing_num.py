# This question is a variation on the Arithmetic Progression kata
#
# The following was a question that I received during a technical interview for an entry
# level software developer position. I thought I'd post it here so that everyone could give it a go:
#
# You are given an unsorted array containing all the integers from 0 to 100 inclusively.
# \However, one number is missing. Write a function to find and return this number.
# What are the time and space complexities of your solution?

def missing_no(nums):
    if len(nums) < 1:
        return None
    my_range = list(range(0, sorted(nums)[-1] + 1))
    for char in my_range:
        if char not in nums:
            return char
    return 100


def missing_no2(nums):
    my_list = range(0, 101)
    my = [x for x in my_list if x not in nums]
    return my[0]