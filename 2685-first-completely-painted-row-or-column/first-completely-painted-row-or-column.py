from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        
        position = {}
        for r in range(n):
            for c in range(m):
                position[mat[r][c]] = (r, c)

        row_count = [0] * n
        col_count = [0] * m
        
        for i, num in enumerate(arr):
            r, c = position[num]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == m or col_count[c] == n:
                return i
        
        return -1
