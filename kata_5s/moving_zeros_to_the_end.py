# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order
# of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    zero_count = lst.count(0)
    lst = [x for x in lst if x > 0]
    for n in range(zero_count):
        lst.append(0)
    return lst


def move_zeros2(lst):
    new = filter(lambda x: x != 0, lst)
    new_2 = filter(lambda x: x == 0, lst)
    return list(new) + list(new_2)


def move_zeros3(lst):
    new_num = []
    second_num = []
    for num in lst:
        if num != 0:
            new_num.append(num)
        else:
            second_num.append(0)
    new_num.extend(second_num)
    return new_num


def move_zeros4(lst):
    return [x for x in lst if x > 0] + ([0] * lst.count(0))


def move_zeros5(lst):
    lst_2 = list(filter(lambda x: x > 0, lst))
    while len(lst_2) < len(lst):
        lst_2.append(0)
    return lst_2


def move_zeros6(lst):
    for char in lst:
        if char == 0:
            lst.pop(lst.index(0))
            lst.append(0)
    return lst


move_zeros7 = lambda lst: sorted(lst, key=lambda x: x == 0)

move_zeros8 = lambda x: [num for num in x if num != 0] + [zero for zero in x if zero == 0]


def move_zeros9(lst):
    no_zeros = []
    zeros = []
    [no_zeros.append(x) if x != 0 else zeros.append(0) for x in lst]
    no_zeros.extend(zeros)
    return no_zeros
