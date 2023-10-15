#this question was asked in Mercari_Japan test
#first done on 15-10-2023, not optimized
class Solution:
    def maxXor(self, lo, hi, k):
        res = 0
        for i in range(lo, hi+1):
            for j in range(i+1, hi+1):
                curr = i^j
                if curr <= k:
                    res = max(res, curr)
        return res


s = Solution()
print(s.maxXor(3,5,6))
print(s.maxXor(1,3,3))
