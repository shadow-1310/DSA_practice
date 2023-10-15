#this question was asked in Mercari Japan OA
#done on 15-10-2023
class Solution:
    def countSentences(self, words, sentences):
        word_map = {}
        for word in words:
            curr = [0]*26
            for char in word:
                idx = ord(char) - ord('a')
                curr[idx] += 1
            curr = tuple(curr)
            if curr in word_map:
                word_map[curr] += 1
            else:
                word_map[curr] = 1

        res = []
        for sent in sentences:
            all_words = sent.split()
            temp = 1
            for word in all_words:
                curr = [0]*26
                for char in word:
                    idx = ord(char) - ord('a')
                    curr[idx] += 1
                curr = tuple(curr)
                temp *= word_map[curr]
            res.append(temp)

        return res

s = Solution()
words = ['listen', 'silent', 'it', 'is']
sents = ['listen it is silent']
print(s.countSentences(words, sents))
