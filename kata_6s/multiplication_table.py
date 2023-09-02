# Your task, is to create N×N multiplication table, of size provided in parameter.
#
# For example, when given size is 3:
#
# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:
#
# [[1,2,3],[2,4,6],[3,6,9]]


# simple one line lambda
multiplication_table = lambda array: [[x * s for x in range(1, array + 1)] for s in range(1, array + 1)]


def multiplication_table2(size):
    my_list = [[j * i for j in range(1, size + 1)] for i in range(1, size + 1)]
    return my_list


# using a standard for loop:

def multiplication_table3(size):
    number = []
    for char in range(1, size + 1):
        n = []
        for char2 in range(1, size + 1):
            n.append(char2 * char)
        number.append(n)
    return number
