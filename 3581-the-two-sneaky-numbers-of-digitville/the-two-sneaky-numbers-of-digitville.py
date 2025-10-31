class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = set()
        res = []

        for val in nums:
            if val not in cnt:
                cnt.add(val)
            else:
                res.append(val)
        return res