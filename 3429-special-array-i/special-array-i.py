class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            prev=nums[i]&1
            adj=nums[i+1]&1

            if prev!=adj:
                continue
            else:
                return False
        return True
            
