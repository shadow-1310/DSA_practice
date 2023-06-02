# this is first attempt on 02-06-2023 . This is correct solution
# the main idea is to map the string for its character frequency then iterate through the string again and divide the string into two parts 
# at position where a character having less frequency than k occurs then recurssively call on both two segments
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 0 or k == 1:
            return len(s)
        
        if len(s) == 0 or k > len(s):
            return 0

        freq_map = {}

        for i in range(len(s)):
            if s[i] not in freq_map:
                freq_map[s[i]] = 1
            else:
                freq_map[s[i]] += 1

        s1, s2 = 0, 0

        for i  in range(len(s)):
            if freq_map[s[i]] < k:
                s1 = self.longestSubstring(s[:i], k)
                s2 = self.longestSubstring(s[i+1:], k)
                return max(s1, s2)      
        
        return len(s)
    
    
s1 = 'k'
k1 = 1

s2 = 'jjlk'
k2 = 2

s3 = "weitong"
k3 = 2

s = Solution()

print(s.longestSubstring(s1, k1))
print(s.longestSubstring(s2, k2))
print(s.longestSubstring(s3, k3))