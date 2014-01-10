def reversal(lst, x, idx, pred = False):

    idx += 1
    x   -= 1

    sub = lst[x : idx] 
    lst = lst[:x] + sub[::-1] + lst[idx:]

    if pred:
        for i in range(x,idx):
            lst[i] = not lst[i]    

    return lst

def perm_string(perm, isNeg):
    
    sz = len(perm) - 1

    s = "("
    for i in range(sz):

        if isNeg[i]: s += '-'
        else:        s += '+'
    
        s += str(perm[i]) + ' '

    if isNeg[sz]: s += '-'
    else:         s += '+'
    
    s += str(perm[sz]) + ')'
    return s    

def greedy_sorting(perm):

    ret = ""

    isNeg = []
    p = []

    for x in perm.split():
        val = int(x)
        isNeg.append(val < 0)
        p.append(abs(val)) 

    for x in range(1, len(p)+1):
        
        idx = p.index(x)

        if idx != (x-1):
            isNeg = reversal(isNeg, x, idx, True)
            p     = reversal(p, x, idx)
            ret += perm_string(p, isNeg) + "\n"           

        if isNeg[x-1]:
            isNeg[x-1] = False
            ret += perm_string(p, isNeg) + "\n"
    
    return ret
    
            
           
