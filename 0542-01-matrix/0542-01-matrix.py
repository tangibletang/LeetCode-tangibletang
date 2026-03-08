class Solution:
    from collections import deque
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0]) #initialize the length of rows and cols
        queue = deque()
        for r in range (rows): 
            for c in range (cols): 
                if mat[r][c] == 0: 
                    queue.append((r,c))
                else: #grid[r][c]!=0
                    mat[r][c] = -1 #mark it as univisited
        while queue: 
            ro,co = queue.popleft()
            for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)]:
                nr, nc = dr + ro, dc + co
                
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc]== -1:
                    mat[nr][nc] = mat[ro][co] + 1
                    queue.append((nr, nc))
        return mat




