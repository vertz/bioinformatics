##################################
#
# Solve the Change Problem.
#    Input: An integer money and an array coins = (coin1, ..., coind).
#    Output: The minimum number of coins with denominations coins that changes money.
#    
# Sample Input:
#    40
#    50,25,20,10,5,1
#    
# Sample Output:
#    2
#
################################## 

import week6

def main():
    f = open('input.txt', 'r')
    money = f.readline().rstrip()
    coins = f.readline().rstrip().split(",")
    f.close()

    coins = map(int, coins)
    sol = week6.change_mem(money, coins)
    
    g = open('output.txt', 'w')
    g.write(str(sol) + '\n')
    g.close()
    
if __name__ == '__main__':
    main()
