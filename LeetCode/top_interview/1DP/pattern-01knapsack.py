class Solution:
    def maxProfit(self, values, weights, n, w):
        cache = {}
        def dfs(index, curr_w, curr_p):
            if curr_w == w:
                return curr_p
            if index == len(values) and curr_w <= w:
                return curr_p
            if curr_w > w:
                return 0

            if (index, curr_w) in cache:
                return cache[(index, curr_w)]

            res = max(dfs(index+1, curr_w, curr_p), dfs(index+1, curr_w+weights[index], curr_p+values[index]))
            cache[(index, curr_w)] = res

            return res

        return dfs(0, 0, 0)

# ws = [6,1,5,3]
# vs = [3,6,1,4]
# n = 4; w=10

n=5;w=100
ws = [20, 24, 36, 40, 42]
vs = [12, 35, 41, 25, 32]

s = Solution()
print(s.maxProfit(vs, ws, n, w))

