class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        i,j=0,0
        masked=0
        res=1

        while j<n:
            while nums[j]&masked!=0:
                #shrink the window
                masked=masked^nums[i]
                i+=1
            res=max(res,j-i+1)
            masked=masked|nums[j]
            j+=1
        return res