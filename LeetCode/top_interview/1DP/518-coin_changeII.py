#this is a wrong solution because it includes duplicates
class Solution:
    def change(self, amount, coins):
        cache = {}
        def backtrack(rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            if rem in cache:
                return cache[rem]

            ways = 0
            for coin in coins:
                ways += backtrack(rem-coin)

            cache[rem] = ways
            return ways

        return backtrack(amount)


class Solution:
    def change(self, amount, coins):
        cache = {}
        def backtrack(index, rem):
            if rem == 0:
                return 1
            if index == len(coins) or rem < 0:
                return 0
            if (index,rem) in cache:
                return cache[(index,rem)]

            left = backtrack(index, rem-coins[index])
            right = backtrack(index+1, rem)
            cache[(index, rem)] = left + right

            return (left+right)
        return backtrack(0, amount)

s = Solution()
print(s.change(5, [1,2,5]))
