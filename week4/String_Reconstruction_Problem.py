##################################
#
# Solve the String Reconstruction Problem.
#    Input: The adjacency list of a directed graph that has an Eulerian path.
#    Output: An Eulerian path in this graph.
#
# Sample Input:
#    CTT -> TTA
#    ACC -> CCA
#    TAC -> ACC
#    GGC -> GCT
#    GCT -> CTT
#    TTA -> TAC
#
# Sample Output:
#    GGCTTACCA
#
################################## 

import week4

def main():
    f = open('input.txt', 'r')
    
    adj = []
    for line in f:
        adj.append(line.rstrip())
        
    f.close()

    graph = week4.adjacency_list_to_graph(adj)
    text = week4.string_reconstruction(graph)
    
    g = open('output.txt', 'w')
    g.write(text + "\n")
    g.close()
    
    
if __name__ == '__main__':
    main()
