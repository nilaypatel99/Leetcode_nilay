class Solution:
    def countBadPairs(self, nums):
        freq = defaultdict(int)  # Stores frequency of value[i] = nums[i] - i
        good_pairs = 0
        n = len(nums)

        for j in range(n):
            value_j = nums[j] - j  # Compute value[j]
            good_pairs += freq[value_j]  # Add number of good pairs found
            freq[value_j] += 1  # Update frequency of value[j]
        
        total_pairs = (n * (n - 1)) // 2
        return total_pairs - good_pairs  # Bad pairs = total - good pairs
