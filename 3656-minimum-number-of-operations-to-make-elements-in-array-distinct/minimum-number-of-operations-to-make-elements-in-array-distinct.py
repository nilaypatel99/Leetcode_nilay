class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(0,n+1,3):
            remaining=nums[i:]
            if len(remaining)==len(set(remaining)):
                return i//3
        return (n+2)//3