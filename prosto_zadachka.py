def multi(x, y):
    return x * y


def another(x, y):
    b = multi(x, y)

    return b + b

print(another(5, 5))