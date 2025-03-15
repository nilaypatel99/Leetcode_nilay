class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob_with_capability(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1  # Skip adjacent house
                i += 1  # Move to next house
            return count >= k

        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) // 2
            if can_rob_with_capability(mid):
                high = mid  # Try a lower capability
            else:
                low = mid + 1  # Increase capability
        return low
