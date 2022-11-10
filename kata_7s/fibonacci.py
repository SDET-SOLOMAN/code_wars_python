# Create function fib that returns n'th element of Fibonacci sequence (classic programming task).

def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    my_list = [0, 1, 1]
    a = 1
    b = 1
    for n in range(2, n + 1):
        c = a
        a = b + a
        b = c
        my_list.append(a)
    return my_list[n]