# Your task is to create a function called sum_arrays(), which takes two arrays consisting of integers, and returns the sum of those two arrays.

# The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' converted to an integer for this kata, meaning it would equal 329. The output should be an array of the sum in a similar fashion to the input (for example, if the sum is 341, you would return [3,4,1]). Examples are given below of what two arrays should return.

# [3,2,9],[1,2] --> [3,4,1]
# [4,7,3],[1,2,3] --> [5,9,6]
# [1],[5,7,6] --> [5,7,7]
# If both arrays are empty, return an empty array.

# In some cases, there will be an array containing a negative number as the first index in the array. In this case treat the whole number as a negative number. See below:

# [3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962

num_maker = lambda num: int("".join(map(str, num))) if num else 0
arr_maker = lambda n: ([0] if n == 0 
                       else ([-int(str(n)[1])] + [int(x) for x in str(n)[2:]] if n < 0 
                             else [int(x) for x in str(n)]))
def sum_arrays(a1, a2):
    
    if not a1 and not a2:
        return []
    return arr_maker(num_maker(a1) + num_maker(a2))
    
# Alternative solution:
# def sum_arrays(a1, a2):
#     if not a1 and not a2:
#         return []
#     n1 = int(''.join(map(str, a1))) if a1 else 0
#     n2 = int(''.join(map(str, a2))) if a2 else 0
#     total = n1 + n2
#     if total == 0:
#         return [0]
#     result = []
#     negative = total < 0
#     for digit in str(abs(total)):
#         result.append(int(digit))
#     if negative:
#         result[0] = -result[0]
#     return result