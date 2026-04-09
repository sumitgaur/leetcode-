'''
array of coins with denomiations and target amount
use minimum number of coins to meet the target amount
Input = [1,2,5], amount = 11
5+2+2+2=11 // 4 coins
5+5+1 // 3 coins

11
sort coins denominations
[1,2,5]   11
[1,2]     11-2*5 = 1  coins = 2
[1]       1           coins =2
[]        1-1*1 = 0    coins = 3
---- till target = 0
dp[i]  = = min coin required tp make amount i
dp[0]=0
dp[i] = intmax for all
dp[i] = min(dp[i],dp[i-coin]+1)


'''
from collections import defaultdict


def min_coins_meet_target(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def min_coins_meet_target(coins, target):
    memo = defaultdict(list)

    def do(target):
        if target in memo:
            return memo[target]
        if target == 0:
            return []
        if target < 0:
            return None

        ans = None
        for coin in coins:
            res = do(target - coin)
            if res is not None:
                com = res + [coin]
                if ans is None or len(com) < len(ans):
                    ans = com
        memo[target] = ans
        return ans

    res = do(target)
    return -1 if res == float('inf') else res


#
# assert min_coins_meet_target([1, 2, 5], 11) == 3
# assert min_coins_meet_target([1, 2, 5], 10) == 2
# assert min_coins_meet_target([1, 2, 5], 1) == 1
# assert min_coins_meet_target([2, 3, 5], 1) == -1
# assert min_coins_meet_target([2, 3, 5], 9) == 3
print(min_coins_meet_target([2, 5, 10, 20], 99))  # 20*4 + 10*1 + 5*1+2*2 = 8
print(min_coins_meet_target([7, 13, 19], 100))  # 19x3 + 13x1 + 7x4  -> 10
print(min_coins_meet_target([1, 2, 5, 10, 20, 50], 9317))  # 19x3 + 13x1 + 7x4  -> 10
