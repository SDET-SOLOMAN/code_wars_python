# Implement the function unique_in_order which takes as argument a sequence and returns a list
# of items without any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):

    if not sequence:
        return []

    if len(sequence) == 1:
        return [x for x in sequence]

    if len(sequence) == sequence.count(sequence[0]):
        if isinstance(sequence[0], int):
            return [sequence[0]]
        else:
            return [x for x in sequence[0]]

    new = []

    for char in range(len(sequence) - 1):

        if sequence[char] == sequence[char + 1]:
            continue
        else:
            new.append(sequence[char])
    if sequence[-1] != new[-1]:
        new.append(sequence[-1])

    return new