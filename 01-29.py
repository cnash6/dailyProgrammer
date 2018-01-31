import itertools

def do_it(str_in, str_out):
    coins = str_in.split(" ")[1:]
    target = coins[0]
    coins = coins[1:]
    combos = []
    outs = str_out.split(" ")
    lens = [alen for alen in range(len(coins))[2:] if eval(str(alen) + outs[-2] + outs[-1])]

    print()
    print("Target: " + str(target))
    print("Coins: " + str(coins))


    for perms in [itertools.permutations(coins, x) for x in lens]:
        for perm in perms:
            if sum([int(x) for x in perm]) == int(target) and sorted(perm) not in combos:
                combos.append(sorted(perm))
     
    if (len(combos) > 0):
        print("Valid combos found: ")
        for combo in combos: 
            print(combo)
        print("Min coins needed: " + str(len(min(combos, key=len))))
    else:
        print("No valid combos found")

do_it("Input: 10 5 5 2 2 1", "Output: n <= 3")

do_it("Input: 150 100 50 50 50 50", "Output: n < 5")

do_it("Input: 130 100 20 18 12 5 5", "Output: n < 6")

do_it("Input: 200 50 50 20 20 10", "Output: n >= 5")