# Please write a function that sums a list, but ignores any duplicate items in the list.
#
# For instance, for the list [3, 4, 3, 6] , the function should return 10.

def sum_no_duplicates(l):
    my_sum = 0

    for char in l:
        if l.count(char) == 1:
            my_sum += char
    return my_sum


def sum_no_duplicates2(l):
    return sum([x for x in l if l.count(x) == 1])


def sum_no_duplicates3(l):
    return sum(filter(lambda x: l.count(x) == 1, l))