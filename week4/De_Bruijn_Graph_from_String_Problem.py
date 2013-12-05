##################################
#
# Solve the De Bruijn Graph from a String Problem.
#     Input: An integer k and a string Text.
#     Output: DeBruijnk(Text).
#
#   Sample Input:
#        4
#        AAGATTCTCTAC
#
#   Sample Output:
#        AAG -> AGA
#        AGA -> GAT
#        ATT -> TTC
#        CTA -> TAC
#        CTC -> TCT
#        GAT -> ATT
#        TCT -> CTA,CTC
#        TTC -> TCT
#
################################## 

import week4

def main():
    f = open('input.txt', 'r')
    k = f.readline().rstrip()
    text = f.readline().rstrip() 
    f.close()

    graph = week4.de_bruijn_from_string(text, k)
    graph_string = week4.de_bruijn_graph_to_string(graph)
    
    g = open('output.txt', 'w')
    g.write(graph_string)
    g.close()
    
    
if __name__ == '__main__':
    main()
