class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dist[r][c] will hold the minimum cost (number of modifications) 
        # needed to reach (r, c).
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        from collections import deque
        dq = deque()
        dq.append((0, 0))
        
        # Directions: 1=right, 2=left, 3=down, 4=up
        # Let's define them in a convenient mapping
        # For each direction d, we define (dr, dc)
        # Then for each direction, we can easily loop to find neighbors.
        directions = {
            1: (0, 1),   # right
            2: (0, -1),  # left
            3: (1, 0),   # down
            4: (-1, 0)   # up
        }
        
        def inside(r, c):
            return 0 <= r < m and 0 <= c < n

        while dq:
            r, c = dq.popleft()
            current_cost = dist[r][c]
            current_dir = grid[r][c]
            
            # 1) Follow the existing direction (0-cost edge)
            dr, dc = directions[current_dir]
            nr, nc = r + dr, c + dc
            if inside(nr, nc):
                if current_cost < dist[nr][nc]:
                    dist[nr][nc] = current_cost
                    dq.appendleft((nr, nc))  # 0-cost -> appendleft
            
            # 2) Try changing the direction to each of the other 3 directions (1-cost edges)
            for d_alt in (1, 2, 3, 4):
                if d_alt == current_dir:
                    continue
                dr_alt, dc_alt = directions[d_alt]
                nr_alt, nc_alt = r + dr_alt, c + dc_alt
                if inside(nr_alt, nc_alt):
                    # cost to change sign is current_cost + 1
                    new_cost = current_cost + 1
                    if new_cost < dist[nr_alt][nc_alt]:
                        dist[nr_alt][nc_alt] = new_cost
                        dq.append((nr_alt, nc_alt))  # 1-cost -> append right (back)
        
        return dist[m-1][n-1]
