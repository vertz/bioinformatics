##################################
#
# Solve the Local Alignment Problem.
#    Input: Two protein strings written in the single-letter amino acid alphabet.
#    Output: The maximum score of a local alignment of the strings, followed by a local alignment of these
#    strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty = 5
#    
# Sample Input:
#    MEANLY
#    PENALTY
#    
# Sample Output:
#    15
#    EANL-Y
#    ENALTY
#     
################################## 

import week6

def main():
    f = open('input.txt', 'r')
    s1 = f.readline().strip()
    s2 = f.readline().strip()
    f.close()
    
    sol = week6.local_alignment_1(s1,s2)
    
    g = open('output.txt', 'w')
    g.write(sol)
    g.close()
    
if __name__ == '__main__':
    main()
