import pyfiglet
from termcolor import colored

text = pyfiglet.figlet_format(input("What kind of text you would like"))
color = colored(text, color="blue")

print(color)

