# this is my first approach and it is not working
class Solution:
    def swapPairs(self, head):
        dummy = ListNode()
        dummy.next = head
        tail = head

        while tail and tail.next:
            temp = tail.next.next
            tail.next.next = tail
            tail.next = temp
            tail = tail.next

        return dummy.next


#this is 2nd attempt and working perfectly
#done on 24-10-2023
class Solution:
    def swapPairs(self, head):
        dummy = ListNode()
        dummy.next = head
        tail = dummy

        while head and head.next:
            next_head = head.next.next
            tail.next = head.next
            tail.next.next = head

            head.next = next_head
            tail = head
            head = next_head

        return dummy.next
