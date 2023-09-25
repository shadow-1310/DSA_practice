class NumArray:
    def __init__(self, nums):
        self.tree = [0] * (4*len(nums)+1)
        self.total = len(nums)
        def build(index, low, high):
            if low == high:
                self.tree[index] = nums[low]
                return

            mid = (low + high) // 2
            build(2*index+1, low, mid)
            build(2*index+2, mid+1, high)
            self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]
        build(0, 0, self.total -1)

    def update(self, index, val):
        def helper_update(curr, low, high):
            if low == high:
                self.tree[curr] = val
            else:
                mid = (low + high) // 2
                if index >= low and index <= mid:
                    helper_update(2*curr+1, low, mid)
                else:
                    helper_update(2*curr+2, mid+1, high)

                self.tree[curr] = self.tree[2*curr+1] + self.tree[2*curr+2]

        helper_update(0, 0, self.total-1)

    def sumRange(self, left, right):
        def query(index, left, right, low, high):
            if left <= low and right >= high:
                return self.tree[index]
            if high < left or low > right:
                return 0
            mid = (low + high) // 2
            l_query = query(2*index+1, left, right, low, mid)
            r_query = query(2*index+2, left, right, mid+1, high)
            return l_query + r_query

        return query(0, left, right, 0, self.total-1)


#following are for testing purpose
nums = [1,3,7,3,5,6, 10, 78, 0, -1, 76, 54, 11, 4, 3, 2, 0, 7, 4, -8, 3,1,11,15,17]
c = NumArray(nums)
# print(c.tree)
org = c.tree
print(c.sumRange(2,3))
c.update(2, 5)
print(c.sumRange(2,3))
# print(c.sumRange(2,9))
# print(c.sumRange(6,13))
