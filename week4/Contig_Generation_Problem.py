##################################
#
# Generate the contigs from a collection of reads (with imperfect coverage).
#    Input: A collection of k-mers Patterns.
#    Output: All contigs in DeBruijn(Patterns).
#    
# Sample Input:
#    ATG
#    ATG
#    TGT
#    TGG
#    CAT
#    GGA
#    GAT
#    AGA
#    
# Sample Output:
#    AGA ATG ATG CAT GAT TGGA TGT
#
################################## 

import week4

def main():
    f = open('input.txt', 'r')
    
    k_mers = []
    for line in f:
        k_mers.append(line.rstrip())
        
    f.close()

    contigs = week4.generate_contigs_from_reads(k_mers)
    sol = " ".join(contigs)  
    
    g = open('output.txt', 'w')
    g.write(sol + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
