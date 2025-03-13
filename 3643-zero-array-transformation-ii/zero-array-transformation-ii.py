from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        if all(x == 0 for x in nums):  # Check if nums is already zero
            return 0

        def canMakeZero(k: int) -> bool:
            arr = nums[:]
            diff = [0] * (n + 1)
            
            for i in range(k):
                l, r, v = queries[i]
                diff[l] -= v
                if r + 1 < n:
                    diff[r + 1] += v
            
            curr = 0
            for i in range(n):
                curr += diff[i]
                arr[i] += curr
                if arr[i] > 0:
                    return False
            
            return True

        left, right = 1, m
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if canMakeZero(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
