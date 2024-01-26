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


def sum_no_duplicates4(l):
    m = 0
    for i, c in enumerate(l):
        if isinstance(c, int):
            if c not in l[i + 1:] and c not in l[:i]:
                m += c
    return m


def sum_no_duplicates6(l):
    l_d = {

    }
    for char in l:
        if l_d.get(char):
            l_d[char] += 1
        else:
            l_d[char] = 1

    sum_d = 0

    for k, v in l_d.items():
        if v == 1:
            sum_d += int(k)
    return sum_d


sum_no_duplicates5 = lambda remove_dupes: sum(filter(lambda x: remove_dupes.count(x) == 1, remove_dupes))

# using enumerate
def sum_no_duplicates6(l):
    return sum([x for i, x in enumerate(l) if x not in l[:i] and x not in l[i + 1:]])

# using dictionary
def sum_no_duplicates7(l):
    return sum(k for k, v in {k:l.count(k) for k in l}.items() if v == 1)
