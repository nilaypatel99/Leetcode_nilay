class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref_sum = [0]*n
        pref_sum[0] = nums[0]

        for i in range(1,n):
            pref_sum[i]=pref_sum[i-1]+nums[i]

        res = float('-inf')

        for srt in range(k):
            cur_sum = 0
            i = srt
            while (i<n and i+k-1<n):
                j = i+k-1
                subsum = pref_sum[j]-(pref_sum[i-1] if i>0 else 0)
                cur_sum = max(subsum,cur_sum+subsum)
                res = max(res,cur_sum)
                i+=k

        return res