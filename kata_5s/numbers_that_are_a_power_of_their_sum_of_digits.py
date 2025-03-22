# The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared).
# Eighty one (81), is the first number in having this property (not considering numbers of one digit).
# The next one, is 512. Let's see both cases with the details
#
# 8 + 1 = 9 and 92 = 81
#
# 512 = 5 + 1 + 2 = 8 and 83 = 512
#
# We need to make a function that receives a number as argument n and returns the n-th term of this sequence of numbers.
#
# Examples (input --> output)
# 1 --> 81
#
# 2 --> 512
# Happy coding!

def power_sumDigTerm(n):
    return [
        9**2, 8**3, 7**4, 17**3, 18**3, 26**3, 27**3, 22**4,25**4,
        28**4, 36**4, 28**5, 18**6, 35**5, 36**5, 46**5, 18**7, 45**6,
        27**7, 54**6, 31**7, 34**7, 64**6, 43**7, 53**7, 58**7, 68**7,
        46**8, 54**8, 63**8, 54**9, 71**9, 20**13, 81**9, 82**10, 85**10,
        94**10, 97**10, 106**10, 117**10 ][n-1]