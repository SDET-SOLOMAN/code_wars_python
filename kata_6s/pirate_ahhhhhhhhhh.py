# Pirates have notorious difficulty with enunciating. They tend to blur all the letters together
# and scream at people.
#
# At long last, we need a way to unscramble what these pirates are saying.
#
# Write a function that will accept a jumble of letters as well as a dictionary, and output
# a list of words that the pirate might have meant.
#
# For example:
#
# grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
# Should return ["sport", "ports"].
#
# Return matches in the same order as in the dictionary. Return an empty array if there are no matches.
#
# Good luck!

# using sorted = simple one line
grabscrab = lambda possible_words, said: [x for x in possible_words if sorted(x) == sorted(said)]


# using for loop and conditional logic:
def grabscrab2(said, possible_words):
    a = []
    k = True
    for word in possible_words:
        for char in word:
            if char not in said or word.count(char) > said.count(char) or len(word) < len(said):
                k = False
        if k:
            a.append(word)

        k = True
    return a