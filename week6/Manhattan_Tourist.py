##################################
#
# Find the length of a longest path in the Manhattan Tourist Problem.
#    Input: Integers n and m, followed by an n * (m + 1) matrix down and an (n + 1) * m matrix right.
#           The two matrices are separated by the - symbol.
#    Output: The length of a longest path from source (0, 0) to sink (n, m) in the n * m rectangular grid whose
#           edges are defined by the matrices down and right.
#    
# Sample Input:
#    4
#    4
#    1 0 2 4 3
#    4 6 5 2 1
#    4 4 5 2 1
#    5 6 8 5 3
#    -
#    3 2 4 0
#    3 2 4 2
#    0 7 3 3
#    3 3 0 2
#    1 3 2 2
#    
# Sample Output:
#    34
#
################################## 

import week6

def main():
    f = open('input.txt', 'r')
    
    n = int(f.readline().strip())
    m = int(f.readline().strip())
    
    down = []
    for line in f:
    
        line = line.strip()
        if line == "-":
            break
    
        down.append( map(int, line.split(" ")) )
        
    right = []
    for line in f:
        right.append( map(int, line.strip().split(" ")) )
        
    f.close()

    sol = week6.manhattan_tourist(n, m, down, right)
    
    g = open('output.txt', 'w')
    g.write(str(sol) + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
