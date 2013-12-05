##################################
#
# Construct the de Bruijn graph from a set of k-mers
#     Input: A collection of k-mers Patterns.
#     Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
#
#   Sample Input:
#        GAGG
#        GGGG
#        GGGA
#        CAGG
#        AGGG
#        GGAG
#
#   Sample Output:
#        AGG -> GGG
#        CAG -> AGG
#        GAG -> AGG
#        GGA -> GAG
#        GGG -> GGA,GGG
#
################################## 

import week4

def main():
    f = open('input.txt', 'r')
    
    k_mers = []
    for line in f:
        k_mers.append(line.rstrip())
        
    f.close()

    graph = week4.de_bruijn_from_k_mers(k_mers)
    graph_string = week4.de_bruijn_graph_to_string(graph)
    
    g = open('output.txt', 'w')
    g.write(graph_string)
    g.close()
    
    
if __name__ == '__main__':
    main()
