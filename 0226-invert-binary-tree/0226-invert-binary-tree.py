# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. BASE CASE: The "Stop Sign"
        if not root:
            return None
        
        # 2. THE DIVE: Invert the children first
        # (We save them in variables so we don't lose them during the swap)
        left_side = self.invertTree(root.left)
        right_side = self.invertTree(root.right)
        
        # 3. THE SWAP: Put the left on the right, and right on the left
        root.left = right_side
        root.right = left_side
        
        # 4. RETURN: Send the finished, flipped node back up to the parent
        return root