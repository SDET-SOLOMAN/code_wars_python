# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls'
# comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    return ''.join([x for x in string_ if x not in 'aubioAEUIO'])


def disemvowel2(string_):
    return ''.join(x for x in string_ if x.lower() not in 'auioe')


disemvowel3 = lambda string_: ''.join(x for x in string_ if x.lower() not in 'auioe')


disemvowel4 = lambda word: ''.join(filter(lambda x: x.upper() not in "AUIOE", word))