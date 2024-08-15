# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.
#
# Note: input will never be an empty string

def fake_bin(x):
    return ''.join("0" if int(num) < 5 else "1" for num in x)


def fake_bin2(n):
    return "".join(map(lambda x: "0" if int(x) < 5 else "1", n))