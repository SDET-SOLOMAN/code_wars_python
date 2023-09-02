# write me a function stringy that takes a size and returns a string of alternating 1s and 0s.
#
# the string should start with a 1.
#
# a string with size 6 should return :'101010'.
#
# with size 4 should return : '1010'.
#
# with size 12 should return : '101010101010'.
#
# The size will always be positive and will only use whole numbers.

stringy = lambda size: ''.join('10' for x in range(1, size + 1))[:size]

stringy2 = lambda x: "".join(str(num % 2) for num in range(1, x + 1))
