class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """
        Returns the earliest index i in arr such that either some row or column in mat
        is fully filled with '#'.
        """
        # Number of rows & cols
        rows = len(mat)
        cols = len(mat[0])
        
        # 1) Build a dictionary mapping each value in mat -> (row, col)
        pos_map = {}
        for r in range(rows):
            for c in range(cols):
                pos_map[mat[r][c]] = (r, c)
        
        # 2) Initialize row & column counts
        row_count = [0] * rows
        col_count = [0] * cols
        
        # 3) Iterate through arr in order
        for i, val in enumerate(arr):
            # Find the position (r, c) of this value in mat
            r, c = pos_map[val]
            
            # If not already marked '#', mark it
            if mat[r][c] != '#':
                mat[r][c] = '#'
                
                # Update counters
                row_count[r] += 1
                col_count[c] += 1
                
                # Check if row r got fully filled
                if row_count[r] == cols:
                    return i  # i is the earliest index that completes row r
                
                # Check if column c got fully filled
                if col_count[c] == rows:
                    return i  # i is the earliest index that completes column c
        
        # If no row or column ever completed, you can return -1 or some sentinel
        return -1
