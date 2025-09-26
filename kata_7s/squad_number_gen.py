# At the start of each season, every player in a football team is assigned their own unique squad number. Due to superstition or their history certain numbers are more desirable than others.

# Write a function generateNumber() that takes two arguments, an array of the current squad numbers (squad) and the new player's desired number (n). If the new player's desired number is not already taken, return n, else if the desired number can be formed by adding two digits between 1 and 9, return the number formed by joining these two digits together. E.g. If 2 is taken, return 11 because 1 + 1 = 2. Otherwise return null.

# Note: Often there will be several different ways to form a replacement number. In these cases the number with lowest first digit should be given priority. E.g. If n = 15, but squad already contains 15, return 69, not 78.

def generate_number(s, n):
    
    s = set(s)
    
    if n not in s:
        return n
    
    for num in range(1, 10):
        for num2 in range(1, 10):
            x = int(f"{num}{num2}")
            print(x)
            if x not in s and num + num2 == n:
                return x