##################################
#
# Solve the Overlap Graph Problem (restated below)
#     Input: A collection Patterns of k-mers.
#     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
#
#   Sample Input:
#       ATGCG
#       GCATG
#       CATGC
#       AGGCA
#       GGCAT
#
#   Sample Output:
#       AGGCA -> GGCAT
#       CATGC -> ATGCG
#       GCATG -> CATGC
#       GGCAT -> GCATG
#
################################## 

import week4

def main():
    f = open('input.txt', 'r')
    
    k_mers = []
    for line in f:
        k_mers.append(line.rstrip())
        
    f.close()

    graph = week4.overlap_graph(k_mers)
    graph_string = week4.graph_to_string(graph)
    
    g = open('output.txt', 'w')
    g.write(graph_string)
    g.close()
    
    
if __name__ == '__main__':
    main()
