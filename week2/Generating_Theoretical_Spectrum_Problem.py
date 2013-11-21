##################################
#
# Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
#   Input: An amino acid string Peptide.
#   Output: Cyclospectrum(Peptide).
#
# Sample Input:
#   LEQN
#
# Sample Output:
#   0 113 114 128 129 227 242 242 257 355 356 370 371 484
#
################################## 

import week2

def main():
    f = open('input.txt', 'r')
    pep = f.readline().rstrip()
    f.close()

    sol = week2.cyclospectrum(pep)
    
    sol_s = ""
    for val in sol:
        sol_s += str(val) + ' '
    
    g = open('output.txt', 'w')
    g.write(sol_s + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
