# Define a function that removes duplicates from an array of numbers and returns it as a result.
#
# The order of the sequence has to stay the same.


def distinct(seq):
    my_x = []
    for num in seq:
        if num not in my_x:
            my_x.append(num)
    return my_x
