# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head 
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


#this is a revision done on 02-09-2023
class Solution:
    def reorderList(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tail = None

        while slow:
            temp = slow.next
            slow.next = tail
            tail = slow
            slow = temp

        left = head
        right = tail

        while left and right:
            temp_left = left.next
            temp_right = right.next

            left.next = right
            right.next = temp_left

            left = temp_left
            right = temp_right

        return head
