##################################
#
# Solve the String Composition Problem.
#     Input: An integer k and a string Text.
#     Output: Compositionk(Text), where the k-mers are written in lexicographic order.
#
# Sample Input:
#    5
#    CAATCCAAC
#
# Sample Output:
#    AATCC
#    ATCCA
#    CAATC
#    CCAAC
#    TCCAA
#
################################## 

import week4

def main():
    f = open('input.txt', 'r')
    k = f.readline().rstrip()
    text = f.readline().rstrip()
    f.close()

    k_mers = week4.string_composition(text, k)
    sol = ""
    
    for k_mer in k_mers:
        sol += k_mer + "\n"
    
    g = open('output.txt', 'w')
    g.write(sol)
    g.close()
    
if __name__ == '__main__':
    main()
