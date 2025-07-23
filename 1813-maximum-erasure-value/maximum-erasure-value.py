class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        i,j = 0,0
        curr_sum = 0
        max_sum = 0

        while j<n:
            if nums[j] not in seen:
                curr_sum += nums[j]
                max_sum = max(curr_sum,max_sum)
                seen.add(nums[j])
                j+=1
                
            else:
                # if the duplicate is there we shrink from left and put the right sum in the window
                while i<n and nums[j] in seen:
                    curr_sum -= nums[i]
                    seen.remove(nums[i])
                    i+=1

        return max_sum


        