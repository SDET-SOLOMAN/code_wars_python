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