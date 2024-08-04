# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
#
# Examples(Operator, value1, value2) --> output

# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

def basic_op(operator, value1, value2):
    my_opr = {
        "+": (value1 + value2),
        "-": (value1 - value2),
        "*": (value1 * value2),
        "/": (value1 / value2)
    }
    return my_opr.get(operator)

basic_op2 =  lambda o, v1, v2: {"+": v1 + v2, "-": v1 - v2, "*": v1 * v2, "/": v1 / v2}.get(o)


# using match

def basic_op(o, v1, v2):

    match o:
        case '+':
            return v1 + v2
        case '-':
            return v1 - v2
        case '*':
            return v1 * v2
        case '/':
            return v1 / v2
        case _:
            raise ValueError('Wrong Operator')