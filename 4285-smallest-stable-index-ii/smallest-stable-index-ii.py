class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        # Build suffix minimum: right -> left
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Find first stable index: left -> right
        current_max = float('-inf')

        for i in range(n):
            current_max = max(current_max, nums[i])

            score = current_max - suffix_min[i]

            if score <= k:
                return i

        return -1
