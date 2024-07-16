class Solution:
    def hIndex(self, citations):
        max_cite = max(citations)
        bucket = [0]*(max_cite+1)
        for cite in citations:
            for i in range(1, cite+1):
                bucket[i] += 1

        # print(bucket)
        for i in range(max_cite, 0, -1):
            if bucket[i] >= i:
                return i
        return 0

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        n = len(citations)
        if n == 1 and citations[0]:
            return 1
        if citations[-1] >= n:
            return n
        for i, cite in enumerate(citations):
            if i >= cite:
                return i
        return 0

citations = [3,0,6,1,5]
s = Solution()
print(s.hIndex(citations))
citations = [1,3,1]
print(s.hIndex(citations))
