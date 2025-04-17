# Let's create some scrolling text!
#
# Your task is to complete the function which takes a string, and returns an array with
# all possible rotations of the given string, in uppercase.
#
# Example
#
# scrollingText("codewars") should return:
#
# [ "CODEWARS",
#   "ODEWARSC",
#   "DEWARSCO",
#   "EWARSCOD",
#   "WARSCODE",
#   "ARSCODEW"
#   "RSCODEWA",
#   "SCODEWAR" ]
# Good luck!

def scrolling_text(text):
    text = text.upper()
    return [ text[i:] + text[:i] for i in range(len(text)) ]