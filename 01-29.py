import itertools

def do_it(coins, n):

    target = coins[0]
    coins = coins[1:]
    combos = []

    print("Target: " + str(target))
    print("Coins: " + str(coins))

    for perms in [itertools.permutations(coins, x+2) for x in range(2)]:
        for perm in perms:
            if sum(perm) == target and perm not in combos:
                combos.append(perm)
     
    if (len(combos) > 0):
        print("Valid combos found: ")
        for combo in combos: 
            print(combo)
        print("Min coins needed: " + str(len(min(combos, key=len))))
    else:
        print("No valid combos found")

do_it([10,5,5,2,2,1], 4)