class Solution:
    from collections import deque
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        distance = 1

        #check the boundary condition: 
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1: #if start or end are blocked
            return -1 
        
        if rows == 1 and cols == 1 and grid[0][0] == 0:
            return 1

        while queue: 
            distance +=1
            for _ in range(len(queue)):
                r,c = queue.popleft() #get the starting coords to do check peripheral
                for dr, dc in [(0,1),(0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:#all 8 directions
                    nr, nc = r + dr, c + dc
                    if nr == rows -1 and nc == cols - 1 and grid[nr][nc] == 0:
                        return distance
                    elif 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr,nc) not in visited: 
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
        return -1
