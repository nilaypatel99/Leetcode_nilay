class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        org_cnt=len(set(nums))
        n=len(nums)

        maps=defaultdict(int)
        i,j=0,0
        res=0

        while j<n:
            maps[nums[j]]+=1

            while len(maps)==org_cnt:
                res+=(n-j)

                maps[nums[i]]-=1

                if maps[nums[i]]==0:
                    del maps[nums[i]]
                i+=1

            j+=1
        
        return res
            