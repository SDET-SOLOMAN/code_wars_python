# Exclusive "or" (xor) Logical Operator
# Overview
# In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.)
# called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans.
# It then returns true if exactly one of the two expressions are true, false otherwise. For example:

def xor(a, b):
    return False if a == b else True


xor2 = lambda a, b: [True, False][a == b]


xor3 = lambda a, b: a != b