# Your goal is to return multiplication table for number that is always an integer from 1 to 10.
#
# For example, a multiplication table (string) for number == 5 looks like below:
#
# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# 6 * 5 = 30
# 7 * 5 = 35
# 8 * 5 = 40
# 9 * 5 = 45
# 10 * 5 = 50
# P. S. You can use \n in string to jump to the next line.
#
# Note: newlines should be added between rows, but there should be no trailing newline at the end.
# If you're unsure about the format, look at the sample tests.

multi_table = lambda num: '\n'.join(f"{x} * {num} = {str(x * num)}" for x in range(1, 11))

# super long solution
def multi_table2(number):
    return f'1 * {number} = {number}\n2 * {number} = {number * 2}\n3 * {number} = {number * 3}\n4 * ' \
           f'{number} = {number * 4}\n5 * {number} = {number * 5}\n6 * {number} = {number * 6}\n7 * {number} ' \
           f'= {number * 7}\n8 * {number} = {number * 8}\n9 * {number} = {number * 9}\n10 * {number} = {number * 10}'


def multi_tabl4e(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))