# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:
#
# name + " plays banjo"
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    s = [" plays banjo", " does not play banjo"]

    return name + s[name[0].lower() != 'r']


def are_you_playing_banjo2(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"
