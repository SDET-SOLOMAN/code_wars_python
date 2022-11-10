# Description:
#
# Move all exclamation marks to the end of the sentence
#
# Examples
#
# remove("Hi!") === "Hi!"
# remove("Hi! Hi!") === "Hi Hi!!"
# remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
# remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
# remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"

def remove(s):
    new_s = ''
    exm = ''
    for char in s:
        if char.isalpha() or char == " ":
            new_s += char
        else:
            exm += char
    return new_s + exm