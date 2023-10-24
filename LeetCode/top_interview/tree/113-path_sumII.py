#first done as part of top100 liked playlist on LC, 24-10-2023
class Solution:
    def pathSum(self, root, targetSum):
        res = []
        def dfs(node, curr_path, curr_sum):
            if not node:
                return
            if not node.left and not node.right and curr_sum + node.val == targetSum:
                curr_path.append(node.val)
                res.append(curr_path[:])
                curr_path.pop()

            curr_path.append(node.val)
            dfs(node.left, curr_path, curr_sum + node.val)
            dfs(node.right, curr_path, curr_sum + node.val)
            curr_path.pop()

        dfs(root, [], 0)
        return res
