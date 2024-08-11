def is_even(num):
    return True if num % 2 == 0 else False


def even_birth():
    return "Happy even birthday"


def odd_birth():
    return "Happy odd birthday"


def age(num):
    return even_birth() if is_even(num) else odd_birth()


print(age(34))
