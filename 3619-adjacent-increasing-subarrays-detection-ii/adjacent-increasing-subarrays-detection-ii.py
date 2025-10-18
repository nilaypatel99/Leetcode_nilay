class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        curr_run = 1
        prev_run = 0
        mx_res = 0
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                curr_run += 1
            else:
                prev_run = curr_run
                curr_run = 1

            mx_res = max(mx_res,curr_run//2)
            mx_res = max(mx_res,min(curr_run,prev_run))

        return mx_res
            

