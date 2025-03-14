# Given a string, turn each character into its ASCII character code and join them together to create a number - let's call this number total1:

# 'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
# Then replace any incidence of the number 7 with the number 1, and call this number 'total2':

# total1 = 656667
#               ^
# total2 = 656661
#               ^
# Then return the difference between the sum of the digits in total1 and total2:

#   (6 + 5 + 6 + 6 + 6 + 7)
# - (6 + 5 + 6 + 6 + 6 + 1)
# -------------------------
#                        6

order = lambda w: [str(ord(x)) for x in w]

def changer(x):
    n = ""
    for char in x:
        if char == "7":
            n += "1"
        else:
            n += char
    return n

def calc(w):
    
    first = order(w)
    second = [x if "7" not in x else changer(x) for x in first]
    f = list(map(int, first))
    s = list(map(int, second))
    
    return sum(f) - sum(s)