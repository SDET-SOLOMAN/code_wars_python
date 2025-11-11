# In some countries of former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:

# 003111    #             3 = 1 + 1 + 1
# 813372    #     8 + 1 + 3 = 3 + 7 + 2
# 17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
# 56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
# Such tickets were either eaten after being used or collected for bragging rights.

# Your task is to write a funtion luck_check(str), which returns true/True if argument is string decimal representation of a lucky ticket number, or false/False for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.

def luck_check(st):
    
    if not st:
        raise ValueError("Ticket number cannot be empty")

    if not st.isdigit():
        raise ValueError("Ticket number must contain only digits")

    l = len(st)
    if l % 2 == 0:
        p1, p2 = st[:l//2], st[l//2:]
    else:
        p1, p2 = st[:l//2], st[l//2+1:]
    return sum(int(x) for x in p1) == sum(int(x) for x in p2)

# Examples of usage:
# luck_check("003111")    # True
# luck_check("813372")    # True
# luck_check("17935")     # True
# luck_check("56328116")  # True
# luck_check("123456")    # False
# luck_check("12345")     # False
# luck_check("")          # Raises ValueError       
# luck_check("12a45")     # Raises ValueError
# luck_check("12 45")     # Raises ValueError

