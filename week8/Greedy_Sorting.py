##################################
#
# Implement GREEDYSORTING.
#    Input: A permutation P.
#    Output: The sequence of permutations corresponding to applying GREEDYSORTING to P, ending with
#    the identity permutation.
#    
# Sample Input:
#    (-3 +4 +1 +5 -2)
#    
# Sample Output:
#    (-1 -4 +3 +5 -2)
#    (+1 -4 +3 +5 -2)
#    (+1 +2 -5 -3 +4)
#    (+1 +2 +3 +5 +4)
#    (+1 +2 +3 -4 -5)
#    (+1 +2 +3 +4 -5)
#    (+1 +2 +3 +4 +5)
#
################################## 

import week8

def main():
    f = open('input.txt', 'r')
    perm = f.readline().strip()
    perm = perm.strip('()')
    f.close()

    sol = week8.greedy_sorting(perm)
    
    g = open('output.txt', 'w')
    g.write(sol + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
