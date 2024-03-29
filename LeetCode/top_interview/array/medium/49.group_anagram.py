def group_anagram(strs):
    result = {}
    for word in strs:
        count = [0]*26
        for char in word:
            count[ord(char) - ord('a')] += 1

        if tuple(count) not in result:
            result[tuple(count)] = [word]
        else:
            result[tuple(count)].append(word)

    return list(result.values())


#this is a revision donw on 10-09-2023, working proper on LC testcases
class Solution:
    def groupAnagrams(self, strs):
        sim_map = {}
        for word in strs:
            word_map = [0]*26
            for char in word:
                idx = ord(char) - ord('a')
                word_map[idx] += 1

            word_map = tuple(word_map)
            if word_map in sim_map:
                sim_map[word_map].append(word)

            else:
                sim_map[word_map] = [word]

        return list(sim_map.values())


class Solution:
    def groupAnagrams(self, strs):
        char_map = {}
        for word in strs:
            curr_word = [0]*26
            for char in word:
                idx = ord(char) - ord('a')
                curr_word[idx] += 1
            curr_word = tuple(curr_word)
            if curr_word in char_map:
                char_map[curr_word].append(word)
            else:
                char_map[curr_word] = [word]

        res = []
        for key in char_map:
            res.append(char_map[key])

        return res

    

strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

print(group_anagram(strs))
print(group_anagram(strs2))
print(group_anagram(strs3))
s = Solution()
print(s.groupAnagrams(strs))
print(s.groupAnagrams(strs2))
print(s.groupAnagrams(strs3))
