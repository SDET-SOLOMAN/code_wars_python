# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


def find_outlier(integers):
    my_evens = list(filter(lambda x: x % 2 == 0, integers))
    my_odds = list(filter(lambda x: x % 2 != 0, integers))
    if len(my_evens) < len(my_odds):
        return my_evens[0]
    return my_odds[0]


def find_outlier2(integers):
    evens = []
    odds = []
    for num in integers:
        if num % 2 != 0:
            odds.append(num)
        else:
            evens.append(num)
    if len(evens) > len(odds):
        my_num = int(''.join(str(x) for x in odds))
        return my_num
    my_num = int(''.join(str(x) for x in evens))
    return my_num


def find_outlier3(integers):
    integers = list(set(integers))
    even = []
    odd = []
    [even.append(x) if x % 2 == 0 else odd.append(x) for x in integers]
    short, long = sorted([odd, even], key=len)
    return list(short)[0]


def find_outlier4(integers):
    odd = [x for x in integers if x % 2 != 0]
    even = [x for x in integers if x % 2 == 0]
    return [odd, even][len(odd) > len(even)][0]
