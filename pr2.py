def change(amount, coins):
    first_number = [0] * (amount + 1)
    first_number[0] = 1
    for char in coins:
        for num in range(char, amount + 1):
            first_number[num] += first_number[num - char]
    return first_number[amount]

print(change(10, [10]))

ss = "My name issS".index('is')
print(ss)