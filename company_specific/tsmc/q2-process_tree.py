#this was asked in TSMC OA in IIT Delhi
class Solution:
    def find_parent(self, process):
        if process == 2:
            return 1
        parent = 2
        last_child = 4
        while True:
            if process <= last_child:
                return parent
            parent += 1
            last_child += parent


s = Solution()
print(s.find_parent(6))
print(s.find_parent(10))
print(s.find_parent(12))
