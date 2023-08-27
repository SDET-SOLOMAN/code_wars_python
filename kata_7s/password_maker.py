# One suggestion to build a satisfactory password is to start with a memorable phrase or
# sentence and make a password by extracting the first letter of each word.
#
# Even better is to replace some of those letters with numbers (e.g., the letter O can be replaced with the number 0):
#
# instead of including i or I put the number 1 in the password;
# instead of including o or O put the number 0 in the password;
# instead of including s or S put the number 5 in the password.
# Examples:
#
# "Give me liberty or give me death"  --> "Gml0gmd"
# "Keep Calm and Carry On"            --> "KCaC0"

def make_password(phrase):
    new_s = ''
    for char in phrase.split():
        letter = char[0].lower()
        if letter == 'i':
            new_s += str(1)
        elif letter == 'o':
            new_s += str(0)
        elif letter == 's':
            new_s += str(5)
        else:
            new_s += char[0]
    return new_s


def make_password2(phrase):
    d = {
        'i': '1',
        'I': '1',
        'o': '0',
        'O': '0',
        's': '5',
        'S': '5'
    }
    return ''.join(d[x[0]] if d.get(x[0]) else x[0] for x in phrase.split())



def make_password3(phrase):
    chars_replaced = {'i': "1", 'I':"1", 'o':"0", 'O':"0", 's':'5', 'S':"5"}
    new_phrase = ''
    try:
        for char in phrase.split():
            first = char[0]
            if first in chars_replaced:
                new_phrase += chars_replaced[first]
            else:
                new_phrase += first
        return new_phrase
    except (KeyError, ValueError, ZeroDivisionError) as err:# or can be left empty:
        print(err)
        return f"This item is not here {err}"