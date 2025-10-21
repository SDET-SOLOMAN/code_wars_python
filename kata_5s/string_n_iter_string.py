# This kata is inspired by This Kata
#
# We have a string s
#
# We have a number n
#
# Here is a function that takes your string, concatenates the even-indexed chars to the front, odd-indexed chars to the back.
#
# Examples
#
# s = "Wow Example!"
# result = "WwEapeo xml!"
# s = "I'm Jomo Pipi"
# result = "ImJm ii' ooPp"
# The Task
#
# return the result of the string after applying the function to it n times.
#
# example where s = "qwertyuio" and n = 2:
#
# after 1 iteration  s = "qetuowryi"
# after 2 iterations s = "qtorieuwy"
# return "qtorieuwy"
# Note
#
# there's a lot of tests, big strings, and n is greater than a billion
#
# so be ready to optimize.
#
# after doing this: do its best friend!

def jumbled_string(s, n):
    re = []

    while n > 0:

        s, n = f"{s[::2]}{s[1::2]}", n - 1

        if s in re:
            return re[n % len(re)]

        re.append(s)

    return s