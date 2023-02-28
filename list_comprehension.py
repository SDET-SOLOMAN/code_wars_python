nums = [1, 2, 3]
print([x ** 3 for x in nums])


name = ["james", 'monroe']
print([char[0:3].upper() for char in name])


print([num ** 3 for num in range(0, 5)])

my_nums = [1, 2, 3, 4, 5, 6, 7, 8]
print([str(x) for x in my_nums])

colors = ['yellow', 'black', 'white', 'purple']
print([color[0].upper() for color in colors])

print([x for x in my_nums if x % 2 == 0])
print(''.join([str(x) if x % 2 == 0 else 'odd' for x in my_nums]))

answer = [x for x in [1, 2, 3, 4] if x in [3, 4, 5, 6]]
answer2 = [x[::-1].lower() for x in ["Elie", "Tim", "Matt"]]

# Nested lists
#[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
print([['x' if x % 2 == 0 else "O" for x in range(0, 3)] for s in range(0,3)])

print([["*" for x in range(0,3)] for s in range(0, 3)])
