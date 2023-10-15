# Write a program that outputs the top n elements from a list.
#
# Example:
#
# largest(2, [7,6,5,4,3,2,1])
# # => [6,7]

def largest(n, xs):
    if len(xs) < n or n == 0:
        return []
    return sorted(xs)[-n:]


def largest2(n, xs):
    return sorted(xs, reverse=True)[:n][::-1]
