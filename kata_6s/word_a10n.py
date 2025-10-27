# The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing
# the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.
#
# Write a function that takes a string and turns any and all "words" (see below) within that string of length
# 4 or greater into an abbreviation, following these rules:
#
# A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen
# (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter, then the number of removed characters, then the
# last letter (eg. "elephant ride" => "e6t r2e").
# Example
#
#  input: "elephant-rides are really fun!"
#           ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
#  words (^):   "elephant" "rides" "are" "really" "fun"
#                 123456     123     1     1234     1
#  ignore short words:               X              X
#
#  abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
#  all non-word characters (*) remain in place
#                      "-"      " "    " "     " "     "!"
# output: "e6t-r3s are r4y fun!"

def abbreviate(s):
    res = ""
    word = ""

    for i, char in enumerate(s):

        if char.isalpha():
            word += char
            if i == len(s) - 1:
                l = len(word)
                if l > 3:
                    res += f"{word[0]}{l - 2}{word[-1]}"
                else:
                    res += word

        else:
            l = len(word)
            if l > 3:
                res += f"{word[0]}{l - 2}{word[-1]}"
            else:
                res += word
            res += char
            word = ""
    return res