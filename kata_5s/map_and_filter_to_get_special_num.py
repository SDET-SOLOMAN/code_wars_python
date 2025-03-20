# We
# have
# an
# integern,
# with a certain number of digitsk,
# d
# 1
# d
# 2
# …
# d
# k
# d
# 1
# ​
# d
# 2
# ​
# …d
# k
# ​
# .
#
# We
# have
# a
# function, f()
# that
# produces
# a
# certain
# number
# n
# 'from n, such that,f(n) ---> n'
#
# f
# (
#     n
# )
# =
# ±
# d
# 1
# ∣
# d
# 1
# −
# d
# 2
# ∣
# ±
# d
# 2
# ∣
# d
# 2
# −
# d
# 3
# ∣
# ±
# ⋯
# ±
# d
# k
# −
# 1
# ∣
# d
# k
# −
# 1
# −
# d
# k
# ∣
# +
# d
# k
# f(n) =±d
# 1
# ∣d
# 1
# ​
# −d
# 2
# ​
# ∣
# ​
# ±d
# 2
# ∣d
# 2
# ​
# −d
# 3
# ​
# ∣
# ​
# ±⋯±d
# k−1
# ∣d
# k−1
# ​
# −d
# k
# ​
# ∣
# ​
# +d
# k
# ​
#
# If
# the
# difference is such
# that,
# d
# k
# −
# 1
# −
# d
# k
# >
# 0
# d
# k−1
# ​
# −d
# k
# ​
# > 0, the
# operator
# will
# be - and on
# the
# other
# hand if the
# difference is such
# that:
# d
# k
# −
# 1
# −
# d
# k
# ≤
# 0
# d
# k−1
# ​
# −d
# k
# ​
# ≤0, the
# operator
# will
# be +.
#
# Let
# 's see an example with the number 186599.
#
# f
# (
#     186599
# )
# =
# 1
# ∣
# 1
# −
# 8
# ∣
# −
# 8
# ∣
# 8
# −
# 6
# ∣
# −
# 6
# ∣
# 6
# −
# 5
# ∣
# +
# 5
# ∣
# 5
# −
# 9
# ∣
# +
# 9
# ∣
# 9
# −
# 9
# ∣
# +
# 9
# =
# 1
# −
# 64
# −
# 6
# +
# 625
# +
# 1
# +
# 1
# =
# 566
# f(186599) = 1
# ∣1−8∣
# −8
# ∣8−6∣
# −6
# ∣6−5∣
# +5
# ∣5−9∣
# +9
# ∣9−9∣
# +9 = 1−64−6 + 625 + 1 + 1 = 566
# The
# number
# 100 is the
# first
# integer in having
# the
# value
# of
# the
# above
# function
# equals
# to
# 0, in other
# way
# f(100) = 0.
#
# f
# (
#     100
# )
# =
# −
# 1
# ∣
# 1
# −
# 0
# ∣
# +
# 0
# ∣
# 0
# −
# 0
# ∣
# +
# 0
# =
# −
# 1
# 1
# +
# 0
# 0
# +
# 0
# =
# −
# 1
# +
# 1
# +
# 0
# =
# 0
# f(100) =−1
# ∣1−0∣
# +0
# ∣0−0∣
# +0 =−1
# 1
# +0
# 0
# +0 =−1 + 1 + 0 = 0
# (Yes, we consider here that 00 is equals to 1, following the output that give most programming languages)
#
# The
# first
# terms
# of
# this
# special
# sequence
# of
# numbers
# are:
#
# 100, 101, 110, 121, 132, 143, 154, 165, ...
# The
# function
# prev_next()( in javascript: prevNext())will
# receive
# a
# certain
# integer
# n and will
# output
# the
# highest
# possible
# number
# of
# this
# sequence
# under
# n and the
# smallest
# possible
# number
# of
# this
# sequence
# higher
# than
# n.
#
# For
# example
#
# prev_next(150) == [143, 154]
# If
# a
# number is part
# of
# this
# sequence
# will
# output
# three
# values, istself and the
# next
# previous and next
# one:
#
# prev_next(154) == [143, 154, 165]
# If
# there
# are
# no
# numbers
# below
# the
# given
# number, the
# function
# will
# output
# the
# next
# number
# of
# the
# sequence.
#
# prev_next(99) == [100]
# prev_next(100) == [100, 101]
# Features
# of
# the
# random
# tests:
#
# Numbers
# of
# tests = 100
# n, such
# that, 100 ≤ n < 1000000

def prev_next(val):
    down = val - 1
    up = val + 1
    output = []

    if calc(val) == 0:
        output.append(val)

    while calc(down) != 0:
        down -= 1

    while calc(up) != 0:
        up += 1

    if calc(down) == 0 and down != 0:
        output.insert(0, down)

    if calc(up) == 0 and up != 0:
        output.append(up)

    return output


def calc(num):
    digits = [int(c) for c in str(num)]
    total = 0

    for idx in range(len(digits) - 1):
        difference = digits[idx] - digits[idx + 1]

        if difference > 0:
            total -= digits[idx] ** abs(difference)
        else:
            total += digits[idx] ** abs(difference)

    total += digits[-1]

    return total
