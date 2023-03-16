# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# Examples
#
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    text = text.split()

    new_str = ''

    for char in text:
        if char.isalpha():
            new_str += char[1:]
            new_str += char[0]
            new_str += 'ay'
            new_str += ' '
        else:
            new_str += char
            new_str += ' '
    return new_str[:-1]


def pig_it2(text):
    text = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in text])


def pig_it3(text):
    return ' '.join([x[1:] + x[0] + 'ay' if x.isalpha() else x for x in text.split()])

def pig_it4(text):
    return ' '.join(map(lambda x: x[1:] + x[0] + 'ay' if x.isalpha() else x, text.split()))