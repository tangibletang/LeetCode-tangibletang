# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = {}
        curr = head

        while curr: 
            visited_nodes[curr] = 0
            curr = curr.next
            if curr in visited_nodes: 
                return curr
        
        return None