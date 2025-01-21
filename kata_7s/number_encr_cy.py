# You will receive a string composed by English words, string. You will have to return a cyphered
# version of that string.
#
# The numbers corresponding to each letter are represented at the table below. Notice that
# different letters can share the same number. In those cases, one letter will be upper case
# and the other one lower case.
#
# 1	2	3	4	5	6	7	8	9	0
# Upper case	I	R	E	A	S	G	T	B		O
# Lower case	l	z	e	a	s	b	t		g	o
#
# Any character that is not at the table, does not change when cyphered.
#
# Examples
# Input: "Hello World". Output: "H3110 W0r1d"
# Input: "I am your father". Output: "1 4m y0ur f47h3r"
# Input: "I do not know what else I can test. Be cool. Good luck". Output:
# "1 d0 n07 kn0w wh47 3153 1 c4n 7357. 83 c001. 600d 1uck"

def cypher(s):
    d = {
        "I": 1,
        "l": 1,
        "R": 2,
        "z": 2,
        "E": 3,
        "e": 3,
        "A": 4,
        "a": 4,
        "S": 5,
        "s": 5,
        "G": 6,
        "b": 6,
        "T": 7,
        "t": 7,
        "B": 8,
        "g": 9,
        "O": 0,
        "o": 0
    }
    return "".join(str(d.get(x, x)) for x in s)