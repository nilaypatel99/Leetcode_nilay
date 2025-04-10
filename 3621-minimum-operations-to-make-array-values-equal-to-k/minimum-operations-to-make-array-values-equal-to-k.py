class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # If any element is less than k, we can't increase it — return -1
        if any(num < k for num in nums):
            return -1

        # Collect all unique elements > k
        greater_than_k = sorted(set(num for num in nums if num > k), reverse=True)

        # We need to reduce each unique value above k to the next, down to k
        return len(greater_than_k)
