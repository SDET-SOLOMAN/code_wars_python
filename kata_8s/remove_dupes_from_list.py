# Define a function that removes duplicates from an array of numbers and returns it as a result.
#
# The order of the sequence has to stay the same.


def distinct(seq):
    my_x = []
    for num in seq:
        if num not in my_x:
            my_x.append(num)
    return my_x


def distinct2(seq):
    n_l = []
    [n_l.append(x) if x not in n_l else x for x in seq]
    return n_l

distinct3 = lambda seq: list(dict.fromkeys(seq))

distinct4 = lambda seq: list(sorted(set(seq), key=seq.index))