# Description
# You are a Fruit Ninja, your skill is cutting fruit. All the fruit will be cut in half by your knife. For example:
#
# [  "apple",     "pear",     "banana"  ]  --> ["app", "le", "pe", "ar", "ban", "ana"]
# As you see, all fruits are cut in half. You should pay attention to "apple": if you cannot cut a fruit into equal
# parts, then the first part will has a extra character.
#
# You should only cut the fruit, other things should not be cut, such as the "bomb":
#
# [  "apple",     "pear",     "banana",   "bomb"]  -->
# ["app", "le", "pe", "ar", "ban", "ana", "bomb"]
# The valid fruit names are preloaded for you as:
#
# FRUIT_NAMES
# Task
# Complete function cut_fruits that accepts argument fruits. Returns the result in accordance with the rules above.
#
# OK, that's all. I guess this is a 7kyu kata. If you agree, please rank it as 7kyu and vote very;-) If you think
# this kata is too easy or too hard, please shame me by rank it as you want and vote somewhat or none :[
#

cut = lambda x: [x[:len(x) // 2], x[len(x) // 2:]] if len(x) % 2 == 0 else [x[:(len(x) // 2) + 1],
                                                                            x[(len(x) // 2) + 1:]]


def cut_fruits(f):
    result = []

    for fruit in f:
        if fruit in FRUIT_NAMES:  # Keep certain words intact
            result.extend(cut(fruit))
        else:
            result.append(fruit)
    return result
