# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#this is first approach and correct solution. done on 10-06-2023
class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode(val = 0, next=head)
        tail = dummy

        while tail and tail.next:
            while tail.next and tail.next.val == val:
                tail.next = tail.next.next
            
            tail = tail.next

        return dummy.next


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(val = 0, next = head)
        tail = dummy

        while tail and tail.next:
            while tail.next and tail.next.val == val:
                tail.next = tail.next.next

            tail = tail.next

        return dummy.next


class Solution:
    def removeElements(self, head, val):
        dummy = Node()
        dummy.next = head
        curr = dummy

        while curr and curr.next:
            while curr.next.val == val:
                curr.next = curr.next.next

            curr = curr.next

        return dummy.next
