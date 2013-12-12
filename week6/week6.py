
# Solve the Change Problem.
#    Input: An integer money and an array coins = (coin1, ..., coind).
#    Output: The minimum number of coins with denominations coins that changes money.        
def change_rec(money, coins, acc = 0):
    money = int(money)
    if money == 0:
        return acc
        
    min_coins = float("infinity")
    for coin in coins:
    
        if coin <= money:
            n_coins = change_rec(money - coin, coins, acc + 1)
            if n_coins < min_coins:
                min_coins = n_coins 
                
    return min_coins             

# Solve the Change Problem.
#    Input: An integer money and an array coins = (coin1, ..., coind).
#    Output: The minimum number of coins with denominations coins that changes money.
def change_mem(money, coins):
    money = int(money) 
    if money == 0:
        return 0
        
    mem_min_coins = [0]
    for m in range(money + 1):
    
        mem_min_coins.append(float("infinity")) 
        for coin in coins:
        
            if m >= coin:
                n_coins = mem_min_coins[m - coin] + 1
            
                if n_coins < mem_min_coins[m]:
                    mem_min_coins[m] = n_coins     
                
    return mem_min_coins[money] 

# Find the length of a longest path in the Manhattan Tourist Problem.
#    Input: Integers n and m, followed by an n * (m + 1) matrix down and an (n + 1) * m matrix right.
#           The two matrices are separated by the - symbol.
#    Output: The length of a longest path from source (0, 0) to sink (n, m) in the n * m rectangular grid whose
#           edges are defined by the matrices down and right.
def manhattan_tourist(row, col, down, right):
    _row = int(row) + 1
    _col = int(col) + 1
    
    mem = [[0]*_col for x in xrange(_row)]
    
    for i in range(1, _col):
        mem[0][i] = mem[0][i - 1] + right[0][i - 1]
    
    for j in range(1, _row):
        mem[j][0] = mem[j - 1][0] + down[j - 1][0]

    for i in range(1, _row):
        for j in range(1, _col):
            
            ij_down  = mem[i-1][j] + down[i-1][j]   
            ij_right = mem[i][j-1] + right[i][j-1]
                
            mem[i][j] = max(ij_down , ij_right)   

    return mem[row][col]      

# Longest Common Subsequence (enum)
class LCS:
    deletion  = 1
    insertion = 2
    matches   = 3

def reverseString(s):
    return s[::-1]

# outputs an LCS 
# between the i-prefix of s1 and the j-prefix of s2
# from longest_common_subsequence(s1, s2)
def output_lcs(backtrack, s, i, j):

    ret = ""
    while i > 0 and j > 0:
        
        if backtrack[i][j] == LCS.deletion:
            i -= 1
        elif backtrack[i][j] == LCS.insertion: 
            j -= 1
        else:
            i -= 1
            j -= 1
            ret += s[i]
            
    return reverseString(ret)  
             
# solve the Longest Common Subsequence Problem.
#    Input: Two strings s and t.
#    Output: A longest common subsequence of s and t.
#
# Note: If more than one LCS exists, you may return any one.    
def longest_common_subsequence(s1, s2):
    
    sz_1 = len(s1) + 1
    sz_2 = len(s2) + 1
    
    backtrack = [[0]*sz_2 for x in xrange(sz_1)] 
    mem = [[0]*sz_2 for x in xrange(sz_1)]

    for i in range(1, sz_1):
        for j in range(1, sz_2):
        
            mem[i][j] = max(mem[i-1][j] , mem[i][j-1])
            if s1[i-1] == s2[j-1]:
                mem[i][j] = max(mem[i][j] , mem[i-1][j-1] + 1)     
      
            if mem[i][j] == mem[i-1][j]:
                backtrack[i][j] = LCS.deletion
            elif mem[i][j] == mem[i][j-1]:
                backtrack[i][j] = LCS.insertion
            else:
                backtrack[i][j] = LCS.matches 
            
    #return mem[sz_1 - 1][sz_2 - 1]
    return output_lcs(backtrack, s1, sz_1 - 1, sz_2 - 1)
  


          
