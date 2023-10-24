class Solution:
    def flatten(self, root):
        def dfs(node):
            if not node:
                return None
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if node.left:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            last = right_tail or left_tail or node
            return last
        dfs(root)
