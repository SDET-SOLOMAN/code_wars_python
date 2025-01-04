# Can you find the needle in the haystack?
#
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
#
# After your function finds the needle it should return a message (as a string) that says:
#
# "found the needle at position " plus the index it found the needle, so:
#
# Example(Input --> Output)
#
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
# Note: In COBOL, it should return "found the needle at position 6"

def find_needle(haystack):
    return f"found the needle at position {[haystack.index(x) for x in haystack if x == 'needle'][0]}"

def find_needle2(haystack):
    return f"found the needle at position {haystack.index('needle')}"


def find_needle2(h):
    i = [i for i in range(len(h)) if h[i] == 'needle'][0]
    return f"found the needle at position {i}"