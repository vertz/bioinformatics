# Solve the Trie Construction Problem.
#    Input: A collection of strings Patterns.
#    Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has
#    n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in
#    any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first
#    two members of the triple must be the integers labeling the initial and terminal nodes of the edge,
#    respectively; the third member of the triple must be the symbol labeling the edge.
def trie_construction(patterns):
    
    ret = ""
    
    root  = 1
    next = root + 1

    trie = {root:{}}

    for pat in patterns:
        curr = root
        sz = len(pat)-1

        for i in range(sz):
            node = trie[curr]
            c = pat[i]

            nodeExist = c in node.keys()
            if nodeExist:
                curr = node[c]

            if curr < 0 or not nodeExist:
            
                ret += str(curr) + " " + str(next) + " " + c + "\n"
            
                trie[next] = {} 
                node[c] = next
                curr  = next
                next += 1  
        
        node = trie[curr]  
        c = pat[sz]
        if c not in node.keys():
            ret += str(curr) + " " + str(next) + " " + c + "\n"
            node[c] = next
            next += 1


    return ret
