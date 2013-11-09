##################################
#
# Minimum Skew Problem: Find a position in a genome minimizing the skew.
#    Input: A DNA string Genome.
#    Output: All integer(s) i minimizing Skew(Prefixi (Text)) 
#            among all values of i (from 0 to |Genome|).
#
# Sample Input:
#    TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
#
# Sample Output:
#    11 24
#
################################## 

def value(nuc):
    return {
        'G': 1,
        'C': -1,
    }.get(nuc, 0)

def solve(dna):

    pos = []
    
    skew = 0
    min_skew = skew

    for idx in range(len(dna)):
    
        val = value(dna[idx])
        if val == 0:
            continue
            
        skew += val
        if skew < min_skew:
            min_skew = skew  
            pos = [idx + 1]  
        elif skew == min_skew:
            pos.append(idx + 1)
                
    sol = ""
    for idx in pos:
        sol += str(idx) + " "             

    f = open('output.txt', 'w')
    f.write(sol + '\n')
    f.close()

def main():
    f = open('input.txt', 'r')
    dna = f.readline()
    f.close()

    solve(dna)
    
if __name__ == '__main__':
    main()
