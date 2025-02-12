class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        digit_sum_map = defaultdict(list)

        # Helper function to compute sum of digits
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        # Populate the dictionary
        for num in nums:
            dsum = digit_sum(num)
            digit_sum_map[dsum].append(num)

        max_sum = -1

        # Iterate over groups and find the max sum of two largest numbers
        for num_list in digit_sum_map.values():
            if len(num_list) > 1:
                num_list.sort(reverse=True)  # Sort descending to get the two largest
                max_sum = max(max_sum, num_list[0] + num_list[1])

        return max_sum
