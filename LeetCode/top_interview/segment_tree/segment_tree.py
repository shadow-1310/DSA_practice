class NumArray:
    def __init__(self, nums):
        self.tree = [0] * (4*len(nums)+1)
        self.lazy = [0] * (4*len(nums)+1)
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

    def point_update(self, index, val):
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


    def range_update(self, l, r, v):
        def helper_update(curr, low, high):
            if self.lazy[curr] != 0:
                self.tree[curr] += (high-low+1) * self.lazy[curr]
                if low != high:
                    self.lazy[2*curr+1] += self.lazy[curr]
                    self.lazy[2*curr+2] += self.lazy[curr]
                self.lazy[curr] = 0

            if r < low or high < l:
                return

            if l <= low and high <= r:
                self.tree[curr] += (high-low+1) * v
                if low != high:
                    self.lazy[2*curr+1] += v
                    self.lazy[2*curr+2] += v
                return

            mid = (low+high) // 2
            helper_update(2*curr+1, low, mid)
            helper_update(2*curr+2, mid+1, high)
            self.tree[curr] = self.tree[2*curr+1] + self.tree[2*curr+2]

        helper_update(0, 0, self.total-1)

    def normal_query(self, left, right):
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

    def lazy_sum_query(self, left, right):
        def query(curr, low, high):
            if self.lazy[curr] != 0:
                self.tree[curr] = (high-low+1) * self.lazy[curr]
                if low != high:
                    self.lazy[2*curr+1] += self.lazy[curr]
                    self.lazy[2*curr+2] += self.lazy[curr]
                self.lazy[curr] = 0

            if right < low or left > high:
                return 0

            if left <= low and high <= right:
                return self.tree[curr]

            mid = (low+high) // 2
            return query(2*curr+1, low, mid) + query(2*curr+2, mid+1, high)
        
        return query(0, 0, self.total-1)


#following are for testing purpose
nums = [1,3,7,3,5,6, 10, 78, 0, -1, 76, 54, 11, 4, 3, 2, 0, 7, 4, -8, 3,1,11,15,17]
c = NumArray(nums)
# print(c.tree)
org = c.tree
print(c.normal_query(2,5))
# c.point_update(2, 5)
c.range_update(2, 5, 1)
c.range_update(2, 5, 1)
c.range_update(2, 5, 1)
c.range_update(2, 5, 1)
print(c.normal_query(2,5))
print(c.lazy_sum_query(2,5))
# print(c.sumRange(2,9))
# print(c.sumRange(6,13))
