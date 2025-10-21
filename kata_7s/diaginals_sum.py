# Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary).
#
# Example
#
# [   // 3x3 matrix
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
# ]
#
# // Should return 30: (1 + 5 + 9) + (3 + 5 + 7)

def sum_diagonals(m):
    if not m:
        return 0

    x = [len(x) for x in m][0]
    print(x)

    s = 0
    idx = 0

    for num in m:
        s += num[idx]
        s += num[x - idx - 1]
        idx += 1
    return s