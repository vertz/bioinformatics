##################################
#
# Use OUTPUTLCS (reproduced below) to solve the Longest Common Subsequence Problem.
#    Input: Two strings s and t.
#    Output: A longest common subsequence of s and t.
#
# Note: If more than one LCS exists, you may return any one.
#
# Sample Input:
#    AACCTTGG
#    ACACTGTGA
#
# Sample Output:
#    AACTGG
#     
################################## 

import week6

def main():
    f = open('input.txt', 'r')
    s1 = f.readline().strip()
    s2 = f.readline().strip()
    f.close()

    sol = week6.longest_common_subsequence(s1, s2)
    
    g = open('output.txt', 'w')
    g.write(sol + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
