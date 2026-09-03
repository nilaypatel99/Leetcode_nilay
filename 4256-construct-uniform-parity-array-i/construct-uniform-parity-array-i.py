class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        if len(nums1)==1:
            return True

        odd = sum(x % 2 for x in nums1)
        even = len(nums1) - odd

        # Make everything even
        if odd == 0 or odd >= 2:
            return True

        # Make everything odd
        if odd > 0 and even > 0:
            return True

        return False
