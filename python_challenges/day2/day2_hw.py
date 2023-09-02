# Zeros not for Heros Numbers ending with zeros are boring. They might be fun in your world, but not here. Get rid of
# them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

def remove_zeros(num):
    if num == 0:
        return 0
    action = True
    while action:
        if (num % 10) == 0:
            num = num // 10
        else:
            action = False
    return num


# print(remove_zeros(100400005000010))


def znh_zeros_rec(n):
    if n == 0:
        return 0
    elif n % 10 == 0:
        return znh_zeros_rec(n // 10)
    return n


znh_zeros_rec(100400005000010)


# Digital root is the recursive sum of all the digits in a number.
# # Given n, take the sum of the digits of n.
# # If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# # This is only applicable to the natural numbers.
#
# # 16  -->  1 + 6 = 7
# # 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# # 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# # 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def dig_root(num):
    new_num = 0
    while num > 10:
        for n in str(num):
            new_num += int(n)
        num = new_num
        new_num = 0
    return num


print(dig_root(493193))
