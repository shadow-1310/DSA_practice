#it is done on 2023-09-30, perfectly woring on LC testcases
class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(31, -1, -1):
            bit = n & 1
            n = n >> 1
            res = res | (bit << i)

        return res
