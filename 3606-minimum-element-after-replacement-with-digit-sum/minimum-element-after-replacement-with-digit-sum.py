from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []

        for num in nums:
            curr_sum = 0

            while num > 0:
                digit = num % 10
                curr_sum += digit
                num //= 10

            res.append(curr_sum)

        return min(res)