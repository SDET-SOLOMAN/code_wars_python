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


def digitize(n):
    a = [int(x) for x in str(n)]
    a.reverse()
    return a


def digitize(n):
    a = list(map(lambda x: int(x), str(n)))
    a.reverse()
    return a


def digitize(n):
    nn = -1
    x = []
    while nn >= -len(str(n)):
        x.append(int(str(n)[nn]))
        nn -= 1
    return x


# without str convertion:

def digitize(n):
    my_list = []
    while n > 10:
        my_list.append(n % 10)  # takes the last number
        n = n // 10  # takes the all the numbers besides the last one
    my_list.append(n)
    new_list = []
    index = -1
    while index > - len(my_list):
        new_list.append(my_list[index])
        index -= 1
    return new_list
