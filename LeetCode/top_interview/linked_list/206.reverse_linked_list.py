# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# it is first approach and correct. but it's memory complexity is O(N)
# done on 08-06-2023
class Solution:
    def reverseList(self, head):
        dummy = ListNode()
        tail = dummy
        tail.next = None

        while head:
            prev = ListNode()
            tail.val = head.val
            prev.next = tail
            head = head.next
            tail = prev

        return tail


# two pointer solution. time complexity = O(N) and memory complexity = O(1)
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev