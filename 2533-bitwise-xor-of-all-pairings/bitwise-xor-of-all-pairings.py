class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # XOR of all elements in nums1
        xor_nums1 = 0
        for num in nums1:
            xor_nums1 ^= num

        # XOR of all elements in nums2
        xor_nums2 = 0
        for num in nums2:
            xor_nums2 ^= num

        n = len(nums1)
        m = len(nums2)

        # Case analysis based on parities of n and m
        if (n % 2 == 0) and (m % 2 == 0):
            return 0
        elif (n % 2 == 1) and (m % 2 == 0):
            return xor_nums2
        elif (n % 2 == 0) and (m % 2 == 1):
            return xor_nums1
        else:
            return xor_nums1 ^ xor_nums2
