# Although the following approach works for initial test cases, it fails in basic concept

def find_longest(s):
    if len(s) == 1:
        return 1
    
    left = 0
    count_map = {}
    right = left
    max_count = 0
    count = 0

    while left <= right and right < len(s):
        if s[right] in count_map:
            if s[right] != s[right-1]:
                left = right - 1
                right = left
            else:
                left = right
            count = 0
            count_map = {}
        else:
            count_map[s[right]] = 1
            count += 1
            max_count = max(count, max_count)
            right += 1

    return max_count

# this is the correct approach, done on 30-05-2023
def find_longest(s):
    if len(s) == 1:
        return 1
    
    left = 0
    right = left
    seen_map = {}
    max_count = 0

    while left <= right and right < len(s):
        char = s[right]
        if char in seen_map and seen_map[char] >= left:
            left = seen_map[char] + 1
        
        seen_map[char] = right
        count = right - left + 1
        max_count = max(max_count, count)
        right += 1

    return max_count


# this is a revision on 02-06-2023
# mistake was forgot to include the condition pos_map[s[right]] >= left
def find_longest_ss(s):
    if len(s) == 1:
        return 1
    
    max_count = 0
    left = 0
    right = left
    pos_map = {}

    while right < len(s):
        if s[right] in pos_map and pos_map[s[right]] >= left:
            left = pos_map[s[right]] + 1
            pos_map[s[right]] = right
            
        else:
            pos_map[s[right]] = right

        count = right - left + 1
        max_count = max(max_count, count)
        right += 1
    
    return max_count


#this is a revision done on 06-09-2023, mistake made was putting the current len calculation inside the if loop
class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1
        left = 0
        right = left
        max_len = 0
        exist = {}

        while right < len(s):
            if s[right] in exist and exist[s[right]] >= left:
                left = exist[s[right]] + 1
            
            curr = right - left + 1
            exist[s[right]] = right
            max_len = max(curr, max_len)
            right += 1

        return max_len


#this is a revision done on 27-10-2023
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 1 or n == 0:
            return n
        l = 0
        r = 1
        seen = {}
        seen[s[l]] = 0
        res = 0
        while r < n:
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            res = max(res, r-l+1)
            r += 1

        return res


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "abba"
s5 = ""

s = Solution()
print(s.lengthOfLongestSubstring(s1))
print(s.lengthOfLongestSubstring(s2))
print(s.lengthOfLongestSubstring(s3))
print(s.lengthOfLongestSubstring(s4))
print(s.lengthOfLongestSubstring(s5))
