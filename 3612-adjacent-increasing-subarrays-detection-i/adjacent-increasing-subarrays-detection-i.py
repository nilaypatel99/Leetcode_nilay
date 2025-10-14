from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # Iterate over all possible starting indices for the first subarray
        for i in range(n - 2 * k + 1):  # Last valid `i` is `n - 2k` to allow space for both subarrays
            # Check if the first subarray nums[i..i+k-1] is strictly increasing
            first_increasing = True
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:  # Not strictly increasing
                    first_increasing = False
                    break

            # Check if the second subarray nums[i+k..i+2k-1] is strictly increasing
            second_increasing = True
            for j in range(i + k, i + 2 * k - 1):
                if nums[j] >= nums[j + 1]:  # Not strictly increasing
                    second_increasing = False
                    break

            # If both subarrays are strictly increasing, return True
            if first_increasing and second_increasing:
                return True
        
        # If no valid adjacent increasing subarrays were found, return False
        return False
