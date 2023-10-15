from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []
        q = deque()
        res = defaultdict(list)
        q.append([root,0,0])

        while q:
            for i in range(len(q)):
                node, row, offset = q.popleft()
                res[offset].append([node.val, row])
                if node.left:
                    q.append([node.left, row+1, offset-1])
                if node.right:
                    q.append([node.right, row+1, offset+1])

        # return [v for _,v in sorted(d.items())] 
        ans = []
        for key in sorted(res.keys()):
            curr = res[key]
            curr.sort(key = lambda x: (x[1], x[0]))
            temp = []
            for i in curr:
                temp.append(i[0])
            ans.append(temp)

        return ans
