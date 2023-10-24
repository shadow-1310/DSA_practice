from collections import defaultdict
#working on LC testcases but not efficient
class Solution:
    def pathSum(self, root, targetSum):
        self.res = 0
        def helper(node, curr):
            if not node:
                return
            if curr + node.val == targetSum:
                self.res += 1

            helper(node.left, curr+node.val)
            helper(node.right, curr+node.val)
        def dfs(node):
            if not node:
                return
            helper(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.res


#this is a correct and efficient solution
class Solution:
    def pathSum(self, root, targetSum):
        prev_sum = defaultdict(int)
        prev_sum[0] = 1
        def dfs(node, curr):
            if not node:
                return 0
            tot = curr + node.val
            count = prev_sum[tot - targetSum]
            prev_sum[tot] += 1
            count += dfs(node.left, tot) + dfs(node.right, tot)
            prev_sum[tot] -= 1

            return count

        return dfs(root, 0)



