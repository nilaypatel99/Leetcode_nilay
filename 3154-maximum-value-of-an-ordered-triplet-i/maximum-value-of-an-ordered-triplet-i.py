class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if i<j<k:
                        res=max(res,(nums[i]-nums[j])*nums[k])
                        if res<0:
                            return 0
        return res