##################################
#
# Number of Breakpoints Problem: Find the number of breakpoints in a permutation.
#    Input: A permutation P.
#    Output: The number of breakpoints in P.
#
# Sample Input:
#    (+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)
#
# Sample Output:
#    8
#
################################## 

import week8

def main():
    f = open('input.txt', 'r')
    perm = f.readline().strip()
    perm = perm.strip('()')
    f.close()

    sol = week8.count_breakpoints(perm)
    
    g = open('output.txt', 'w')
    g.write(str(sol) + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
