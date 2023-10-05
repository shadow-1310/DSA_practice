class Solution:
    def lastNon0Digit(self, N):
        def helper(num, res, count5):
            n = num
            if n == 1:
                for i in range(count5):
                    res = (res * 5) % 10
                return res

            while n % 5 == 0:
                n = n // 5
                count5 += 1

            while count5 >= 1 and n & 1 == 0:
                n >>= 1
                count5 -= 1

            res = (res * (n % 10)) % 10

            return helper(num-1, res, count5)

        return helper(N, 1, 0)


s = Solution()
print(s.lastNon0Digit(100))
