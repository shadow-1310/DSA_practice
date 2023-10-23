#first done on 23-10-2023
class Solution:
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return [0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            
            l_depth, l_max = left[0], left[1]
            r_depth, r_max = right[0], right[1]

            depth = 1 + max(l_depth, r_depth)
            curr_max = max(l_max, r_max)

            return [depth, curr_max]

        return dfs(root)[1]
