class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        #j>i if nums[j]<nums[i]
        #j<i if nums[j]>nums[i]

        n=len(nums)

        max_pref=[0]*n
        min_suf=[0]*n

        max_pref[0]=nums[0]
        min_suf[n-1]=nums[n-1]

        for i in range(n):
            max_pref[i]=max(nums[i],max_pref[i-1])

        for i in range(n-2,-1,-1):
            min_suf[i]=min(nums[i],min_suf[i+1])

        ans=[0]*n
        ans[n-1]=max_pref[n-1]

        for i in range(n-2,-1,-1):
            if max_pref[i]>min_suf[i+1]:
                ans[i]=ans[i+1]

            else:
                ans[i]=max_pref[i]
        
        return ans


