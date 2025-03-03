class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than=[]
        equal_than=[]
        greater_than=[]

        for i in range(len(nums)):
            if nums[i]<pivot:
                less_than.append(nums[i])

            elif nums[i]==pivot:
                equal_than.append(nums[i])
            
            else:
                greater_than.append(nums[i])

        return less_than+equal_than+greater_than