#first done on 20-11-2023
class Solution:
    def balanceBST(self, root):
        nums = []
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)


        def balance(l, r):
            if r < l:
                return None
            if l == r:
                node = TreeNode(nums[l])
                node.left = None
                node.right = None
                return node

            mid = (l+r) >> 1
            node = TreeNode(nums[mid])
            node.left = balance(l, mid-1)
            node.right = balance(mid+1, r)
            return node

        inorder(root)
        return balance(0, len(nums)-1)
