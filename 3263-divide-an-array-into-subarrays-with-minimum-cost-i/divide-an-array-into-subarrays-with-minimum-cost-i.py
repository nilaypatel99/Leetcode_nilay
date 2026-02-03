class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first=nums[0]
        secbest=nums[1]
        ans=float('inf')

        for j in range(2,len(nums)):
            ans=min(ans,first+secbest+nums[j])
            secbest=min(secbest,nums[j])

        return ans