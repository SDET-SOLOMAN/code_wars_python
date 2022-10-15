# Convert number to reversed array of digits
#
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# 35231 => [1,3,2,5,3]
# 0 => [0]

def digitize(n):
    return [int(x) for x in str(n)[::-1]]


def digitize2(n):
    return map(int, str(n)[::-1])


def digitize3(n):
    new_num = []
    for x in str(n)[::-1]:
        new_num.append(int(x))
    return new_num


# without [::-1]

def reverser_str(n):
    new_str = ''
    index = -1
    my_len = -len(str(n))
    while index >= my_len:
        new_str += str(n)[index]
        index -= 1
    return new_str


def dig4(n):
    return [int(x) for x in reverser_str(n)]


print(dig4(987654321))
