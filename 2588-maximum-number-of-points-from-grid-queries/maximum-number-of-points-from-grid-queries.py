from heapq import heappush, heappop
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])  # Sort queries with indices

        min_heap = [(grid[0][0], 0, 0)]  # Min-heap to process smallest values first
        visited = set()  # Set to track visited cells
        result_map = {}  # Stores results per query index
        count = 0  # Number of unique points collected

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movement directions

        for idx, q in queries_sorted:
            # Expand cells while they are strictly less than q
            while min_heap and min_heap[0][0] < q:
                val, r, c = heappop(min_heap)
                
                if (r, c) in visited:
                    continue  # Skip if already counted
                
                visited.add((r, c))
                count += 1  # Increase count as this is a new valid visit
                
                # Explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        heappush(min_heap, (grid[nr][nc], nr, nc))

            result_map[idx] = count  # Store result for this query
        
        return [result_map[i] for i in range(len(queries))]
