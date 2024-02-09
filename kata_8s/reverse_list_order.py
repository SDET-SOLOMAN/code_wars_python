# In this kata you will create a function that takes in a list and returns a list with the reverse order.
#
# Examples (Input -> Output)
#
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

def reverse_list(l):
    return l[::-1]

# more complicated solution
def reverse_list2(l):
    return [l[x] for x in range(-1, -len(l) -1, -1)]


def reverse_list3(l):
    l.sort()
    return l
