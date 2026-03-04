from collections import deque
class Solution:
    def find_start(self, grid, rows, cols):
            for r in range(rows):
                for c in range(cols): 
                    if grid[r][c] == 1: 
                        return (r,c)
            return None
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        perimeter = 0 

        start_node = self.find_start(grid, rows, cols)
        if not start_node: return 0

        queue = deque ([start_node])
        visited = set ([start_node])

        while queue: 
            r,c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == 0:
                    perimeter += 1
                elif (nr, nc) not in visited:
                    visited.add((nr, nc)) # Mark as seen!
                    queue.append((nr, nc))
                
        return perimeter