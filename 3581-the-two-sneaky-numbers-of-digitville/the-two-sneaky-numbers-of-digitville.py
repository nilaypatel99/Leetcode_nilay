class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = defaultdict()
        res = []

        for val in nums:
            if val not in cnt:
                cnt[val]=1
            else:
                res.append(val)
        return res