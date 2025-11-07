class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []

        def get_sum(subarray):
            freq = Counter(subarray)
            sorted_elements = sorted(freq.items(),key=lambda item:(-item[1],-item[0]))
            top_elements = sorted_elements[:x]
            return sum([ele*cnt for ele,cnt in top_elements])

        for i in range(n-k+1):
            res.append(get_sum(nums[i : k+i]))
        return res