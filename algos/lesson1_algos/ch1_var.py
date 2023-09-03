# variable assignment

# re-assign variables
a = 15
b = 20

# 1 f"a{b}" string
f"a = {b} b = {a}"
# 2 using a temp variable
temp = b

b = a

a = temp
# 3 using math, plus, minus, minus
a = a + b
b = a - b
a = a - b
print(a, b)


# 4 taking advantage of python's dynamic typing feature
a, b = b, a

