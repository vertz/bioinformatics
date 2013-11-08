##################################
#
# Clump Finding Problem: Find patterns forming clumps in a string.
#    Input: A string Genome, and integers k, L, and t.
#    Output: All distinct k-mers forming (L, t)-clumps in Genome.
#
# Sample Input:
#    CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
#    5 50 4
#
################################## 


def solve_k_mers(gen, k, t):
    k_mers = []
    
    k_val = int(k)
    t_val = int(t)
    
    k_range = len(gen) - k_val

    for idx in range(k_range):
        s = gen[idx:idx+k_val]

        if s in k_mers:
            continue

        tmp = gen.count(s,idx)

        if tmp >= t_val:
            k_mers.append(s)
            
    return k_mers
    
def pattern_matching(gen, pat):
    idx = -1
    pat_lst = []
        
    while True:
        idx = gen.find(pat, idx + 1)

        if idx < 0:
            break;
        else:
            pat_lst.append(idx)

    return pat_lst

def solve(gen, k, L, t):

    k_mers = solve_k_mers(gen, k, t)
    
    t_val = int(t)
    L_val = int(L)
         
    pos = {}
    for pat in k_mers:
        pos[pat] = pattern_matching(gen, pat)
        
    sol = []
    for pat in k_mers:
        lst = pos[pat]
        for idx in range(len(lst) - t_val + 1):
            if (lst[idx] + L_val) >= lst[idx + t_val - 1]:
                sol.append(pat) 
                break  
    
    sol_s = ""
    for pat in sol:
        sol_s += str(pat) + " "

    f = open('output.txt', 'w')
    f.write(sol_s + '\n')
    f.close() 

def main():
    f = open('input.txt', 'r')
    gen = f.readline().rstrip('\n')
    parms = f.readline().rstrip('\n').split()
    f.close()

    if len(parms) != 3:
        raise Exception("wrong input")

    solve(gen, parms[0], parms[1], parms[2])
    
if __name__ == '__main__':
    main()
