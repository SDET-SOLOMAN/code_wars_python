# Different sites have different password requirements.
#
# You have grown tired of having to think up new passwords to meet all the different rules,
# so you write a small piece of code to do all the thinking for you.
#
# Kata Task
# Return any valid password which matches the requirements.
#
# Input:
#
# length = password must be this length
# flagUpper = must (or must not) contain UPPERCASE alpha
# flagLower = must (or must not) contain lowercase alpha
# flagDigit = must (or must not) contain digit
# Notes
# Only alpha-numeric characters are permitted
# The same character cannot occur more than once in the password!
# All test cases guarantee that a valid password is possible

def make_password(l, fu, fl, fd):
    alpha = [chr(char) for char in range(ord('a'), ord('z') + 1)]
    re = ""
    temp = 0

    while len(re) < l:

        if fu:
            re += alpha[temp].upper()
        if fl:
            re += alpha[temp]
        if fd and temp < 10:
            re += str(temp)
        if temp >= 26:
            temp = 0
        temp += 1

    return re[:l]