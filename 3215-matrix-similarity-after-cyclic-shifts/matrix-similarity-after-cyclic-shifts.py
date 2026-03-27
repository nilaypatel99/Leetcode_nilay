class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n
        for r in mat:
            # If a row shifted by k is equal to itself, it doesn't matter 
            # if it's left or right; it just needs to be periodic.
            if r != r[k:] + r[:k]:
                return False
        return True
