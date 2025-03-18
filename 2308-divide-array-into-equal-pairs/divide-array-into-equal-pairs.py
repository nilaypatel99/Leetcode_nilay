class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        
        temp=Counter(nums)
        for key,val in temp.items():
            if val%2==0:
                continue
            else:
                return False
        return True