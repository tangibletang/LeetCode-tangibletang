from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 0. Identify the "target_value" (the original color we are replacing)
        original_color = image[sr][sc]
        
        # EDGE CASE: If the starting pixel is already the new color, 
        # we don't need to do anything (prevents infinite loops!)
        if original_color == newColor:
            return image
            
        rows, cols = len(image), len(image[0])
        
        # 1. Setup the Queue (We don't actually need a visited set if we change the color immediately!)
        # But for learning, let's keep the coordinate pairs in the queue.
        queue = deque([(sr, sc)])
        
        # 2. Change the starting pixel immediately
        image[sr][sc] = newColor

        while queue:
            r, c = queue.popleft()
            
            # 3. Explore Neighbors (Up, Down, Left, Right)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                # 4. The "Safety Check"
                # - In bounds?
                # - Is it the color we're looking for?
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    
                    # 5. Process & Mark as "Visited"
                    # By changing the color NOW, we ensure we don't add it to the queue twice.
                    image[nr][nc] = newColor
                    queue.append((nr, nc))
                    
        return image