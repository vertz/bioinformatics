##################################
#
# Solve the k-Universal Circular String Problem.
#    Input: An integer k.
#    Output: A k-universal circular string.
#
# Sample Input:
#    4
#
# Sample Output:
#    0000110010111101
#
################################## 

import week4

def main():
    f = open('input.txt', 'r')
    k = f.readline().rstrip()
    f.close()

    sol = week4.universal_string(k)
    
    g = open('output.txt', 'w')
    g.write(sol + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
