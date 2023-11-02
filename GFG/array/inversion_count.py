# brute force approach using 2 loops
def brute(arr:list, n:list):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

a = [2, 4, 1, 3, 5]
n = 5
print(brute(a, n))

# optimized solution using merge sort
def merge_sort(arr:list):
    count_inv = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        count_inv += merge_sort(left_arr)
        count_inv += merge_sort(right_arr)

        i = 0 # idx of left_arr
        j = 0 # idx for right_arr
        k = 0 # idx for sorted arr

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                count_inv += len(left_arr) - i
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return count_inv


#revision done on 02-11-2023
class Solution:
    def inversionCount(self, arr, n):
        def merge(nums):
            count_inv = 0
            n = len(nums)
            if n <= 1:
                return count_inv
            mid = len(nums) >> 1
            left = nums[:mid]
            right = nums[mid:]
            count_inv += merge(left)
            count_inv += merge(right)

            l = 0
            r = 0
            i = 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    nums[i] = left[l]
                    l += 1

                else:
                    nums[i] = right[r]
                    r += 1
                    count_inv += len(left) - l
                i += 1

            while l < len(left):
                nums[i] = left[l]
                l += 1
                i += 1

            while r < len(right):
                nums[i] = right[r]
                r += 1
                i += 1

            return count_inv

        return merge(arr)



test1 = [10, 10, 10]
test2 = [2, 4, 1, 3, 5]
# print("test case1 before sorting: ",test1)
# print("inversion count: ",merge_sort(test1))
# print("test case 1 after sorting: ",test1)
# print("\n")
# print("test case2 before sorting: ",test2)
# print("inversion count: ",merge_sort(test2))
# print("test case 2 after sorting: ",test2)
s = Solution()
print(s.inversionCount(test1, len(test1)))
print(s.inversionCount(test2, len(test2)))
