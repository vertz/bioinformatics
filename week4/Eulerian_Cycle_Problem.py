##################################
#
# Solve the Eulerian Cycle Problem.
#     Input: The adjacency list of an Eulerian directed graph.
#     Output: An Eulerian cycle in this graph.
#
#   Sample Input:
#    0 -> 3
#    1 -> 0
#    2 -> 1,6
#    3 -> 2
#    4 -> 2
#    5 -> 4
#    6 -> 5,8
#    7 -> 9
#    8 -> 7
#    9 -> 6
#
#   Sample Output:
#    6->8->7->9->6->5->4->2->1->0->3->2->6
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
    cycle = week4.eulerian_cycle(graph)
    graph_string = week4.cycle_to_string(cycle)
    
    g = open('output.txt', 'w')
    g.write(graph_string)
    g.close()
    
    
if __name__ == '__main__':
    main()
