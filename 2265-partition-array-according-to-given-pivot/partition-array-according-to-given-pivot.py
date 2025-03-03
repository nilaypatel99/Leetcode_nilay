class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_cnt=0
        eq_cnt=0
        grt_cnt=0
        res=[0]*len(nums)

        for i in range(len(nums)):
            if nums[i]<pivot:
                less_cnt+=1
            elif nums[i]==pivot:
                eq_cnt+=1
            else:
                grt_cnt+=1
        i=0
        j=less_cnt
        k=less_cnt+eq_cnt

        for val in nums:
            if val<pivot:
                res[i]=val
                i+=1
            elif val==pivot:
                res[j]=val
                j+=1
            else:
                res[k]=val
                k+=1
        return res