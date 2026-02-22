# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        length = 0
        if not root: 
            return length #no root length is 0 
        #start the queue at the root
        queue = deque([root])
        while queue: 
            level_size = len(queue)
            for i in range(level_size): 
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            length += 1
        return length 
