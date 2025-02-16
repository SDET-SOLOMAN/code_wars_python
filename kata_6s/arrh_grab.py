# Pirates have notorious difficulty with enunciating. They tend to blur all the
# letters together and scream at people.
#
# At long last, we need a way to unscramble what these pirates are saying.
#
# Write a function that will accept a jumble of letters as well as a dictionary,
# and output a list of words that the pirate might have meant.
#
# For example:
#
# grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
# Should return ["sport", "ports"].
#
# Return matches in the same order as in the dictionary. Return an empty array
# if there are no matches.
# Good luck!

def grabscrab(s, p):
    return [x for x in p if sorted(s) == sorted(x)]


d = lambda x: {k: x.count(k) for k in x}
def grabscrab2(s, p):
    s_count = d(s)
    re = []

    for word in p:
        word_count = d(word)

        if s_count == word_count:
            re.append(word)

    return re