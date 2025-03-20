# Write a simple parser that will parse and run Dead fish.
#
# Deadfish has 4 commands, each 1 character long:
#
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.


def parse(data):

    num = 0
    my_list = []

    for char in data:
        if char == 'i':
            num += 1
        elif char == "d":
            num -= 1
        elif char == 's':
            num **= 2
        else:
            if char == 'o':
                my_list.append(num)
    return my_list

print(parse("iiisdoso"))


def parse2(data):
    num = 0
    myArr = []

    def incriment():
        nonlocal num
        num += 1

    def minus():
        nonlocal num
        num -= 1

    def multi():
        nonlocal num
        num *= num

    def app():
        myArr.append(num)

    commands = {
        'i': incriment,
        'd': minus,
        's': multi,
        'o': app
    }

    for char in data:
        action = commands.get(char)
        if action:
            action()

    return myArr
