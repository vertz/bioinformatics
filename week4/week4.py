

def string_composition(text, k):
    k = int(k)
    sz = len(text) - k + 1
    
    k_mers = []
    for idx in range(sz):
        k_mers.append(text[idx : idx + k])
        
    return sorted(k_mers)   

def graph_to_string(graph):
    graph = dict(graph)
    
    ret = ""
    for v in sorted(graph.keys()):
        for u in graph[v]:
            ret += v + " -> " + u + "\n"
            
    return ret        
    
def overlap_graph(k_mers):
    k_mers = list(k_mers)
    sz = len(k_mers)
    
    graph = {}
    
    for mer_1 in k_mers:
        suffix = mer_1[1:]
        edges = []
        count = 0
        
        for mer_2 in k_mers:
            if suffix == mer_2[:-1]:
                edges.append(mer_2)  
                count += 1      
        
        if count > 0:
            graph[mer_1] = sorted(edges)             
                
    return graph              
                
                
                
                
                
                
                
                
                
                
                
                
