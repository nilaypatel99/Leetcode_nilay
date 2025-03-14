from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0  # Not enough candies for each child to get at least 1
        
        left, right = 1, max(candies)
        best = 0  # To store the best possible answer

        while left <= right:
            mid = (left + right) // 2
            children_served = sum(c // mid for c in candies)

            if children_served >= k:  # We can satisfy at least k children
                best = mid  # Update best answer
                left = mid + 1  # Try for a larger size
            else:
                right = mid - 1  # Reduce the candy size
        
        return best
