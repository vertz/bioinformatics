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
    
def cycle_to_string(cycle):
    cycle = list(cycle)
    
    ret = ""
    sz = len(cycle) - 1
    
    for idx in range(sz):
        ret += cycle[idx] + "->"  
        
    ret += cycle[sz] + "\n"  
    return ret     
    
def adjacency_list_to_graph(adj):
    adj = list(adj)
    
    graph = {}
    
    for elem in adj:
        lst = elem.split(" -> ")
        if len(lst) != 2:
            raise Exception("bad data format => " + str(lst))
            
        u = lst[0]
        neighbors = lst[1].split(",") 
        graph[u] = neighbors    
    
    return graph           

def string_suffix(s):
    return s[1:] 
                   
def string_prefix(s):
    return s[:-1]      

def read_pair_suffix(pair):
    return (pair[0][1:],pair[1][1:]) 
                   
def read_pair_prefix(pair):
    return (pair[0][:-1],pair[1][:-1]) 

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
    
# Construct the de Bruijn graph from a set of read_pairs
#   Input: A collection of read_pairs
#   Output: the de Bruijn graph DeBruijn(read_pairs).                
def de_bruijn_from_read_pairs(read_pairs):                   
    read_pairs = list(read_pairs)
    
    graph = {}
    
    for pair in read_pairs:
        pair = pair.split('|')
    
        suffix = read_pair_suffix(pair)
        prefix = read_pair_prefix(pair)        

        if prefix in graph.keys():
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]
            
    return graph    

# Solve the Eulerian Cycle Problem.
#   Input: An Eulerian directed graph.
#   Output: An Eulerian cycle in this graph.    
def eulerian_cycle(graph):
    _graph = dict(graph)
    
    euler_cycle = []
    unused_edges = []
    cycle = []
    
    vertices = _graph.keys()
    if len(vertices) < 1:
        raise Exception("empty graph")    
        
    u = vertices[0]
    while True:
        
        if not _graph[u]:
            
            cycle.append(u)
            
            if u != cycle[0]:
                raise Exception("not a cycle")   
            
            if not euler_cycle:
                euler_cycle = cycle
            else:
                idx = euler_cycle.index(cycle[0])
                
                tmp  = euler_cycle[:idx]
                tmp += cycle
                tmp += euler_cycle[idx+1:]
                
                euler_cycle = tmp  
            
            if not unused_edges:
                break
            
            v = unused_edges[0]
            edges = _graph[v]
            u = edges.pop()
            
            if not edges:
                unused_edges.remove(v)  
                
            cycle = [v]     
        
        else:
            cycle.append(u)
            edges = _graph[u]
            
            _u = edges.pop()
            if edges and not u in unused_edges:
                unused_edges.append(u)
            elif not edges and u in unused_edges:
                unused_edges.remove(u)    
                
            u = _u
                
    return euler_cycle            

#   Input: directed graph that has an Eulerian path.
#   Output: list of unbalanced nodes in the graph
def find_unbalanced_nodes(graph):
    _graph = dict(graph)
    
    edges = []
    for nodes in _graph.values():
        edges += nodes         
    
    unbalanced = []
    
    v = None
    count = 0
    for u in sorted(edges):
    
        if v != u:
            if count % 2 == 1:
                unbalanced.append(v)                    
            
            v = u
            if v in _graph.keys():
                count = len(_graph[v])
            else:
                count = 0
            
        count += 1       
    
    if len(unbalanced) == 1:
        edges = set(edges)
        
        for u in _graph.keys():
            if not u in edges:
                unbalanced.append(u) 
                break   
    
    return unbalanced            

# Solve the Eulerian Path Problem.
#    Input: directed graph that has an Eulerian path.
#    Output: An Eulerian path in this graph. 
def eulerian_path(graph):
    _graph = dict(graph)
    
    unbalanced = find_unbalanced_nodes(graph)
    sz = len(unbalanced)
    w = None
    if sz == 2:
    
        u = unbalanced[0]
        v = unbalanced[1]
        
        if u in _graph.keys():
            w = v
            _graph[v] = [u]
        else:
            w = u
            _graph[u] = [v]     
         
    elif sz != 0:
        raise Exception("wrong number of unbalanced nodes ( " + str(sz) + " )")            
    
    cycle = eulerian_cycle(_graph)
    cycle.pop() # remove cycle
    
    if w:
        idx = cycle.index(w) + 1
        eulerian_path  = cycle[idx:]
        eulerian_path += cycle[:idx]
    else:
        eulerian_path = cycle    
    
    return eulerian_path

# Solve the String Reconstruction Problem.
#    Input: directed graph that has an Eulerian path.
#    Output: An Eulerian path in this graph.
def string_reconstruction(graph):
    path = eulerian_path(graph)
    
    if not path:
        raise Exception("Empty path")    
    
    text = path[0]
    for s in path[1:]:
        text += s[-1]  
        
    return text   

#    Input: An integer k.
#    Output: list of all binary numbers in range [0,2^k)
def binary_numbers_iter(k, numbers = ['0','1']):
    k = int(k) - 1
    
    if k < 1:
        return numbers
        
    lst = []
    for num in numbers:
        lst += [num + '0', num + '1']
        
    return binary_numbers_iter(k, lst)    

# Solve the k-Universal Circular String Problem.
#    Input: An integer k.
#    Output: A k-universal circular string.    
def universal_string(k):
    k = int(k) - 1
    graph = {}
    
    if k < 2:
        raise Exception("k(" + str(k + 1) + ") should be > 2 ") 
    
    nodes = binary_numbers_iter(k) 
    for u in nodes:
        suffix = string_suffix(u)
        graph[u] = [suffix + '0', suffix + '1']    
 
    cycle = eulerian_cycle(graph)   
    
    idx = cycle.index(nodes[0])
    path  = cycle[idx:]
    path += cycle[1:idx]
    
    u_string = path[0]
    zero_idx = 1 - k
    
    for s in path[1:zero_idx]:
        u_string += s[-1]  
        
    return u_string

def read_pairs_to_string(read_pairs):
    read_pairs = list(read_pairs)
    
    ret = ""
    for pair in read_pairs[:-1]:
        ret += "(" + pair[0] + "|" + pair[1] + "),"  
        
    pair = read_pairs[-1]    
    ret += "(" + pair[0] + "|" + pair[1] + ") \n" 
    
    return ret    

# Give the (k,d)-mer composition of text in lexicographic order    
def paired_composition(text, k, d):
    k = int(k)
    d = int(d)
    
    read_pairs = []
    
    sz  = len(text) - 2*k - d + 1
    for idx in range(sz):
        idy = idx + k + d
        read1 = text[idx : idx + k]
        read2 = text[idy : idy + k]
        
        read_pairs.append([read1,read2])
    
    return sorted(read_pairs)    

# Solve the String Reconstruction from Read-Pairs Problem.
#    Input: paired (k-1)-mers PairedReads graph and integer d.
#    Output: A string Text with (k, d)-mer composition equal to PairedReads.
def string_reconstruction_from_read_pairs(graph, d):
    path = eulerian_path(graph)
    d = int(d)
    
    if not path:
        raise Exception("Empty path")    
    
    text = path[0][0]
    for pair in path[1 : d + 2]:
        # [0,d+1) because |pair| = k-1
        text += pair[0][-1]
    
    text += path[0][1]
    for pair in path[1:]:
        text += pair[1][-1]  
        
    return text 

def graph_degrees(graph):
    if not graph:
        raise Exception("Empty graph")
    
    # degrees[u] = [in(u),out(u)]    
    degrees = {}     
    
    for v in graph.keys():
        neighbors = graph[v]
        out_degree = len(neighbors)
        
        if v in degrees:
            degrees[v][1] = out_degree
        else:
            degrees[v] = [0, out_degree]        
        
        for u in neighbors:
            if u in degrees:
                degrees[u][0] += 1
            else:
                degrees[u] = [1,0]
     
    return degrees                 

# Generate the contigs from a collection of reads (with imperfect coverage).
#    Input: A collection of k-mers Patterns.
#    Output: All contigs in DeBruijn(Patterns).    
def generate_contigs_from_reads(k_mers):
    graph = de_bruijn_from_k_mers(k_mers)
    if not graph:
        raise Exception("Empty graph")         
    
    degrees = graph_degrees(graph)
    contigs = []
    
    for v in graph.keys():
    
        # we want maximal non-branching path 
        if degrees[v] == [1,1]:
            continue
    
        for u in graph[v]: 
            contig = v
            w = u
            
            while True:
                contig += w[-1]
                w_degree = degrees[w] 
                
                if w_degree == [1,1]:
                    w = graph[w][0]
                else:
                    break
                   
            contigs.append(contig)                                      
         
    return sorted(contigs)                           
