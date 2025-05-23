# In genetics 2 differents DNAs sequences can code for the same protein.
#
# This is due to the redundancy of the genetic code, in fact 2 different tri-nucleotide can code for the same
# amino-acid. For example the tri-nucleotide 'TTT' and the tri-nucleotide 'TTC' both code for the amino-acid 'F'.
# For more information you can take a look here.
#
# Your goal in this kata is to define if two differents DNAs sequences code for exactly the same protein.
# Your function take the 2 sequences you should compare. For some kind of simplicity here the sequences
# will respect the following rules:
#
# It is a full protein sequence beginning with a Start codon and finishing by an Stop codon
# It will only contain valid tri-nucleotide.
# The translation hash is available for you under a translation hash $codons [Ruby] or codons [Python and JavaScript].
#
# To better understand this kata you can take a look at this one, it can help you to start.
#

def code_for_same_protein(s1,s2):
    return all(codons[s1[num:num+3]] == codons[s2[num:num+3]] for num in range(0, len(s1), 3))