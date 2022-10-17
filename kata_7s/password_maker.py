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