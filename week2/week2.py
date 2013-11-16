
# complement of nucleotide 
def complement(nuc):
    return {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }.get(nuc, "")

def loadRNA_codon_table():
    table = {}
    
    f = open('RNA_codon_table.txt', 'r')
    while True:
        line = f.readline().rstrip()
        if not line: break
        
        data = line.split()
        if len(data) == 2:
            table[data[0]] = data[1]
        else:
            table[data[0]] = ""
            
    f.close()
    return table
    
# Translate an RNA string into an amino acid string.    
def translate_rna_to_amino_acid(rna):
    ret = ""
    translation_table = loadRNA_codon_table()
    
    sz = len(rna)
    if sz%3 != 0:
        print "rna length ain't divide by 3..."
        
    sz = sz - sz%3 
    idx_s = 0
    idx_e = 3
       
    for i in range(sz/3):
        ret += translation_table[rna[idx_s:idx_e]]
        
        idx_s = idx_e
        idx_e += 3
        
    return ret






    
        
