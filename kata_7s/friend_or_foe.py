# Make a program that filters a list of strings and returns a list with only your friends name in it.
#
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
# Otherwise, you can be sure he's not...
#
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
#
# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

def friend(x):
    return [char for char in x if len(char) == 4]


def friend2(x):
    return filter(lambda name: len(name) == 4, x)


def friend3(x):
    new_ = []
    for name in x:
        if len(name) == 4:
            new_.append(name)
    return new_


friend4 = lambda names: list(filter(lambda x: len(x) == 4, names))

friend5 = lambda names: [name for name in names if len(name) == 4]


len_meter = lambda x: True if len(x) == 4 else False
def friend4(s):
    if not s:
        return []
    return [x for x in s if len_meter(x)]


# another one

meter = lambda x: len(x) == 4

friend = lambda s: [x for x in s if meter(x)]