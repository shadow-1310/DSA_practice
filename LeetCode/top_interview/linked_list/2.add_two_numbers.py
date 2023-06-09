# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# this is a wrong solution. done on 09-06-2023
class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        tail = result
        carry = 0

        while l1 and l2:
            curr_sum = l1.val + l2. val + carry
            value = curr_sum % 10
            carry = curr_sum // 10
            tail.next = ListNode(value)

            l1 = l1.next
            l2 = l2.next
            tail = tail.next

        while l1 or carry:
            curr_sum = l1.val + carry
            value = curr_sum % 10
            carry = curr_sum // 10
            tail.next = ListNode(value)

            l1 = l1.next
            tail = tail.next

        while l2 or carry:
            curr_sum = l2.val + carry
            value = curr_sum % 10
            carry = curr_sum // 10
            tail.next = ListNode(value)

            l2 = l2.next
            tail = tail.next

        return result.next
    

# this is correct solution. done on 09-06-2023
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            val = sum % 10
            carry = sum // 10

            curr.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next