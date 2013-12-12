##################################
#
# Solve the String Reconstruction from Read-Pairs Problem.
#    Input: An integer d followed by a collection of paired k-mers PairedReads.
#    Output: A string Text with (k, d)-mer composition equal to PairedReads.
#
# Sample Input:
#    2
#    GAGA|TTGA
#    TCGT|GATG
#    CGTG|ATGT
#    TGGT|TGAG
#    GTGA|TGTT
#    GTGG|GTGA
#    TGAG|GTTG
#    GGTC|GAGA
#    GTCG|AGAT
#
# Sample Output:
#    GTGGTCGTGAGATGTTGA
#
################################## 

import week4

def main():
    f = open('input.txt', 'r')
    
    d = f.readline().rstrip()
    
    read_pairs = []
    for line in f:
        read_pairs.append(line.rstrip())
        
    f.close()

    graph = week4.de_bruijn_from_read_pairs(read_pairs)
    text  = week4.string_reconstruction_from_read_pairs(graph, d)

    g = open('output.txt', 'w')
    g.write(text + '\n')
    g.close()
    
    
if __name__ == '__main__':
    main()
