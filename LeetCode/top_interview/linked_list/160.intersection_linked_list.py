# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        map_a = {}
        index = 0

        while headA:
            map_a[headA] = index
            headA = headA.next
            index += 1

        while headB:
            if headB in map_a:
                return headB
            
            headB = headB.next

        return None