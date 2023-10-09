#revision done on 09-10-2023
class Solution:
    def maxProfit(self, prices):
        cache = {}
        def backtrack(index, buying):
            if index >= len(prices):
                return 0
            if (index, buying) in cache:
                return cache[(index, buying)]

            if buying:
                buy = backtrack(index+1, not buying) - prices[index]
                cd = backtrack(index+1, buying)
                cache[(index, buying)] = max(buy, cd)

            else:
                sell = backtrack(index+2, not buying) + prices[index]
                cd = backtrack(index+1, buying)
                cache[(index, buying)] = max(sell, cd)

            return cache[index,buying]

        return backtrack(0, True)


s = Solution()
print(s.maxProfit([1,2,3,0,2]))
print(s.maxProfit([1]))
