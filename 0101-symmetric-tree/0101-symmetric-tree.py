# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True #empty tree is symmetric 
        
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, t1, t2):
        if not t1 and not t2: 
            return True # Both are empty - match!
        if not t1 or not t2: 
            return False # One is empty, one isn't - fail!
        if t1.val != t2.val: 
            return False # Values don't match - fail!
        outer_match = self.isMirror(t1.left, t2.right)
        inner_match = self.isMirror(t1.right, t2.left)

        return outer_match and inner_match