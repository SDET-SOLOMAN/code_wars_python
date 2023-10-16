# Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.
#
# Example:
#
# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"

def greet(name):
    if not name:
        return "Hello!"
    return f"Hello {name.capitalize()}!"


greet_2 = lambda x: f"Hello {x.title()}!"