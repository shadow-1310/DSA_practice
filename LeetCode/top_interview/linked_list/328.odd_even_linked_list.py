# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        head_odd = head
        head_even = head.next
        tail_odd =  head_odd
        tail_even = head_even

        while tail_odd and tail_odd.next and tail_even and tail_even.next:
            tail_odd.next = tail_odd.next.next
            tail_even.next = tail_even.next.next

            tail_odd = tail_odd.next
            tail_even = tail_even.next

        tail_even.next = None
        tail_odd.next = head_even

        return head
