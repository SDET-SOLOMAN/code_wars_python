# The aim of this Kata is to write a function which will reverse the case of all consecutive duplicate letters
# in a string. That is, any letters that occur one after the other and are identical.
#
# If the duplicate letters are lowercase then they must be set to uppercase, and if they are uppercase then
# they need to be changed to lowercase.
#
# Examples:
#
# "puzzles" --> "puZZles"
# "massive" --> "maSSive"
# "LITTLE"  --> "LIttLE"
# "shhh"    --> "sHHH"
# Arguments passed will include only alphabetical letters A–Z or a–z.

def reverse(s):
    
    if not s:
        return s

    result = []

    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1]:
            result.append(s[i].swapcase())
        elif i < len(s) - 1 and s[i] == s[i + 1]:
            result.append(s[i].swapcase())
        else:
            result.append(s[i])

    return ''.join(result)