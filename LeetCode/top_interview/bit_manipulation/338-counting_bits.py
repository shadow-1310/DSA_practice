class Solution:
    def countBits(self, n):
        res = []
        for num in range(n+1):
            count = 0
            while num > 0:
                num &= (num-1)
                count += 1
            res.append(count)

        return res


#it is a solution with O(N) as it uses DP approach with extra space
class Solution:
    def countBits(self, n):
        dp = [0] * (n+1)
        offset = 1
        for num in range(1, n+1):
            if offset * 2 == num:
                offset = num
            dp[num] = 1 + dp[num-offset]

        return dp
