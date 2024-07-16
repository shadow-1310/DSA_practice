def countUnorderedTriplets(nums1, nums2):
    N = len(nums1)
    BIT = [0] * (N+1)
    num1_index = [0] * (N+1)
    num2_index = [0] * (N+1)
    
    # Mapping elements of nums1 to their indices
    for i, num in enumerate(nums1):
        num1_index[num] = i
    
    # Mapping elements of nums2 to their indices
    for i, num in enumerate(nums2):
        num2_index[num] = i
    
    nums = [0] * (N+1)
    
    # Mapping elements of nums1 to their corresponding indices in nums2
    for i, index in enumerate(num1_index):
        nums[index] = num2_index[i]
    
    # Function to calculate the lowest set bit
    def lowbit(i):
        return i & (-i)
    
    # Function to update the BIT
    def add(i):
        i += 1
        while i <= N:
            BIT[i] += 1
            i += lowbit(i)
    
    # Function to query the BIT for the sum of elements from 0 to i
    def query(i):
        i += 1
        result = 0
        while i:
            result += BIT[i]
            i -= lowbit(i)
        return result
    
    smaller = []
    bigger = []
    
    for i, n in enumerate(nums):
        smaller.append(query(n))
        bigger.append(N - 1 - i - n + smaller[-1])
        add(n)
    
    # Calculate the sum of products of smaller and bigger lists
    result = sum(s * b for s, b in zip(smaller, bigger))
    
    return result


A = [4, 1, 3, 2]
B = [1, 4, 3, 2] 
