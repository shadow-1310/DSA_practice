#this problem was asked in Mercari Japan OA
# done on 15-10-2023
class Solution:
    def getMaximumMex(self, arr, x):
        for i,num in enumerate(arr):
            while num >= x:
                num = num % x
            arr[i] = num

        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        min_freq = count[arr[0]]
        min_num = arr[0]
        for key in count:
            if count[key] < min_freq:
                min_freq = count[key]
                min_num = key

        mex = min_num + x * min_freq
        return mex

s = Solution()
print(s.getMaximumMex([0,1,2,1,3], 3))
