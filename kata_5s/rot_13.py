# DESCRIPTION:
#
# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
#
# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.
#
# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.
#
# Test examples:
#
# "EBG13 rknzcyr." -> "ROT13 example."
#
# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"


from string import ascii_lowercase, ascii_uppercase
alpha = ascii_lowercase + ascii_lowercase + ascii_uppercase + ascii_uppercase


# simple lambda version
rot13_v1 = lambda word: ''.join(x if not x.isalpha() else alpha[alpha.index(x) + 13] for x in word)


def rot13_for_loop(message):
    new = ''
    for char in message:
        if not char.isalpha():
            new += char
        else:
            new += alpha[alpha.find(char) + 13]
    return new


def rot13(message):
    return "".join(alpha[alpha.index(x) + 13] if x.isalpha() else x for x in message)


def rot13_v2(message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    my_message = ""
    tem_index = 13
    for num in message:
        if num.lower() not in alphabet:
            my_message += num
        else:
            nums = alphabet.index(num.lower())
            if num.isupper():
                my_message += alphabet[nums + tem_index].upper()
            else:
                my_message += alphabet[nums + tem_index]
    return my_message
