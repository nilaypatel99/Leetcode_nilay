class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        n=len(nums)

        if n<3:
            return 0

        max_k=[0]*n
        max_k[-1]=nums[-1]

        for k in range(n-2,-1,-1):
            max_k[k] = max(max_k[k + 1], nums[k])
        
        max_value = 0
        max_i=nums[0]
        for j in range(1, n - 1):
            max_i = max(max_i, nums[j - 1])  
            triplet_value = (max_i - nums[j]) * max_k[j + 1]
            max_value = max(max_value, triplet_value)

        return max_value



                