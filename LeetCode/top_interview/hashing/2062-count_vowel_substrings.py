class Solution:
    def countVowelSubstrings(self, word):
        res = 0
        n = len(word)
        for start in range(n):
            curr = [0]*5
            for end in range(start, n):
                if word[end] == 'a':
                    curr[0] += 1
                elif word[end] == 'e':
                    curr[1] += 1
                elif word[end] == 'i':
                    curr[2] += 1
                elif word[end] == 'o':
                    curr[3] += 1
                elif word[end] == 'u':
                    curr[4] += 1
                else:
                    break
                check = 0
                for count in curr:
                    if count:
                        check += 1
                if check == 5:
                    res += 1

        return res
        

s = Solution()
word1 = "unicornarihan"
word2 = "cuaieuouac"
print(s.countVowelSubstrings(word1))
print(s.countVowelSubstrings(word2))
