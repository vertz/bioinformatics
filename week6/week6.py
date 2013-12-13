
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
    matche    = 3
    mismatch  = 4

def reverse(s):
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
            
    return reverse(ret)  
             
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
                backtrack[i][j] = LCS.matche 
            
    #return mem[sz_1 - 1][sz_2 - 1]
    return output_lcs(backtrack, s1, sz_1 - 1, sz_2 - 1)
    
# Output topological ordering 
def topological_sort(graph, src, weight = True):
    if weight:
        graph = graph['edges']
    
    edges = []
    for lst in graph.values():
        edges += lst     
    
    top_sort = []
    stack = [src]
                  
    while stack:
        
        t = stack.pop()
        top_sort.append(t)
        
        if t in graph.keys(): 
            for v in graph[t]:
            
                edges.remove(v)
                if not v in edges:
                    stack.append(v) 
    
    if edges:
        raise Exception("graph has at least one cycle") 
        
    return top_sort        

# Input a list of edges in the graph. 
# The edge notation 0->1:7 indicates that an edge connects node 0 to node 1 with weight 7
def adjacency_list_to_graph(adj):
    adj = list(adj)
    
    edges = {}
    weights = {}
    
    for elem in adj:
        lst = elem.split("->")
        if len(lst) != 2:
            raise Exception("bad data format => " + str(lst))
            
        u = lst[0]
        
        # edge = (v, w(u,v))
        edge = lst[1].split(":") 
        v = edge[0]
        
        if u in edges.keys():
            edges[u].append(v)
            weights[(u,v)] = int(edge[1])
        else:
            edges[u] = [v] 
            weights[(u,v)] = int(edge[1])        
          
    return {'weights':weights, 'edges':edges}

# backtrack the path from node top_sort[i] to the source node 
def output_dag_longest_path(backtrack, top_sort, i):

    path = [top_sort[i]]
    while i > 0:
        
        i = backtrack[i]
        path.append(top_sort[i])
            
    return reverse(path) 

# Solve the Longest Path in a DAG Problem.
#    Input: An integer representing the source node of a graph, followed by an integer representing the sink
#    node of the graph, followed by a list of edges in the graph. The edge notation 0->1:7 indicates that
#    an edge connects node 0 to node 1 with weight 7.
#    Output: The length of a longest path in the graph and the path.
def dag_longest_path(graph, src, sink):
    
    top_sort = topological_sort(graph, src)
    sz = len(top_sort)
    
    backtrack = [0 for x in xrange(sz)] 
    mem = [float("-infinity") for x in xrange(sz)]
    mem[0] = 0
    
    for idx in xrange(sz):
        v = top_sort[idx]
        
        for idy in xrange(idx):
            u = top_sort[idy]
            if not u in graph['edges'].keys():
                continue
            
            if v in graph['edges'][u]:
                w = mem[idy] + graph['weights'][(u,v)]
                
                if mem[idx] < w:
                    backtrack[idx] = idy
                    mem[idx] = w             

        if v == sink:
            path = output_dag_longest_path(backtrack, top_sort, idx)
            return {'length':mem[idx], 'path':path}

    raise Exception("sink not in top_sort") 

class Score:
    BLOSUM62 = 1
    PAM250   = 2

# load the BLOSUM62 scoring matrix 
def load_scoring_matrix(t_score = Score.BLOSUM62):
    index = {}
    matrix = []
    
    f = None
    if t_score == Score.BLOSUM62:
        f = open('BLOSUM62.txt', 'r')
    elif t_score == Score.PAM250:
        f = open('PAM250.txt', 'r')
    else:
        raise Exception("wrong score matrix")     
    
    keys = f.readline().strip().split()
    sz = len(keys)
    for idx in xrange(sz):
        index[keys[idx]] = idx    
    
    while True:
        line = f.readline().strip()
        if not line: break
        
        data = line.split()
        if len(data) == sz + 1:
            matrix.append(map(int, data[1:]))
        else:
            Exception("bad data format") 
       
    f.close()
    
    return {'index':index, 'matrix':matrix}

def output_global_alignment(backtrack, s1, s2, i, j):

    ret1 = ""
    ret2 = ""
    while i > 0 or j > 0:
    
        if backtrack[i][j] == LCS.deletion:
            i -= 1
            ret1 += s1[i]
            ret2 += "-"
            
        elif backtrack[i][j] == LCS.insertion:
            j -= 1
            ret1 += "-"
            ret2 += s2[j]
            
        else:
            i -= 1
            j -= 1
            ret1 += s1[i]
            ret2 += s2[j]
    
    ret  = reverse(ret1) + '\n'
    ret += reverse(ret2) + '\n' 
    return ret 

# Solve the Global Alignment Problem.
#    Input: Two protein strings written in the single-letter amino acid alphabet.
#    Output: The maximum alignment score of these strings followed by an alignment achieving this
#    maximum score. Use the BLOSUM62 scoring matrix and indel penalty = 5
def global_alignment(s1, s2, indel_penalty = 5, score = None):
    if not score:
        score = load_scoring_matrix() 
    
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
        
            idx = score['index'][s1[i-1]]
            idy = score['index'][s2[j-1]]
            matche = mem[i-1][j-1] + score['matrix'][idx][idy] 
            deletion  = mem[i-1][j] - indel_penalty
            insertion = mem[i][j-1] - indel_penalty  
            
            mem[i][j] = max(matche, deletion, insertion)
            
            if mem[i][j] == matche:
                if s1[i-1] == s2[j-1]:
                    backtrack[i][j] = LCS.matche
                else:
                    backtrack[i][j] = LCS.mismatch
            elif mem[i][j] == insertion:
                backtrack[i][j] = LCS.insertion
            else:
                backtrack[i][j] = LCS.deletion    
      
    ret  = str(mem[sz_1 - 1][sz_2 - 1]) + '\n'
    ret += output_global_alignment(backtrack, s1, s2, sz_1 - 1, sz_2 - 1)
    return ret

def backtrack_alignment_graph(path, s1, s2, local = False):
    
    ret1 = ""
    ret2 = ""
    
    curr = path.pop()
    if local:
        curr = path.pop()
    
    i = curr[0]
    j = curr[1]
    
    zero = (0,0)
    while path:
    
        curr = path.pop() 
        if curr <= zero:
            break 
        elif curr == (i-1,j):
            i -= 1
            ret1 += s1[i]
            ret2 += "-"
            
        elif curr == (i,j-1):
            j -= 1
            ret1 += "-"
            ret2 += s2[j]
            
        else:
            i -= 1
            j -= 1
            ret1 += s1[i]
            ret2 += s2[j]
    
    ret  = reverse(ret1) + '\n'
    ret += reverse(ret2) + '\n' 
    return ret


def alignment_graph(s1, s2, indel_penalty, score):
    
    sz_1 = len(s1) + 1
    sz_2 = len(s2) + 1
    
    edges = {}
    weights = {}

    for i in xrange(1, sz_1):
        v = (i-1,0)
        u = (i,0)
        
        edges[v] = [u]
        weights[(v,u)] = -indel_penalty

    for j in xrange(1, sz_2):
        v = (0,j-1)
        u = (0,j)
        
        if v in edges.keys():
            edges[v].append(u)
        else:
            edges[v] = [u]
        weights[(v,u)] = -indel_penalty

    w = [-indel_penalty, -indel_penalty, 0]

    for i in range(1, sz_1):
        for j in range(1, sz_2):
        
            u    = (i,j)
            in_u = [(i-1,j), (i,j-1), (i-1,j-1)]
        
            idx = score['index'][s1[i-1]]
            idy = score['index'][s2[j-1]]
            w[2] = score['matrix'][idx][idy] 
            
            for k in xrange(3):
                v = in_u[k]
            
                if v in edges.keys():
                    edges[v].append(u)
                else:
                    edges[v] = [u]
                weights[(v,u)] = w[k]  
                
    return {'weights':weights, 'edges':edges}                       

# Solve the Global Alignment Problem.
#    Input: Two protein strings written in the single-letter amino acid alphabet.
#    Output: The maximum alignment score of these strings followed by an alignment achieving this
#    maximum score. Use the BLOSUM62 scoring matrix and indel penalty = 5
def global_alignment_with_dag(s1, s2, indel_penalty = 5, score = None):
    if not score:
        score = load_scoring_matrix()
        
    graph   = alignment_graph(s1,s2,indel_penalty,score)
    dag_ret = dag_longest_path(graph, (0,0), (len(s1),len(s2)))
    
    ret  = str(dag_ret['length']) + '\n'
    ret += backtrack_alignment_graph(dag_ret['path'], s1, s2)
    return ret    

# Solve the Local Alignment Problem.
#    Input: Two protein strings written in the single-letter amino acid alphabet.
#    Output: The maximum score of a local alignment of the strings, followed by a local alignment of these
#    strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty = 5
def local_alignment(s1, s2, indel_penalty = 5, score = None):
    if not score:
        score = load_scoring_matrix(Score.PAM250)
        
    graph = alignment_graph(s1,s2,indel_penalty,score)
    
    weights = graph['weights']
    edges = graph['edges']
    
    sz_1 = len(s1) + 1
    sz_2 = len(s2) + 1
    
    src  = (-1,-1)
    sink = (sz_1,sz_2)
    
    edges[src] = []
    edges[(sz_1-1,sz_2-1)] = []
    
    for i in range(0, sz_1):
        for j in range(0, sz_2):
            v = (i,j)   
                             
            edges[src].append(v)
            edges[v].append(sink) 
            
            weights[(src,v)] = 0
            weights[(v,sink)] = 0   
    
    dag_ret = dag_longest_path(graph, src, sink)
    
    ret  = str(dag_ret['length']) + '\n'
    ret += backtrack_alignment_graph(dag_ret['path'], s1, s2, True)
    return ret  

           
