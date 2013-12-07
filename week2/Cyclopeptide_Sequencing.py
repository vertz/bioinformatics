##################################
#
# Counting Peptides with Given Mass Problem: Compute the number of peptides of given total mass.
#    Input: An integer m.
#    Output: The number of linear peptides having integer mass m.
#
# Sample Input:
#    1024
#
# Sample Output:
#    14712706211
#
################################## 

import week2

def main():
    f = open('input.txt', 'r')
    mass = f.readline().rstrip()
    f.close()

    sol = week2.count_peptides(mass)
    
    g = open('output.txt', 'w')
    g.write(sol + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
