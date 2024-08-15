# Write a small function that returns the values of an array that are not odd.
#
# All values in the array will be integers. Return the good values in the order they are given.

def no_odds(values):
    if not values:
        return []
    return list(filter(lambda x: x % 2 == 0, values))


def no_odds2(values):
    return [i for i in values if i % 2 == 0]
