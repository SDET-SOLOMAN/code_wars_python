# DESCRIPTION:

# Complete the method that takes a boolean value and return a
# "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"
    # return "Yes" if boolean else "No"


def boolean_to_string2(b):
    return ["False", "True"][b == True]

bool_to_word(True)