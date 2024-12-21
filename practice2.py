a = 0 == False
b = "1"

try:
    print(b / a)
except ZeroDivisionError:
    print("There is Zero")
finally:
    print("Hi")