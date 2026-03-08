class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        minutes = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c)) # Add every rotten orange to the starting line
                elif grid[r][c] == 1:
                    fresh_oranges += 1 # We keep track of this to know when we're done
    
        
        while queue and fresh_oranges > 0:
            minutes += 1
            for _ in range(len(queue)):  #processes oranges at the start of the queue 
                r, c = queue.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    sumRows, sumCols = r + dr, c + dc
                    if 0 <= sumRows < rows and 0 <= sumCols < cols and grid[sumRows][sumCols] == 1:
                            grid[sumRows][sumCols] = 2
                            fresh_oranges -=1
                            queue.append((sumRows, sumCols))
        return minutes if fresh_oranges == 0 else -1