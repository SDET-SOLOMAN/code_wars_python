# In his publication Liber Abaci Leonardo Bonacci, aka Fibonacci, posed a problem involving a population of idealized
# rabbits. These rabbits bred at a fixed rate, matured over the course of one month, had unlimited resources,
# and were immortal.
#
# Create a function that determines the number of pairs of mature rabbits after n months, beginning with one immature
# pair of these idealized rabbits that produce b pairs of offspring at the end of each month.
#
# To illustrate the problem, consider the following example:
#
# n = 5 months
# b = 3 births
# -> 19 mature rabbit pairs
# Month	Immature pairs	Mature pairs
# 0	1	0
# 1	0	1
# 2	3	1
# 3	3	4
# 4	12	7
# 5	21	19
# Hint
# Any Fibonacci number can be computed using the following equation: F(n) = F(n-1) + F(n-2)

def fib_rabbits(n, b):
    if n == 0:
        return 0
    elif n == 1 or b == 0:
        return 1
    immature_p = b
    mature_p = 1
    for num in range(3, n + 1):
        temp = immature_p
        immature_p = mature_p * b
        mature_p += temp
    return mature_p
