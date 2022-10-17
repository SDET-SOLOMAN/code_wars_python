def positive_sum(arr):
    return sum(filter(lambda x: x > 0, arr))


# vs

def positive_sum2(arr):
    return sum(x for x in arr if x > 0)


# -----------


def divisible_by3(n, d):
    return list(filter(lambda x: not x % d, n))


# vs

def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]


# ----------------


def find_short(s):
    return len(sorted(s.split(), key=len)[0])


# vs

def find_short(s):
    list_of = s.split(" ")
    min_word = list_of[0]
    for words in list_of:
        if len(words) < len(min_word):
            min_word = words

    return len(min_word)


# --------

def filter_list(l):
    new_list = []
    for x in l:
        if type(x) == int:
            new_list.append(x)
    return new_list


# vs


def filter2(l):
    return list(filter(lambda x: isinstance(x, int), l))


# ---------------

def move(position=3, roll=6):
    return position + roll * 2


# vs


# solution 2 using lambdas
move_two = lambda p, r: p + r * 2


# --------------------


def no_space(x):
    return x.replace(" ", "")


def no_space2(x):
    new_string = ""
    for char in x:
        if char != " ":
            new_string += char
    return new_string


no_space3 = lambda x: ''.join(x.split())


# ---------------

def move_zeros(lst):
    zero_count = lst.count(0)
    lst = [x for x in lst if x > 0]
    for n in range(zero_count):
        lst.append(0)
    return lst


# vs


def move_zeros2(lst):
    new = filter(lambda x: x != 0, lst)
    new_2 = filter(lambda x: x == 0, lst)
    return list(new) + list(new_2)


# --------------------

def friend(x):
    return [char for char in x if len(char) == 4]


# vs

def friend2(x):
    return filter(lambda name: len(name) == 4, x)


# ---------


to_acronym3 = lambda word: "".join(list(map(lambda x: x[0].upper(), word.split())))


# vs

def to_acronym(inp):
    my_words = ''
    for char in inp.split():
        my_words += char[0]
    return my_words.upper()


def to_acronym2(input):
    # only call upper() once
    return ''.join(word[0] for word in input.split()).upper()

# -------------------
