# Task
#
# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).
#
# Input:
#
# If, you can read?
#
# Output:
#
# India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?
#
# Note:
#
# There is a preloaded dictionary that you can use, named NATO. It uses uppercase keys, e.g.
# NATO['A'] is "Alfa". See comments in the initial code to see how to access it in your language.
# The set of used punctuation is ,.!?.
# Punctuation should be kept in your return string, but spaces should not.
# Xray should not have a dash within.
# Every word and punctuation mark should be seperated by a space ' '.
# There should be no trailing whitespace

alpha = { 'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo',
       'F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliett',
       'K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar',
       'P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango',
       'U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee',
       'Z':'Zulu'
      }

def to_nato(words):
    words = words.replace(' ','').upper()
    return ' '.join([alpha[i] if i in alpha else i for i in words])  # NATO['A'] == 'Alfa', etc


def to_nato3(words: str) -> str:
    words = words.upper()

    a = " ".join(alpha[x] if x.isalpha() else x for x in words)

    return " ".join(x for x in a.split(" ") if len(x) > 0)


to_nato2 = lambda words: ' '.join(alpha.get(x.upper(), x) for x in words if x != " ")