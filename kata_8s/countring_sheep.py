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
