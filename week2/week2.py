# complement of nucleotide 
def complement(nuc):
    return {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }.get(nuc, "")
    
def reverseString(s):
    return s[::-1]

# the reverse complement of Pattern
def dna_complement(dna):
    cdna = ""

    for nuc in dna:
        cdna += complement(nuc) 
        
    return reverseString(cdna)    

# Find all occurrences of a pattern in a string
# brute force
def bf_pattern_matching(string, pat):
    pos = []
    idx = -1

    while True:
        idx = string.find(pat, idx + 1)

        if idx < 0:
            break;
        else:
            pos.append(idx)

    return pos

def load_rna_codon_table(br_delimiter = ""):
    table = {}
    
    f = open('RNA_codon_table.txt', 'r')
    while True:
        line = f.readline().rstrip()
        if not line: break
        
        data = line.split()
        if len(data) == 2:
            table[data[0]] = data[1]
        else:
            table[data[0]] = br_delimiter
            
    f.close()
    return table
    
def load_integer_mass_table():
    table = {}
    
    f = open('integer_mass_table.txt', 'r')
    while True:
        line = f.readline().rstrip()
        if not line: break
        
        data = line.split()
        if len(data) == 2:
            table[data[0]] = int(data[1])
        else:
            raise Exception("bad data format")
            
    f.close()
    return table    

def rna_to_amino_conversion_rate():
    return 3
    
# Translate an RNA string into an amino acid string.    
def translate_rna_to_amino_acid(rna, frame = 0, br_delimiter = ""):
    rate = rna_to_amino_conversion_rate()
    if frame < 0 or frame >= rate:
        raise Exception("frame out of bound")

    ret = ""
    translation_table = load_rna_codon_table(br_delimiter)
    
    sz = len(rna) - frame
    sz = sz - sz%rate
    
    idx_s = 0 + frame
    idx_e = rate + frame
       
    for i in range(sz/rate):
        ret += translation_table[rna[idx_s:idx_e]]
        
        idx_s = idx_e
        idx_e += rate
        
    return ret

# transforms a DNA string into an RNA string 
# by replacing all occurrences of T with U
def dna_to_rna(dna):
    rna = ""
    
    for nuc in dna:
        if nuc == 'T':
            rna += 'U'
        else:
            rna += nuc
        
    return rna
    
def peptide_encoding_iter(dna, pep, complement = False): 
    rate = rna_to_amino_conversion_rate()
       
    strings = []
    sz = rate * len(pep)
    rna  = dna_to_rna(dna)
    
    for frame in range(rate):
        amino  = translate_rna_to_amino_acid(rna, frame, " ") 
        dna_pos_3 = bf_pattern_matching(amino , pep)
        dna_pos_3 = [rate*x + frame for x in dna_pos_3]
        
        if complement:
            strings += [dna_complement(dna[x:x+sz]) for x in dna_pos_3]
        else:
            strings += [dna[x:x+sz] for x in dna_pos_3]
        
    return strings
    
# Find substrings of a genome encoding a given amino acid sequence. 
# DNA string Pattern encodes an amino acid string Peptide if 
# the RNA string transcribed from either Pattern or its reverse complement 
# Pattern translates into Peptide.
def peptide_encoding(dna, pep):
    cdna = dna_complement(dna)
    
    strings  = peptide_encoding_iter(dna , pep)
    strings += peptide_encoding_iter(cdna, pep, True)
    
    return strings

def generate_subpeptides(pep):
    subpeptides = ['']
    sz = len(pep)
    
    loop_pep = pep + pep
    loop_range = range(0,sz)
    
    for length in range(1,sz):
        subpeptides += [loop_pep[idx:idx+length] for idx in loop_range]
        
    subpeptides.append(pep)
    return subpeptides     

def integer_mass(pep, integer_mass_table = None):
    if not integer_mass_table:
        integer_mass_table = load_integer_mass_table()
        
    mass = 0
    for atom in pep:
        mass += integer_mass_table[atom]
        
    return mass    

def cyclospectrum(pep):
    integer_mass_table = load_integer_mass_table()
    subpeptides = generate_subpeptides(pep)
    
    ret = []
    for sub in subpeptides:
        ret.append(integer_mass(sub, integer_mass_table))
    
    return ret
    
        
