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
