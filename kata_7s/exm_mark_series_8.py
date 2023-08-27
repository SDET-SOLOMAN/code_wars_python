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


def remove2(string):
    new = ''.join(x for x in string if x != "!")

    return new + "!" * (len(string) - len(new))


def remove3(string):
    new = ''.join(x for x in string if x != "!")

    return new + "!" * string.count("!")


def remove4(string):
    new = ''.join(x for x in string if x != "!")

    c = len([1 for x in string if x == "!"])

    return new + ''.join(map(lambda x: "!", range(1, c + 1)))