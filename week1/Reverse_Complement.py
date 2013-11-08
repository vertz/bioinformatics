##################################
#
# Reverse Complement Problem: Reverse complement a nucleotide pattern.
#	Input: A DNA string Pattern.
# 	Output: @Pattern, the reverse complement of Pattern.
#
################################## 

def complement(nuc):
    return {
	'A': 'T',
        'T': 'A',
	'G': 'C',
        'C': 'G',
    }.get(nuc, "")

def reverseString(s):
	return s[::-1]

def solve(dna):
	cdna = ""

	for nuc in dna:
		cdna += complement(nuc)

	f = open('output.txt', 'w')
	f.write(reverseString(cdna) + '\n')
	f.close()

def main():
	f = open('Input.txt', 'r')
	dna = f.readline()
	f.close()

	solve(dna)
    
if __name__ == '__main__':
    main()
