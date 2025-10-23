class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        max_val = max(nums)+k
        diff_arr = [0]*(max_val+2)
        freq =  defaultdict(int)

        for i in range(n):
            #range creation
            freq[nums[i]]+=1
            l = max(nums[i]-k,0)
            r = min(nums[i]+k,max_val)

            diff_arr[l] += 1
            diff_arr[r+1] -= 1
        
        res = 1
        for target in range(max_val+1):
            if target > 0:
                diff_arr[target] += diff_arr[target-1]
            target_freq = freq[target]
            need_conv = diff_arr[target] - target_freq
            max_pos = min(need_conv,numOperations)

            res = max(res,target_freq+max_pos)

        return res
