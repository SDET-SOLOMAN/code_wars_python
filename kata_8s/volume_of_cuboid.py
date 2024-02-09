# Bob needs a fast way to calculate the volume of a cuboid with
# three values: the length, width and height of the cuboid. Write a function to
# help Bob with this calculation.

import math

def get_volume_of_cuboid(l, w, h):
    return math.ceil(l * w * h)


from functools import reduce
def get_volume_of_cuboid2(*args):
    return reduce(lambda x, y: x * y, args)