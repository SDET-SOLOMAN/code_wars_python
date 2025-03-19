# In this exercise, you will have to create a function named tiyFizzBuzz. This function will take
# on a string parameter and will return that string with some characters replaced, depending on the value:
#
# If a letter is a upper case consonants, replace that character with "Iron".
# If a letter is a lower case consonants or a non-alpha character, do nothing to that character
# If a letter is a upper case vowel, replace that character with "Iron Yard".
# If a letter is a lower case vowel, replace that character with "Yard".

normal = lambda x: "Iron" if x.isupper() else x
vowel = lambda x: "Iron Yard" if x.isupper() else "Yard"
sep = lambda x: vowel(x) if x.lower() in "aeiou" else normal(x)

def tiy_fizz_buzz(s):
    return "".join(sep(x) for x in s)
