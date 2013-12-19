
# Longest Common Subsequence (enum)
class LCS:
    start     = -1
    deletion  =  1
    insertion =  2
    matche    =  3
    mismatch  =  4
    
# Solve the Global Alignment Problem.
#    Input:  Two protein strings written in the single-letter amino acid alphabet.
#    Output: The maximum alignment score of these strings
def global_alignment(s1, s2, indel_penalty = 0 , score = 1):
    
    sz_1 = len(s1) + 1
    sz_2 = len(s2) + 1
    
    backtrack = [[0]*sz_2 for x in xrange(sz_1)] 
    mem = [[0]*sz_2 for x in xrange(sz_1)]

    for i in xrange(1, sz_1):
        backtrack[i][0] = LCS.deletion
        mem[i][0] = mem[i-1][0] - indel_penalty

    for j in xrange(1, sz_2):
        backtrack[0][j] = LCS.insertion
        mem[0][j] = mem[0][j-1] - indel_penalty

    for i in range(1, sz_1):
        for j in range(1, sz_2):
        
            if s1[i-1] == s2[j-1]:
                backtrack[i][j] = LCS.matche
                mem[i][j] = mem[i-1][j-1] + score
                continue
                
            deletion  = mem[i-1][j] - indel_penalty
            insertion = mem[i][j-1] - indel_penalty
            mismatch  = mem[i-1][j-1] - indel_penalty
            
            mem[i][j] = max(mismatch, deletion, insertion)    
                
            if mem[i][j] == insertion:
                backtrack[i][j] = LCS.mismatch
            elif mem[i][j] == insertion:
                backtrack[i][j] = LCS.insertion
            else:
                backtrack[i][j] = LCS.deletion
    
    return mem[sz_1 - 1][sz_2 - 1]

# Find the edit distance between two strings.
#    Input: Two strings.
#    Output: The edit distance between these strings.    
def edit_distance(s1, s2):

    # set the indel_penalty = 1 and score = 0 
    # will give as exactly how many indel we had
    ret = global_alignment(s1, s2, 1 ,0)
    return -ret







        
