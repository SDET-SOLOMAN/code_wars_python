# There are no explanations. You have to create the code that gives the following results in Python, Ruby, and Haskell:

# one_two_three(0) == [0, 0]
# one_two_three(1) == [1, 1]
# one_two_three(2) == [2, 11]
# one_two_three(3) == [3, 111]
# one_two_three(19) == [991, 1111111111111111111]

def one_two_three(n: int):
    
    if n == 0:
        return [0, 0]
    
   
    second_one = int("1" * n)
    first_one = ""
    count = 0
    while n > 9:
        first_one += "9"
        count += 1
        n -= 9
    first_one += str(n)
    return [int(first_one), second_one]