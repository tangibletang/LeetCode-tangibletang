# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #first find the middle 
        slow = head
        fast = head
        test_head = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        #now slow should be the middle value
        #need to reverse the list now
        
        prev = None
        while slow: 
            temp_next = slow.next
            slow.next = prev
            prev = slow
            slow = temp_next
        #reverses the link
        while prev: 
            if prev.val != test_head.val:
                return False
            #increment pointers
            prev = prev.next
            test_head = test_head.next
        return True