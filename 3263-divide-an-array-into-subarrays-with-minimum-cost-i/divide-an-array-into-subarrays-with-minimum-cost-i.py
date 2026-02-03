class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        score=nums[0]
        sec_best=float('inf')
        third_best=float('inf')
        

        for i in range(1,len(nums)):
            if nums[i]<sec_best:
                third_best=sec_best
                sec_best=nums[i]
            elif nums[i]<third_best:
                third_best=nums[i]
        return score+sec_best+third_best