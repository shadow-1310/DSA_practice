#this problem is based on divide and conquer
# the following approach is wrong
def find_substring(s, k):
    def check(dic, k):
        for key in dic:
            if dic[key] < k:
                return False
        
        return True
    
    left = 0
    right = 0
    curr = 0
    res = 0
    freq_map = {}

    while left <= right and right < len(s):
        char = s[right]
        if char not in freq_map:
            freq_map[char] = 1
        else:
            freq_map[char] += 1

        curr = right - left + 1

        if check(freq_map, k):
            res = max(res, curr)
        else:
            freq_map[s[left]] -= 1
            left += 1

        right += 1

    return res


s = "aaabb"
k = 3

print(find_substring(s, k))