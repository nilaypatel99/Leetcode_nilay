class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n=len(nums1)
        m=len(nums2)

        xor1=0
        for num1 in nums1:
            xor1^=num1
        
        xor2=0
        for num2 in nums2:
            xor2^=num2
        
        res=0
        if n%2==1:
            res^=xor2
        if m%2==1:
            res^=xor1
        return res