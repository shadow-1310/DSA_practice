# this gives wrong results
def trial(arr:list[int], n:int, k:int) -> int:
    hash_map = {}
    pairs = 0
    for index, num in enumerate(arr):
        diff = k - num
        if diff in hash_map:
            pairs += 1
            hash_map[num] = index
        else:
            hash_map[num] = index
    return pairs


# trying the correct method
def count_pairs(arr:list[int], n:int, k:int) -> int:
    freq_map = {}
    count_pair = 0
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    for num in arr:
        diff = k - num
        if diff in freq_map:
            count_pair += freq_map[diff]
            if k - num == num:
                count_pair -= 1
    return count_pair // 2
        
test = [1, 5, 7, 1]
k = 6
n = 4
print(count_pairs(test, n, k))