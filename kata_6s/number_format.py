# Format any integer provided into a string with "," (commas) in the correct places.
#
# Example:
#
# For n = 100000 the function should return '100,000';
# For n = 5678545 the function should return '5,678,545';
# for n = -420902 the function should return '-420,902'.
#


def number_format(n):
    sign = "-" if n < 0 else ""
    s = str(abs(n))

    parts = []
    while s:
        parts.append(s[-3:])
        s = s[:-3]

    return sign + ",".join(reversed(parts))
