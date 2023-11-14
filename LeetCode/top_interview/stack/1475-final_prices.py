class Solution:
    def finalPrices(self, prices):
        res = prices
        stack = []
        for i, p in enumerate(prices):
            while stack and p <= stack[-1][-1]:
                index, _ = stack.pop()
                res[index] -= p
            stack.append([i,p])

        return res

s = Solution()
prices = [8,4,6,2,3]
print(s.finalPrices(prices))
prices = [1,2,3,4,5]
print(s.finalPrices(prices))
prices = [10,1,1,6]
print(s.finalPrices(prices))
