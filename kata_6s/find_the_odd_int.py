# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
#
# Examples
#
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

# complex lambda solution
find_it_lambda = lambda l: [x[0] for x in {k: l.count(k) for k in l}.items() if x[1] % 2 != 0][0]


def find_it(seq):
    return [x for x in seq if seq.count(x) % 2 != 0][0]


def find_it2(seq):
    my_dict = {}

    for num in seq:
        if my_dict.get(num):
            my_dict[num] += 1
        else:
            my_dict[num] = 1
    print(my_dict)

    for k, v in my_dict.items():
        if v % 2 != 0:
            return int(k)


def find_it3(seq):
    d = {
        k: seq.count(k) for k in seq
    }
    return [x[0] for x in d.items() if x[1] % 2 != 0][0]
