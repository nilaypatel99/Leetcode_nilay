class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while nums[0] < k:  # Continue until the smallest element is >= k
            if len(nums) < 2:  # If we can't pick two elements, return -1
                return -1
            
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)  # Second smallest element
            
            new_element = 2 * min(x, y) + max(x, y)
            heapq.heappush(nums, new_element)  # Add the new element back
            
            operations += 1
        
        return operations
