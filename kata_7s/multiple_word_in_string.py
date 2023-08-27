# You are to write a function that takes a string as its first parameter. This string will be a string of words.
#
# You are expected to then use the second parameter, which will be an integer,
# to find the corresponding word in the given string. The first word would be represented by 0.
#
# Once you have the located string you are finally going to multiply by it the third provided parameter,
# which will also be an integer. You are additionally required to add a hyphen in between each word.
#
# Example
#
# modify_multiply ("This is a string",3,5)

def modify_multiply(st, loc, num):
    return ((st.split()[loc] + "-") * num)[:-1]


modify_multiply2 = lambda words, pos, times: '-'.join(words.split()[pos] for num in range(1, times + 1))
