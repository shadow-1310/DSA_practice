# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        slow.next = None

        left = self.sortList(left)
        right = self.sortList(right)
        dummy = ListNode()
        tail = dummy
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next

            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left

        elif right:
            tail.next = right

        return dummy.next
