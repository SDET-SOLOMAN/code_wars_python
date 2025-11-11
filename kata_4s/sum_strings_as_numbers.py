# Given the string representations of two integers, return the string representation of the sum of those integers.

# For example:

# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

# I have removed the use of BigInteger and BigDecimal in java

# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

from itertools import zip_longest

def sum_strings(x, y):
    
    if not x and not y: 
        return "0"
    if not x: 
        return y.lstrip("0") or "0"
    if not y: 
        return x.lstrip("0") or "0"
    
    carry = 0
    res = []
    
    for a, b in zip_longest(x[::-1], y[::-1], fillvalue="0"):
        s = ord(a) + ord(b) - 96 + carry
        res.append(chr(s % 
                       10 + 48))
        carry = s // 10
    if carry: 
        res.append("1")
    return ("".join(reversed(res))).lstrip("0") or "0"

# another solution
# def sum_strings(x, y):
#     max_len = max(len(x), len(y))
#     x = x.zfill(max_len)[::-1]
#     y = y.zfill(max_len)[::-1]
#     carry = 0
#     result = []
#     for i in range(max_len):
#         digit_sum = int(x[i]) + int(y[i]) + carry
#         result.append(str(digit_sum % 10))
#         carry = digit_sum // 10
#     if carry:
#         result.append(str(carry))
#     return ''.join(result[::-1]).lstrip('0') or '0'

x = "232".