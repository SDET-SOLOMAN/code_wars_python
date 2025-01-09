# Write a function that takes a string of parentheses, and determines if the order of the parentheses
# is valid. The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

def valid_parentheses(string):
    # your code here

    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            try:
                stack.pop()
            except:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


def valid_parentheses2(a):
    s = 0
    for item in a:
        if item == '(':
            s += 1
        elif s:
            s -= 1
        else:
            return False
    return s == 0


def valid_parentheses3(x):
    while "()" in x:
        x = x.replace("()", "")
    return x == ""


def valid_parentheses4(p):
    l = []
    for char in p:
        if char == "(":
            l.append(char)
        else:
            try:
                l.pop()
            except:
                return False
    if not l:
        return True
    return False