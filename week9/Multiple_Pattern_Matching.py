##################################
#
# Implement TRIEMATCHING to solve the Multiple Pattern Matching Problem.
#    Input: A string Text and a collection of strings Patterns.
#    Output: All starting positions in Text where a string from Patterns appears as a substring.
#    
# Sample Input:
#    AATCGGGTTCAATCGGGGT
#    ATCG
#    GGGT
#    
# Sample Output:
#    1 11
#    4 15
#
################################## 

import week9

def main():
    f = open('input.txt', 'r')
    
    text = f.readline().strip()
    
    patterns = []
    for line in f:
        patterns.append(line.strip())
        
    f.close()

    sol = week9.multiple_pattern_matching(text, patterns)
    
    g = open('output.txt', 'w')
    g.write(sol)
    g.close()
    
if __name__ == '__main__':
    main()
