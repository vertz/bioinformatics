##################################
#
# Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
#   Input: A DNA string Text and an amino acid string Peptide.
#   Output: All substrings of Text encoding Peptide (if any such substrings exist).
#
# Sample Input:
#   ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
#   MA
#
# Sample Output:
#   ATGGCC
#   GGCCAT
#   ATGGCC
#
#   Note: The solution may contain repeated strings 
#   if the same string occurs more than once as a substring of Text and encodes Peptide.
#
################################## 

import week2

def main():
    f = open('input.txt', 'r')
    dna = f.readline().rstrip()
    pep = f.readline().rstrip()
    f.close()

    sol = week2.peptide_encoding(dna, pep)
    
    sol_s = ""
    for s in sol:
        sol_s += s + '\n'
    
    g = open('output.txt', 'w')
    g.write(sol_s + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
