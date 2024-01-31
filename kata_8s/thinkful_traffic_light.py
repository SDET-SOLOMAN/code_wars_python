# You're writing code to control your town's traffic lights. You need a function to handle each change
# from green, to yellow, to red, and then to green again.
#
# Complete the function that takes a string as an argument representing the current state of the light and returns
# a string representing the state the light should change to.
#
# For example, when the input is green, output should be yellow.

def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    return 'green'


# using match / python Switch

def update_light2(current):
    match current:
        case "red":
            return "green"
        case "green":
            return "yellow"
        case "yellow":
            return "red"