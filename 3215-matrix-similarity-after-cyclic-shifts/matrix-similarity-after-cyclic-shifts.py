from collections import deque

class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        n = len(mat[0])

        shift_amount = k % n
        
        if shift_amount == 0:
            return True
            
        shifted = []
        for i, r in enumerate(mat):
            d = deque(r)
            if i % 2 == 0:
                # Even row: Left shift
                d.rotate(-shift_amount)
            else:
                # Odd row: Right shift
                d.rotate(shift_amount)
            shifted.append(list(d))
            
        return shifted == mat

