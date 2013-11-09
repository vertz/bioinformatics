##################################
#
# Approximate Pattern Matching Problem: ind all approximate occurrences of a pattern in a string.
#    Input: Two strings Pattern and Text along with an integer d.
#    Output: All positions where Pattern appears in Text with at most d mismatches.
#
# Sample Input:
#    ATTCTGGA
#    CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
#    3
#
# Sample Output:
#    6 7 26 27
#
################################## 

def distance(pat, sub):
    sz = len(pat)
    if sz != len(sub):
        return sz
    
    d = 0  
    for idx in range(sz):
        if pat[idx] != sub[idx]:
            d += 1
            
    return d

def solve(dna, pat, d):
    pos = []
    dis = int(d)
    sz = len(pat)

    for idx in range(len(dna)):
        if distance(pat, dna[idx: idx + sz]) <= dis:
            pos.append(idx)
                
    sol = ""
    for idx in pos:
        sol += str(idx) + " "             

    f = open('output.txt', 'w')
    f.write(sol + '\n')
    f.close()

def main():
    f = open('input.txt', 'r')
    pat = f.readline().rstrip('\n')
    dna = f.readline().rstrip('\n')
    dis = f.readline().rstrip('\n') # distance
    f.close()

    solve(dna, pat, dis)
    
if __name__ == '__main__':
    main()
