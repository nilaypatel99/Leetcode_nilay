class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        m, n = len(isWater), len(isWater[0])
        
        # Initialize the height array with -1 for land, and 0 for water
        height = [[-1]*n for _ in range(m)]
        q = deque()
        
        # Step 1: Put all water cells in the queue with height = 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append((i, j))
        
        # Directions: up, down, left, right
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        # Step 2: BFS
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr, nc))
        
        return height

