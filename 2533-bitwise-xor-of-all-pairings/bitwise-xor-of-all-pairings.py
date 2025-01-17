class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        #as xor is assiociative the even terms will be zero and odd 
        #terms will be left

        n=len(nums1)
        m=len(nums2)
        res=defaultdict(int)

        for num in nums1:
            res[num]+=m
        for num2 in nums2:
            res[num2]+=n
    
        ans=0
        for key,val in res.items():
            if val%2!=0:
                ans^=key
        return ans
