# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4
# positive integers. No floats or non-positive integers will be passed.
#
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#
# [10, 343445353, 3453445, 3453545353453] should return 3453455.

def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]


def sum_two_smallest_numbers2(numbers):
    if not numbers or len(numbers) < 2:
        return 0
    numbers.sort()
    a, b = numbers[0], numbers[1]
    return a + b


# not using sort or sorted functions
def sum_two_smallest_numbers3(numbers):

    if not numbers or len(numbers) < 2:
        return 0

    numbers = [x for x in numbers if x > 0]

    my_min = numbers[0]

    for num in numbers:
        if num > 0 and num < my_min:
            my_min = num
    numbers.remove(my_min)

    my_min2 = numbers[0]

    for num in numbers:
        if num >= 0 and num < my_min2:
            my_min2 = num

    return my_min + my_min2

