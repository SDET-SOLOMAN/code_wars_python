# Given a non-negative integer, return an array / a list of the individual digits in order.
#
# Examples:
#
# 123 => [1,2,3]
#
# 1 => [1]
#
# 8675309 => [8,6,7,5,3,0,9]

def digitize(n):
    return [int(x) for x in str(n)]


def digitize2(n):
    return list(map(lambda x: int(x), str(n)))


def digitize3(nn):
    n = []

    while nn >= 10:
        n.append(nn % 10)
        nn //= 10
    n.append(nn)
    return n[::-1]


def digitize4(n):
    my_d = {

    }

    counter = 0

    while n >= 10:
        my_d[counter] = n % 10
        n //= 10
        counter += 1
    my_d[counter] = n % 10

    new_l = [v for v in reversed(my_d.values())]
    return new_l
