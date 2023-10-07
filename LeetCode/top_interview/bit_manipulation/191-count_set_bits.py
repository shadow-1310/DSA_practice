class Solution:
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            print(n)
            n = n & (n-1)
            count += 1

        return count


#revision done 07-10-2023
class Solution:
    def hammingWeight(self, n):
        res = 0
        while n:
            n &= (n-1)
            res += 1

        return res

s = 101100001
so = Solution()
print(so.hammingWeight(s))
