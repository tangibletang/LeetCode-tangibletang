# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque 

        if not root:
            return []
        queue = deque([root])#first element of the tree
        result = []
            
        while queue:
            level_size = len(queue)
            current_level = []
            #because root is the firs tleement of the tree, current level is 1 first run
            for i in range (level_size):
                node = queue.popleft()
                current_level.append(node.val)
            #pop from the queue and add to current level. 
                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            #add to queue the neighbors 
            result.append(current_level)
            #add the current_level array to results for the grand array
        
        return result 
                
