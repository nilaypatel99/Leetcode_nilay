class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_cnt=0
        pos_cnt=0

        for i in range(len(nums)):
            if nums[i]<0:
                neg_cnt+=1
            elif nums[i]>0:
                pos_cnt+=1
            else:
                continue
        return max(neg_cnt,pos_cnt)