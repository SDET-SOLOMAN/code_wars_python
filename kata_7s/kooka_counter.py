# The trick to counting kookaburras is to listen carefully
#
# The males sound like HaHaHa...
#
# The females sound like hahaha...
#
# And they always alternate male/female
#
# Examples
#
# ha = female => 1
# Ha = male => 1
# Haha = male + female => 2
# haHa = female + male => 2
# hahahahaha = female => 1
# hahahahahaHaHaHa = female + male => 2
# HaHaHahahaHaHa = male + female + male => 3


def kooka_counter(laughing):
    if not laughing:
        return 0
    in_here = None
    counter = 0
    for char in laughing:
        if char != 'a' and in_here != char:
            in_here = char
            counter += 1
    return counter
