# Write a function insert_dash(num) / insertDash(num) / InsertDash(int num) that will insert dashes ('-')
# between each two odd digits in num. For example: if num is 454793 the output should be 4547-9-3.
#
# Note that the number will always be non-negative (>= 0).

odd = lambda x: int(x) % 2 != 0


def insert_dash(num):
    num = str(num)

    return "".join(f"{x}-" if odd(x) and odd(num[i + 1]) else x for i, x in enumerate(num[:-1])) + num[-1]


def insert_dash2(num):
    num = str(num)
    s = ''
    for char in range(0, len(num)):

        try:
            if int(num[char]) % 2 != 0 and int(num[char + 1]) % 2 != 0:
                s += num[char] + "-"
            else:
                s += num[char]
        except IndexError as ER:
            s += num[-1]
    return s