# This is a problem that involves adding numbers to items in a list. In a list you will have
# to add the item's remainder when divided by a given divisor to each item.
#
# For example if the item is 40 and the divisor is 3 you would have to add 1 since 40 minus
# the closest multiple of 3 which is 39 is 1. So the 40 in the list will become 41. You would have
# to return the modified list in this problem.
#
# For this problem you will receive a divisor called div as well as simple list of whole numbers called nums.
# Good luck and happy coding.


def solve(nums,div):
    return [x + x % div for x in nums]

solve2 = lambda nums, div: list(map(lambda x: (x % div) + x, nums))

# good old for loop
def solve3(nums, div):
    if not nums:
        return []

    new_nums = []

    for num in nums:
        digit = num % div
        new_nums.append(num + digit)
    return new_nums

#good old while loop
def solve4(nums, div):
    if not nums:
        return []

    new_nums = []
    my_index = 0
    len_nums = len(nums)

    while my_index < len_nums:
        temp = nums[my_index]
        digit = temp % div
        new_nums.append(temp + digit)
        my_index += 1
    return new_nums