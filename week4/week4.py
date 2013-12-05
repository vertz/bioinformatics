# Solve the String Composition Problem.
#   Input: An integer k and a string Text.
#   Output: Compositionk(Text), where the k-mers are written in lexicographic order.
def string_composition(text, k):
    k = int(k)
    sz = len(text) - k + 1
    
    k_mers = []
    for idx in range(sz):
        k_mers.append(text[idx : idx + k])
        
    return sorted(k_mers)   

#   Input: A graph (dictionary)
#   Output: the graph in the form of an adjacency list. 
def graph_to_string(graph):
    graph = dict(graph)
    
    ret = ""
    for v in sorted(graph.keys()):
        for u in graph[v]:
            ret += v + " -> " + u + "\n"
            
    return ret  
    
#   Input: A graph (dictionary)
#   Output: the graph in the form of an adjacency list. 
def de_bruijn_graph_to_string(graph):
    graph = dict(graph)
    
    ret = ""
    for v in sorted(graph.keys()):
        ret += v + " -> "
        
        neighbors = sorted(set(graph[v]))
        sz = len(neighbors) - 1
        
        for idx in range(sz):
            ret += neighbors[idx] + ","
            
        ret += neighbors[sz] + "\n"    
            
    return ret          

def string_suffix(s):
    return s[1:] 
                   
def string_prefix(s):
    return s[:-1]  

# Solve the Overlap Graph Problem 
#   Input: A collection Patterns of k-mers.
#   Output: The overlap graph Overlap(Patterns)  
def overlap_graph(k_mers):
    k_mers = list(k_mers)
    sz = len(k_mers)
    
    graph = {}
    
    for mer_1 in k_mers:
        suffix = string_suffix(mer_1)
        edges = []
        count = 0
        
        for mer_2 in k_mers:
            if mer_1 == mer_2:
                continue
                
            if suffix == string_prefix(mer_2):
                edges.append(mer_2)  
                count += 1      
        
        if count > 0:
            graph[mer_1] = sorted(edges)             
                
    return graph              



# Solve the De Bruijn Graph from a String Problem.
#   Input: An integer k and a string Text.
#   Output: DeBruijnk(Text).                
def de_bruijn_from_string(text, k):                
    k_mers = string_composition(text, k)                
    sz = len(k_mers)
    
    graph = {}
    
    for mer_1 in k_mers:
        suffix_1 = string_suffix(mer_1)
        edges = []
        count = 0
        
        for mer_2 in k_mers:
            if mer_1 == mer_2:
                continue
            
            # check suffix(mer1) == prefix(mer2)
            prefix_2 = string_prefix(mer_2) 
            if suffix_1 == prefix_2:
                # append prefix(mer2)
                edges.append(prefix_2)  
                count += 1      
        
        if count == 0:
            edges.append(suffix_1)
          
        prefix_1 = string_prefix(mer_1)      
        if prefix_1 in graph.keys():
            graph[prefix_1] += edges
        else:
            graph[prefix_1] = edges                  
               
    return graph             

# Construct the de Bruijn graph from a set of k-mers
#   Input: A collection of k-mers Patterns.
#   Output: the de Bruijn graph DeBruijn(Patterns).                
def de_bruijn_from_k_mers(k_mers):                   
    k_mers = list(k_mers)
    
    graph = {}
    
    for mer in k_mers:
        suffix = string_suffix(mer)
        prefix = string_prefix(mer)        

        if prefix in graph.keys():
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]
            
    return graph        
            


                
                
