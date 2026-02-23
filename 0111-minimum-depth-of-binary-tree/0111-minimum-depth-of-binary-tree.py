# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = 0
        if not root: 
            return 0

        queue = deque([root])
        while queue:
            queue_length = len(queue)
            min_depth += 1
            for i in range(queue_length):
                node = queue.popleft()
                if not node.right and not node.left: #no children
                    return min_depth
                if node.right: 
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
