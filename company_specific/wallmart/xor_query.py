class segTree:
    def __init__(self, nums):
        self.size = len(nums)
        self.lazy = [0]*4*self.size
        self.tree = [0]*4*self.size
        self.build_tree(nums)
        pass

    def build_tree(self, nums):
        def helper(curr, low, high):
            if low == high:
                self.tree[curr] = nums[low]

            else:
                mid = (low+high) // 2
                helper(2*curr+1, low, mid)
                helper(2*curr+2, mid+1, high)
                self.tree[curr] = self.tree[2*curr+1] ^ self.tree[2*curr+2]

        helper(0, 0, self.size - 1)


    def lazy_update(self, l, r, v):
        def helper(curr, low, high):
            if self.lazy[curr] != 0:
                self.tree[curr] ^= self.lazy[curr]
                if low != high:
                    self.lazy[2*curr+1] ^= self.lazy[curr]
                    self.lazy[2*curr+2] ^= self.lazy[curr]
                self.lazy[curr] = 0

            if high < l or low > r:
                return None

            if l <= low and high <= r:
                self.tree[curr] ^= v
                if low != high:
                    self.lazy[2*curr+1] ^= v
                    self.lazy[2*curr+2] ^= v

            mid = (low+high) // 2
            left = helper(2*curr+1, low, mid)
            right = helper(2*curr+2, mid+1, high)
            if left and right:
                return left ^ right

            return left if not right else right

        helper(0, 0, self.size - 1)

    def get_all(self):
        updated_nums = []
        def helper(curr, low, high):
            if self.lazy[curr] != 0 and ((high-low+1) % 2) == 1:
                self.tree[curr] ^= self.lazy[curr]
                if low != high:
                    self.lazy[2*curr+1] ^= self.lazy[curr]
                    self.lazy[2*curr+2] ^= self.lazy[curr]

                self.lazy[curr] = 0

            
            if low == high:
                updated_nums.append(self.tree[curr])
                return
            
            mid = (low+high) // 2
            helper(2*curr+1, low, mid)
            helper(2*curr+2, mid+1, high)

        return updated_nums


    def get_query(self, l, r):
        def helper(curr, low, high):
            if self.lazy[curr] != 0 and ((high-low+1) % 2) == 1:
                self.tree[curr] ^= (self.lazy[curr] * ((high-low+1) % 2))`
                if low != high:
                    self.lazy[2*curr+1] ^= self.lazy[curr]
                    self.lazy[2*curr+2] ^= self.lazy[curr]

                self.lazy[curr] = 0

            if low == high:
                updated_nums.append(self.tree[curr])
                return
            
            mid = (low+high) // 2
            helper(2*curr+1, low, mid)
            helper(2*curr+2, mid+1, high)

        return updated_nums


class Solution:
    def find_xor(self, nums, l, r):
        t = segTree(nums)
        print(t.tree)
        return t.get_query(l, r)


def main():
    size, num_query = map(input(), int)
    nums = list(map(int, input()))
    s = segTree(nums)
    for q in range(num_query):
        l, r, v = map(int, input())
        s.lazy_update(l, r, v)

    

nums1 = [1,2,3,4]
nums2 = [1,2,3,4, 5,6,7,8,9]
s = Solution()
# print(s.find_xor(nums1, 0, 3))
# print(s.find_xor(nums2, 2, 8))
test = [1,2,5,7]
print(list(map(str, test)))
