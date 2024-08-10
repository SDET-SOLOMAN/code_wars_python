# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot
# climb on the shelf directly above its head), according to the illustration:

def solution(start, finish):
    counter = 0
    cats = start

    while cats != finish:
        if cats + 3 <= finish:
            cats += 3
        elif cats + 1 <= finish:
            cats += 1
        counter += 1
    return counter
