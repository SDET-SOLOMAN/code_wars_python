# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).

# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]

def count_sheeps(sheep):
    sheep_counter = 0
    for num in sheep:
        if num:
            sheep_counter += 1
    return sheep_counter


def count_sheeps2(sheep):
    return sheep.count(True)

# just some more complicated = fun solutions
from functools import reduce
def count_sheeps3(sheep):
    return reduce(lambda x, y: x + y, (1 for x in sheep if x)) if True in sheep else 0

def count_sheeps4(sheep):
    return sum(x for x in sheep if x)

count_sheep = lambda s: len([x for x in s if x])


from functools import reduce

count_sheeps5 = lambda baaaa: reduce(lambda x, y: x + y, [1 for x in baaaa if x]) if True in baaaa else 0