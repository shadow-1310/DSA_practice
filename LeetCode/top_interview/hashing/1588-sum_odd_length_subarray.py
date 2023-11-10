#done on 10-11-2023
class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        res = 0
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += 1
                if curr & 1:
                    res += arr[j]
                    if j > 0:
                        res += arr[j-1]
        return res

#this is brute force approach
#done on 10-11-2023
class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        res = 0
        for i in range(1, n+1, 2):
            start = 0
            end = start + i
            while end < n+1:
                print(arr[start:end])
                res += sum(arr[start:end])
                start += 1
                end += 1
        return res


#this is a O(N) solution
class Solution:
    def sumOddLengthSubarrays(self, arr):
        res = 0
        n = len(arr)
        for i, num in enumerate(arr):
            tot = (n-i)*(i+1)
            if tot & 1:
                freq = (tot >> 1)+1
            else:
                freq = tot >> 1

            res += freq*num

        return res



arr = [1,4,2,5,3]
s = Solution()
print(s.sumOddLengthSubarrays(arr))
