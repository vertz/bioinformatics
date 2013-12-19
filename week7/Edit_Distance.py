##################################
#
# Find the edit distance between two strings.
#    Input: Two strings.
#    Output: The edit distance between these strings.
#    
# Sample Input:
#    PLEASANTLY
#    MEANLY
#    
# Sample Output:
#    5
#
################################## 

import week7

def main():
    f = open('input.txt', 'r')
    s1 = f.readline().strip()
    s2 = f.readline().strip()
    f.close()

    sol = week7.edit_distance(s1, s2)
    
    g = open('output.txt', 'w')
    g.write(str(sol) + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
