class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Helper function to find parent in DSU
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Helper function to union two nodes
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                size[py] += size[px]
        
        # Initialize DSU structures
        parent = list(range(n * n))
        size = [1] * (n * n)
        
        # First pass: connect all existing islands
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    for dr, dc in [(0, 1), (1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            union(r * n + c, nr * n + nc)
        
        # Calculate island sizes
        island_sizes = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    root = find(r * n + c)
                    island_sizes[root] = size[root]
        
        # If no zeros exist, return total grid size
        if not any(0 in row for row in grid):
            return max(island_sizes.values(), default=0)
        
        # Second pass: try changing each zero to one
        max_island_size = max(island_sizes.values(), default=0)
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    unique_islands = set()
                    current_size = 1
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            root = find(nr * n + nc)
                            if root not in unique_islands:
                                unique_islands.add(root)
                                current_size += size[root]
                    
                    max_island_size = max(max_island_size, current_size)
        
        return max_island_size

