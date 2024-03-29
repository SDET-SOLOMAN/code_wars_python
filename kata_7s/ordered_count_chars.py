# Count the number of occurrences of each character and return it as a (list of tuples) in order of appearance.
# For empty output return (an empty list).
#
# Consult the solution set-up for the exact data structure implementation depending on your language.
#
# Example:
#
# ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]


def ordered_count(inp):
    my_dict = {x: inp.count(x) for x in inp}
    return [(k, v) for k, v in my_dict.items()]


ordered_count2 = lambda inp: list({d: inp.count(d) for d in inp}.items())


def ordered_count3(inp):
    d = {
        k: inp.count(k) for k in inp
    }
    return list(d.items())