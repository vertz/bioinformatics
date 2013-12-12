# Solve the Change Problem.
#    Input: An integer money and an array coins = (coin1, ..., coind).
#    Output: The minimum number of coins with denominations coins that changes money.        
def change_rec(money, coins, acc = 0):
    money = int(money)
    if money == 0:
        return acc
        
    min_coins = float("infinity")
    for coin in coins:
    
        if coin <= money:
            n_coins = change_rec(money - coin, coins, acc + 1)
            if n_coins < min_coins:
                min_coins = n_coins 
                
    return min_coins             

# Solve the Change Problem.
#    Input: An integer money and an array coins = (coin1, ..., coind).
#    Output: The minimum number of coins with denominations coins that changes money.
def change_mem(money, coins):
    money = int(money) 
    if money == 0:
        return 0
        
    mem_min_coins = [0]
    for m in range(money + 1):
    
        mem_min_coins.append(float("infinity")) 
        for coin in coins:
        
            if m >= coin:
                n_coins = mem_min_coins[m - coin] + 1
            
                if n_coins < mem_min_coins[m]:
                    mem_min_coins[m] = n_coins     
                
    return mem_min_coins[money]   
