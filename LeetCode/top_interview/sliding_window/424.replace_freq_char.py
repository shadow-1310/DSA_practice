#optimized approach with time complexity O(26*N) = O(N)
def find_longest(s, k):
    def find_highest_freq(dic):
        max_freq = 0
        for key in dic:
            value = dic[key]
            max_freq = max(value, max_freq)
        
        return max_freq
    
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

        tot = right - left + 1
        max_freq = find_highest_freq(freq_map)

        if tot - max_freq <= k:
            res = max(res, tot)

        else:
            freq_map[s[left]] -= 1
            left += 1

        right += 1

    return res

s = "ABAB"
k = 2

s2 = "AABABBA"
k2 = 1

print(find_longest(s, k))
print(find_longest(s2, k2))