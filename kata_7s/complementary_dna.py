# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries
# the "instructions" for the development and functioning of living organisms.
#
# If you want to know more: http://en.wikipedia.org/wiki/DNA
#
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# Your function receives one side of the DNA (string, except for Haskell); you need to
# return the other complementary side. DNA strand is never empty or there is no DNA at all
# (again, except for Haskell).
#
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
#
# Example: (input --> output)
#
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


def DNA_strand(dna):
    return_dna = ''
    for char in dna:
        if char == "A":
            return_dna += 'T'
        elif char == 'T':
            return_dna += 'A'
        elif char == 'G':
            return_dna += 'C'
        elif char == 'C':
            return_dna += 'G'
    return return_dna


def DNA_strand2(dna):
    return dna.replace("A", '1').replace("T","2").replace("C", '3')\
        .replace("G","4").replace("1","T").replace('2', 'A').replace("3","G")\
        .replace('4', 'C')


def DNA_strand3(dna):
    return dna.replace("A", '1').replace("T","2").replace("C", '3')\
        .replace("G","4").replace("1","T").replace('2', 'A').replace("3","G").replace('4', 'C')