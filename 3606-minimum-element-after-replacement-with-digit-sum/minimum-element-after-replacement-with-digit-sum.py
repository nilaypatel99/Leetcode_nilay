from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')

        for num in nums:
            curr_sum = 0
            while num > 0:
                digit = num % 10
                curr_sum += digit
                num //= 10
            res=min(res,curr_sum)

        return res