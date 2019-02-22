def coin_change_caller(target,coins):
    cache = [None] * (target+1)
    return(coin_change(target, coins, cache))
def coin_change(target, coins, cache):
    min_coins = target
    if target in coins:
        return 1
    if cache[target] != None:
        return cache[target]
    else:
        for value in coins:
            if value <= target:
                num_coins = coin_change(target - value, coins, cache) + 1
                min_coins = min(min_coins, num_coins)
                cache[target] = min_coins
    return cache[target]

coin_change_caller(18,[1,2,5,10])