class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0 
        rows, cols = len(grid), len(grid[0])
        islands = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    #BFS
                    queue = deque ([(r,c)])
                    grid[r][c] = "0"
                    while queue: 
                        curr, curc = queue.popleft()
                        for dr, dc, in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nr, nc = curr + dr, curc + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0" # Sink it! (Acts as 'visited')
                                queue.append((nr, nc))
        return islands
                    





