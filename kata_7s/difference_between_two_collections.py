# Find the difference between two collections. The difference means that either the character is present
# in one collection or it is present in other, but not in both. Return a sorted list with the difference.
#
# The collections can contain any character and can contain duplicates.
#
# Example
# A = [a, a, t, e, f, i, j]
#
# B = [t, g, g, i, k, f]
#
# difference = [a, e, g, j, k]

def diff(a, b):
    re = []
    [re.append(k) for k in set(a) if k not in b]
    [re.append(k) for k in set(b) if k not in a]

    return sorted(re)
