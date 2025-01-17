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
        
        if n%2==0 and m%2==0:
            return 0
        elif n%2==1 and m%2==0:
            return xor2
        elif n%2==0 and m%2==1:
            return xor1
        else:
            return xor1^xor2