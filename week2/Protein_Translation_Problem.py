##################################
#
# Protein Translation Problem: Translate an RNA string into an amino acid string.
#     Input: An RNA string Pattern.
#     Output: The translation of Pattern into an amino acid string Peptide.
#
# Sample Input:
#    AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
#
# Sample Output:
#    MAMAPRTEINSTRING
#
################################## 

import week2

def main():
    f = open('input.txt', 'r')
    rna = f.readline().rstrip()
    f.close()

    sol = week2.translate_rna_to_amino_acid(rna)
    g = open('output.txt', 'w')
    g.write(sol + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
