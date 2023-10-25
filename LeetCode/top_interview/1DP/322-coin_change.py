#this is using bottom-up approach and it is not intuitive for me
class Solution:
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        return dp[amount] if dp[amount] != amount+1 else -1


#this revision was done on 09-10-2023
#this is using top down approach and find it intuitive
class Solution:
    def coinChange(self, coins, amount):
        INF = float('inf')
        cache = {}
        def backtrack(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return INF

            if rem in cache:
                return cache[rem]

            min_coins = INF
            for coin in coins:
                min_coins = min(min_coins, 1 + backtrack(rem-coin))

            cache[rem] = min_coins
            return cache[rem]

        res = backtrack(amount) 
        return -1 if res == INF else res


class Solution:
    def coinChange(self, coins, amount):
        INF = float('inf')
        cache = {}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return INF
            if rem in cache:
                return cache[rem]

            minimum = INF
            for coin in coins:
                minimum = min(minimum, 1 + dfs(rem-coin))
            cache[rem] = minimum

            return minimum
        res = dfs(amount)
        return res if res != INF else -1


class Solution:
    def coinChange(self, coins, amount):
        INF = float('inf')
        cache = [INF]*(amount+1)
        cache[0] = 0

        for rem in range(1, amount+1):
            for coin in coins:
                if rem-coin >= 0:
                    cache[rem] = min(cache[rem], 1 + cache[rem-coin])

        res = cache[amount]
        return res if res != INF else -1


s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
print(s.coinChange([2147483647], 0))

