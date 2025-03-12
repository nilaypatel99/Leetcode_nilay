class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        neg_count = bisect_left(nums, 0)  # Index of first non-negative number (count of negatives)
        pos_count = len(nums) - bisect_right(nums, 0)  # Count of positives
        return max(neg_count, pos_count)


