##################################
#
# Solve the Eulerian Path Problem.
#    Input: The adjacency list of a directed graph that has an Eulerian path.
#    Output: An Eulerian path in this graph.
#
# Sample Input:
#    0 -> 2
#    1 -> 3
#    2 -> 1
#    3 -> 0,4
#    6 -> 3,7
#    7 -> 8
#    8 -> 9
#    9 -> 6
#
# Sample Output:
#    6->7->8->9->6->3->0->2->1->3->4
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
    path = week4.eulerian_path(graph)
    graph_string = week4.cycle_to_string(path)
    
    g = open('output.txt', 'w')
    g.write(graph_string)
    g.close()
    
    
if __name__ == '__main__':
    main()
