# Solve the Trie Construction Problem.
#    Input: A collection of strings Patterns.
#    Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has
#    n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in
#    any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first
#    two members of the triple must be the integers labeling the initial and terminal nodes of the edge,
#    respectively; the third member of the triple must be the symbol labeling the edge.
def trie_construction(patterns, root_label = 1):
    root = root_label
    next = root + 1
    
    adj_str = ""
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
                adj_str += str(curr) + " " + str(next) + " " + c + "\n"
            
                trie[next] = {} 
                node[c] = next
                curr  = next
                next += 1  
        
        node = trie[curr]  
        c = pat[sz]
        if c not in node.keys():
            adj_str += str(curr) + " " + str(next) + " " + c + "\n"
            node[c] = next
            next += 1

    return trie , adj_str
    
    
def prefix_trie_matching(text, trie, sz = -1, root = 1):
    if sz < 0:
        sz = len(text)

    node = root
    idx = 0
    
    while idx < sz:
        curr = trie[node]
        c = text[idx]
        
        if c in curr.keys():
            node = curr[c]
            idx += 1
        else:
            break
            
        if node not in trie.keys():
            return True , text[:idx]    

    return False , ""

# Implement TRIEMATCHING to solve the Multiple Pattern Matching Problem.
#    Input: A string Text and a Trie(Patterns).
#    Output: All starting positions in Text where a string from Patterns appears as a substring.
def trie_matching(text, trie):

    text_len = len(text)
    sz = text_len
    idx = 0
    
    matching = {}
    
    while idx < text_len:
    
        pred , pat = prefix_trie_matching(text[idx:], trie, sz)     
        if pred:
            if pat in matching.keys():
                matching[pat].append(idx)
            else:
                matching[pat] = [idx]
         
        idx += 1
        sz  -= 1   
      
    return matching         

# solve the Multiple Pattern Matching Problem.
#    Input: A string Text and a collection of strings Patterns.
#    Output: All starting positions in Text where a string from Patterns appears as a substring.
def multiple_pattern_matching(text, patterns):

    trie, _  = trie_construction(patterns)
    matching = trie_matching(text, trie) 
    
    ret = ""
    for i in range(len(patterns)):
        pat = patterns[i]
    
        if pat in matching.keys():
            ret += " ".join(map(str,matching[pat])) + "\n"     
    
    return ret
              


