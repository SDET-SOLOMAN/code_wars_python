# We need a function that can transform a number (integer) into a string.
#
# What ways of achieving this do you know?
#
# Examples (input --> output):
#
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

# not using int capsulation aka function
def number_to_string(num):
    if num == 0:
        return "0"

    sign = "" if num > 0 else "-"
    result = ""
    num = abs(num)

    while num > 0:
        digit = num % 10
        result = chr(48 + digit) + result
        num //= 10
    return sign + result

# simple solution
def number_to_string2(num):
    return str(num)