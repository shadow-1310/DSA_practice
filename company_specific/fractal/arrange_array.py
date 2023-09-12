#this is a two pointer approach done on 11-09-2023 but not working for GFG testcases
class Solution:
    def Rearrange(self, n, arr):
        left = 0
        curr = left

        while curr <= n -1 and left <= n -1:
            if arr[curr] < 0:
                arr[left], arr[curr] = arr[curr], arr[left]
                left += 1

            curr += 1


#this is a brute force approach done on 11-09-2023 which is woring for all testcases on GFG
class Solution:
    def Rearrange(self, n, arr):
        pos = []
        neg = []

        for i in range(n):
            if arr[i] < 0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])

        idx = 0
        i = 0
        while idx < len(neg):
            arr[idx] = neg[i]
            idx += 1
            i += 1

        i = 0
        while idx < n and i < len(pos):
            arr[idx] = pos[i]
            idx += 1
            i += 1

#this is two pointer approach, time complexity O(1) but failing in time limit for GFG testcase-1112
class Solution:
    def Rearrange(self, n ,arr):
        left = 0
        curr = left

        while curr < n:
            if arr[curr] >= 0:
               curr += 1 
            else:
                for i in range(curr, left, -1):
                    arr[i-1], arr[i] = arr[i], arr[i-1]

                curr += 1
                left += 1


