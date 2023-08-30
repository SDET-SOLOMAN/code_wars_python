# You certainly can tell which is the larger number between 210 and 215.
#
# But what about, say, 210 and 310? You know this one too.
#
# Things tend to get a bit more complicated with both different bases and exponents: which is larger between 39 and 56?
#
# Well, by now you have surely guessed that you have to build a function to compare powers, returning -1 if the first
# member is larger, 0 if they are equal, 1 otherwise; powers to compare will be provided in the [base, exponent] format:
#
# compare_powers([2,10],[2,15])==1
# compare_powers([2,10],[3,10])==1
# compare_powers([2,10],[2,10])==0
# compare_powers([3,9],[5,6])==-1
# compare_powers([7,7],[5,8])==-1
# Only positive integers will be tested, including bigger numbers - you are warned now, so be diligent try to implement
# an efficient solution not to drain too much on CW resources ;)!

def compare_powers(n1,n2):
    return -1 if n1[0] ** n1[1] > n2[0] ** n2[1] else 0 if n1[0] ** n1[1] == n2[0] ** n2[1] else 1