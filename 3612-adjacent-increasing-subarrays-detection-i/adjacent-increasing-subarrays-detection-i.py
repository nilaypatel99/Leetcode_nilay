class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        curr_run = 1
        prev_run = 0
        max_res = 0

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                curr_run += 1
            else:
                prev_run = curr_run
                curr_run = 1
            if curr_run >= 2*k:
                # curr_run length of an array which can accomadate both arrays
                return True

            if min(prev_run,curr_run)>=k:
                return True
        return False
            

