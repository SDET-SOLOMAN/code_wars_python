# DESCRIPTION:

# Complete the method that takes a boolean value and return a
# "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"
    # return "Yes" if boolean else "No"


bool_to_word2 = lambda b: ["No", "Yes"][b]


bool_to_word3 = lambda x: "Yes" if x else "No"