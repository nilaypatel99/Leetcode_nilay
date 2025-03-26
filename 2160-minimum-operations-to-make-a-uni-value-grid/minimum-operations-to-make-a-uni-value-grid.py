from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid to a 1D list
        nums = [num for row in grid for num in row]
        nums.sort()

        # Check feasibility: all numbers must have the same remainder when divided by x
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        
        # Find the median of the sorted list
        median = nums[len(nums) // 2]

        # Calculate operations needed to convert all elements to the median
        operations = sum(abs(num - median) // x for num in nums)
        
        return operations
