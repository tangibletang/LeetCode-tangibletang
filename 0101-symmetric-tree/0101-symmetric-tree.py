# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # Push the first pair: the two children of the root
        queue = deque([root.left, root.right])

        while queue: 
            # Pop the pair currently at the front
            L = queue.popleft()
            R = queue.popleft()
            
            # 1. If both are None, this "branch" is symmetric. Continue to next pair.
            if not L and not R:
                continue
                
            # 2. If only one is None, OR the values don't match, it's not symmetric.
            if not L or not R or L.val != R.val:
                return False
                
            # 3. Mirror Push:
            # Pair the outsides
            queue.append(L.left)
            queue.append(R.right)
            # Pair the insides
            queue.append(L.right)
            queue.append(R.left)
            
        return True