##################################
#
# Frequent Words Problem: Find the most frequent k-mers in a string.
#	Input: A string Text and an integer k.
# 	Output: All most frequent k-mers in Text.
#
################################## 


def solve(dna , k):
	k_val = int(k)
	k_range = len(dna) - k_val

	if k_range == 0:
		print dna
		return 
	elif k_range < 0:
		return 

	sol = []
	maxF = 0

	for i in range(k_range):
		sub_dna = dna[i:i+k_val]

		if sub_dna in sol:
			continue

		tmp = dna.count(sub_dna)

		if tmp > maxF:
			maxF = tmp
			sol = [sub_dna]
		elif tmp == maxF:
			sol.append(sub_dna)

	sol_s = ""
	for s in sol:
		sol_s += str(s) + " "	

	f = open('output.txt', 'w')
	f.write(sol_s + '\n')
	f.close()

def main():
	f = open('Input.txt', 'r')
	dna = f.readline().rstrip('\n')
	k = f.readline()  
	f.close()

	solve(dna , k)
    
if __name__ == '__main__':
    main()
