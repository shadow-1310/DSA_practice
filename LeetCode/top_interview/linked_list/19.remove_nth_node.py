# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my first approach. giving wrong solution, done one 09-06-2023
class Solution:
    def removeNthFromEnd(self, head, n: int):
        count = 0
        tail = head

        while tail:
            count += 1
            tail = tail.next

        node = count - n
        temp = 0
        left_node = head

        while temp < node:
            temp += 1
            left_node = left_node.next

        left_node.next = left_node.next.next

        return head
    

# this is the correct solution using two pointers
# done on 09-06-2023
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(val=0, next = head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

#this is a revision done on 02-09-2023, working for all test cases of Leetcode
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        tail = dummy

        while n > 0:
            head = head.next
            n -= 1

        while head:
            tail = tail.next
            head = head.next

        tail.next = tail.next.next

        return dummy.next


