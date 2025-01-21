# Requirements
# The constructor should take an array as an argument, this will contain
# 3 integers of the form [width, length, height] from which the Block should be created.
#
# Define these methods:
#
# `get_width()` return the width of the `Block`
#
# `get_length()` return the length of the `Block`
#
# `get_height()` return the height of the `Block`
#
# `get_volume()` return the volume of the `Block`
#
# `get_surface_area()` return the surface area of the `Block`
# Examples
#     b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4`
#     and a height of `6`
#
#     b.get_width() -> return 2
#
#     b.get_length() -> return 4
#
#     b.get_height() -> return 6
#
#     b.get_volume() -> return 48
#
#     b.get_surface_area() -> return 88
# Note: no error checking is needed
#
# Any feedback would be much appreciated

from functools import reduce


class Block:
    def __init__(self, ar):
        self.ar = ar

    def mul(self, a, b):
        return a * b

    def get_width(self):
        return self.ar[0]

    def get_length(self):
        return self.ar[1]

    def get_height(self):
        return self.ar[2]

    def get_volume(self):
        return reduce(lambda x, y: x * y, self.ar)

    def get_surface_area(self):
        return 2 * (self.ar[0] * self.ar[1] + self.ar[1] * self.ar[2] + self.ar[2] * self.ar[0])