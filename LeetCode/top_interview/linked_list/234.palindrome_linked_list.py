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
    

class Solution:
    def isPalindrome(self, head) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow  =slow.next
            fast = fast.next.next

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev:
            if prev.val != head.val:
                return False
            
            head = head.next
            prev = prev.next

        return True


#this is new approach to the problem while doing revision, but it is not working for the test case [1,0,1]
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        tail = None
        fast = head
        count = 1

        while fast and fast.next:
            fast = fast.next.next
            count += 1

            temp = head.next
            head.next = tail
            tail = head
            head = temp

        print(count)
        if count == 1 and tail.val == fast.next.next.val:
            return True
 
        if count % 2 == 1:    
            left = tail
            right = tail
            print("even", left.val, right.val)
        else:
            left = tail
            right = head
            print("odd", left, right)

        # print(left.val,right.val)

        while left and right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next


        return True


#this is a revision done on 02-09-2023, working for all test cases of Leetcode
class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head
        
        #code to find the mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        front = slow
        tail = None

        #code to reverse the right half
        while front:
            temp = front.next
            front.next = tail
            tail = front
            front = temp

        #code to check if corresponding elements are equal, head pointer is going from the front and tail is coming from the back
        while tail and head:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next

        return True


#this revision is done on 03-10-2023
class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        prev = None

        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp

        right = prev
        while head and right:
            if head.val != right.val:
                return False

            head = head.next
            right = right.next

        return True
