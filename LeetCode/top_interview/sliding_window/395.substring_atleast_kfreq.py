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

#this is a revision. it is a correct solution done on 11-06-2023.
# mistake I did was calling the function on right and left segments, I have to exclude the character and remember the edge cases
def longest_substring(s, k):
    if len(s) == 0 or k > len(s):
        return 0
    
    if k == 1 or k == 0:
        return len(s)
    
    def find_length(s, k):
        if len(s) == 0 or k > len(s):
            return 0
        
        count_map = {}
        for char in s :
            if char in count_map:
                count_map[char] += 1
            else:
                count_map[char] = 1

        break_point = -1
        flag = True

        for i in range(len(s)):
            if count_map[s[i]] < k:
                break_point = i
            else:
                flag = False
        
        if flag:
            return 0

        if break_point == -1:
            return len(s)
            
        max_left = find_length(s[:break_point], k)
        max_right = find_length(s[break_point+1:], k)

        return max(max_left, max_right)
    
    return find_length(s, k)

s1 = "aaabb"
k1 = 3

s2 = "bbaaacbd"
k2 = 3

print(find_substring(s1, k1))
print(longest_substring(s2, k2))