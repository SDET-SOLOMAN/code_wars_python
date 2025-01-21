# Color Ghost
# Create a class Ghost
#
# Ghost objects are instantiated without any arguments.
#
# Ghost objects are given a random color attribute of "white" or
# "yellow" or "purple" or "red" when instantiated
#
# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"

from random import randint, choice

class Ghost(object):
    def __init__(self):
        self.colors = ['red', 'white', 'purple', 'red', 'yellow']
        self.color = choice(self.colors)

class Ghost2(object):
    def __init__(self):
        self.colors = ['red', 'white', 'purple', 'red', 'yellow']
        self.color = self.colors[randint(0, len(self.colors) - 1)]