##################################
#
# Solve the Longest Path in a DAG Problem.
#    Input: An integer representing the source node of a graph, followed by an integer representing the sink
#    node of the graph, followed by a list of edges in the graph. The edge notation 0->1:7 indicates that
#    an edge connects node 0 to node 1 with weight 7.
#    Output: The length of a longest path in the graph.
#    
# Sample Input:
#    0
#    4
#    0->1:7
#    0->2:4
#    2->3:2
#    1->4:1
#    3->4:3
#    
# Sample Output:
#    9
#    0->2->3->4
#     
################################## 

import week6

def main():
    f = open('input.txt', 'r')
    
    src  = f.readline().strip()
    sink = f.readline().strip()
    
    adj = []
    for line in f:
        adj.append(line.strip())
    
    f.close()

    graph = week6.adjacency_list_to_graph(adj)
    sol = week6.dag_longest_path(graph, src, sink)
    
    g = open('output.txt', 'w')
    g.write(str(sol['length']) + '\n')
    g.write('->'.join(map(str, sol['path'])) + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
