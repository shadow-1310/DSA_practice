class Solution:
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            print(n)
            n = n & (n-1)
            count += 1

        return count

s = 101100001
so = Solution()
print(so.hammingWeight(s))
