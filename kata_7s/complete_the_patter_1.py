# Task:
#
# You have to write a function pattern which returns the following Pattern(See
# Pattern & Examples) upto n number of rows.
#
# Note:Returning the pattern is not the same as Printing the pattern.
# Rules/Note:
#
# If n < 1 then it should return "" i.e. empty string.
# There are no whitespaces in the pattern.


# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# 10101010101010101010
# 1111111111111111111111

def pattern(n):
    new_str = ''
    for num in range(1, n + 1):
        new_str += str(num) * num
        new_str += "\n"
    return new_str[:-1]


def pattern2(n):
    return '\n'.join(str(i) * i for i in range(1, n + 1))