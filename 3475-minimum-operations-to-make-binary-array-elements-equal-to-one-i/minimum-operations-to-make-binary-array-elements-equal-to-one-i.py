class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #if we do xor directly will it solve the problem
        
        n=len(nums)
        op=0

        for i in range(n-2):
            if nums[i]==0:
                nums[i]^=1
                nums[i+1]^=1
                nums[i+2]^=1
                op+=1

        return op if all(x==1 for x in nums) else -1
