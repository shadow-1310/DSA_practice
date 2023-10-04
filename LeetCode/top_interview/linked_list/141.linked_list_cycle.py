# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# it is a correct solution. my first approach. uses array to store each node.but time complexity is bad 
# done on 08-06-2023
class Solution:
    def hasCycle(self, head):
        node_map = []
        while head:
            node_map.append(head)
            if head.next in node_map:
                return True
            head = head.next

        return False
    

# optimized approac. uses hashmap instead of array to store the node. correct solution
# done on 08-06-2023
class Solution:
    def hasCycle(self, head):
        node_map = {}
        index = 0
        while head:
            node_map[head] = index
            index += 1
            if head.next in node_map:
                return True
            head = head.next

        return False
    

# Floyd's Hare and tortoise approach. uses two pointers one slow(step=1) and one fast(step=2)
# Time complexity = O(N), memory complexity = O(1)
# done on 08-06-2023
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = (fast.next).next

            if slow == fast:
                return True
            
        return False


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = slow

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


#revised on 03-10-2023
class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = slow.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
