class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cnt=0 #to count the variable 
        left_sum=0 #prefix sum
        total_sum=sum(nums)  #complement nature to get the right sum

        for i in range(len(nums)-1):
            left_sum+=nums[i]
            r_sum=total_sum-left_sum
            if left_sum>=r_sum:
                cnt+=1
        return cnt