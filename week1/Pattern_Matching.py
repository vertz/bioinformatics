##################################
#
# Pattern Matching Problem: Find all occurrences of a pattern in a string.
#    Input: Two strings, Pattern and Genome.
#    Output: All starting positions where Pattern appears as a substring of Genome.
#
################################## 


def solve(pat, gen):
    pos = []
    idx = -1

    while True:
        idx = gen.find(pat, idx + 1)

        if idx < 0:
	    break;
	else:
	    pos.append(idx)

    sol = ""
    for i in pos:
        sol += str(i) + " "

    f = open('output.txt', 'w')
    f.write(sol + '\n')
    f.close()

def main():
    f = open('input.txt', 'r')
    pat = f.readline().rstrip('\n')
    gen = f.readline().rstrip('\n')
    f.close()

    solve(pat, gen)
    
if __name__ == '__main__':
    main()
