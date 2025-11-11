# Task

# You will receive an array as parameter that contains 1 or more integers and a number n.

# Here is a little visualization of the process:

# Step 1: Split the array in two:

# [1, 2, 5, 7, 2, 3, 5, 7, 8]
#       /            \
# [1, 2, 5, 7]    [2, 3, 5, 7, 8]
# Step 2: Put the arrays on top of each other:

#    [1, 2, 5, 7]
# [2, 3, 5, 7, 8]
# Step 3: Add them together:

# [2, 4, 7, 12, 15]
# Repeat the above steps n times or until there is only one number left, and then return the array.

# Example

# Input: arr=[4, 2, 5, 3, 2, 5, 7], n=2


# Round 1
# -------
# step 1: [4, 2, 5]  [3, 2, 5, 7]

# step 2:    [4, 2, 5]
#         [3, 2, 5, 7]

# step 3: [3, 6, 7, 12]


# Round 2
# -------
# step 1: [3, 6]  [7, 12]

# step 2:  [3,  6]
#          [7, 12]

# step 3: [10, 18]


# Result: [10, 18]

def split_and_add(l, n):
    
    if len(l) <= 1 or n == 0:
        return l
    
    while n > 0 and len(l) > 1:
        
        long = len(l) // 2
        temp = [l[:long], l[long:]]
        
        inside1 = len(temp[0])
        inside2 = len(temp[1])
        
        if inside1 == inside2:
            l = [temp[0][t] + temp[1][t] for t in range(inside1)]
        else:
            l = [temp[1][0]] + [temp[0][t] + temp[1][t+1] for t in range(inside1)]
            
        n -= 1

    return l

# Alternative solution:
# def split_and_add(l, n):
#     for _ in range(n):
#         if len(l) <= 1:
#             break
#         mid = len(l) // 2
#         left = l[:mid]
#         right = l[mid:]
#         if len(left) < len(right):
#             left = [0] * (len(right) - len(left)) + left
#         l = [left[i] + right[i] for i in range(len(right))]
#     return l