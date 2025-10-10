from typing import List

class Solution:
    def __init__(self):
        self.n = 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def reachable(self, grid: List[List[int]], i: int, j: int, mid: int, visited: List[List[bool]]) -> bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.n or visited[i][j] or grid[i][j] > mid:
            return False

        if i == self.n - 1 and j == self.n - 1:
            return True

        visited[i][j] = True

        for dx, dy in self.directions:
            if self.reachable(grid, i + dx, j + dy, mid, visited):
                return True

        return False

    def swimInWater(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        left = grid[0][0]
        right = self.n * self.n - 1
        result = 0

        while left <= right:
            mid = (left + right) // 2
            visited = [[False] * self.n for _ in range(self.n)]

            if self.reachable(grid, 0, 0, mid, visited):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
