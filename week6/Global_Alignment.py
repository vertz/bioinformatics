##################################
#
# Solve the Global Alignment Problem.
#    Input: Two protein strings written in the single-letter amino acid alphabet.
#    Output: The maximum alignment score of these strings followed by an alignment achieving this
#    maximum score. Use the BLOSUM62 scoring matrix and indel penalty = 5
#    
# Sample Input:
#    PLEASANTLY
#    MEANLY
#    
# Sample Output:
#    8
#    PLEASANTLY
#    MEA--N-LY
#     
################################## 

import week6

def main():
    f = open('input.txt', 'r')
    s1 = f.readline().strip()
    s2 = f.readline().strip()
    f.close()
    
    sol = week6.global_alignment(s1,s2)
    
    g = open('output.txt', 'w')
    g.write(sol)
    g.close()
    
if __name__ == '__main__':
    main()
