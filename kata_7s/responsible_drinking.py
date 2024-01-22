# Welcome to the Codewars Bar!
#
# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
#
# Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting
# how many glasses of water you should drink to not be hungover.


# "1 beer"  -->  "1 glass of water"
# because you drank one standard drink
#
# "1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"  -->  "10 glasses of water"
# because you drank ten standard drinks

def hydrate(drink_string):
    counter = 0
    for char in drink_string:
        if char.isdigit():
            counter += int(char)
    if counter > 1:
        return f"{counter} glasses of water"
    return f"{counter} glass of water"

# the best solution in my opinion:
def hydrate4(drink_string):
    num = sum(int(x) for x in drink_string if x.isdigit())
    word = "glass" if num <= 1 else "glasses"
    return f"{num} {word} of water"

def hydrate2(d):
    num_drinks = sum(int(x) for x in d if x.isdigit())
    return "{} {} of water".format(num_drinks, 'glass') if num_drinks == 1 else "{} {} of water".format(num_drinks,
                                                                                                        'glasses')

# using reduce instead of sum

from functools import reduce
def hydrate3(d):
    num_drinks = reduce(lambda x, y: x + y, (int(x) for x in d if x.isdigit()))
    return f"{num_drinks} glass of water" if num_drinks < 2 else f"{num_drinks} glasses of water"
