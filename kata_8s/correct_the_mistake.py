# Description:
# Character recognition software is widely used to digitise
# printed texts. Thus the texts can be edited, searched and stored on a computer.
#
# When documents (especially pretty old ones written with a
# typewriter), are digitised character recognition softwares often make mistakes.
#
# Your task is correct the errors in the digitised text.
# You only have to handle the following mistakes:
#
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

def correct(s):
    d = {
        "5": "S",
        "0": "O",
        "1": "I"
    }

    return "".join(d.get(x, x) for x in s)
    # return ''.join(dict.get(int(x)) if x.isdigit() else x for x in s)


def matcher(x):
    match x:
        case "5":
            return "S"
        case "0":
            return "O"
        case "1":
            return "I"
        case _:
            return x


correct2 = lambda n: "".join(matcher(x) for x in n)