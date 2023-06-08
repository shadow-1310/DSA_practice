# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#this is first approach using an extra array. done on 08-06-2023
class Solution:
    def isPalindrome(self, head) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True