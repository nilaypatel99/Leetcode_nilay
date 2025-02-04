class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l,r=0,1
        res=float('-inf')
        while r<len(nums):
            if nums[r]>nums[r-1]:
                r+=1
            else:
                res=max(res,sum(nums[l:r]))
                l=r
                r+=1
        res=max(res,sum(nums[l:r]))
        return res