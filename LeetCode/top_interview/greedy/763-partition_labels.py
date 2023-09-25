class Solution:
    def partitionLabels(self, s):
        res = []
        hashmap = {}
        
        for index, char in enumerate(s):
            if char not in hashmap:
                hashmap[char] = index

            else: 
                hashmap[char] = index

        end = 0
        size = 0
        for index, char in enumerate(s):
            size += 1
            end = max(hashmap[char], end)
            if index == end:
                res.append(size)
                size = 0
        
        return res
