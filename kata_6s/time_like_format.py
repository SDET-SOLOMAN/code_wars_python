# Build up a method that takes a positive integer and formats it to a 'time - like' format.
#
# The method must raise an exception if its hour length is less than 3 digits and greater than 4.
#
# Examples:
#
# 800   --> '8:00'
# 1000  --> '10:00'
# 1451  --> '14:51'
# 3351  --> '33:51'
# 10000 --> raise an exception

def solution(hour):
    assert hour <= 99 or hour > 9999
    hour = str(hour)
    return f"{hour[:1]}:{hour[1:]}" if len(hour) < 4 else f"{hour[:2]}:{hour[2:]}"