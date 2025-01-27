class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_remaining_sum=sum(grid[0])
        second_row=0
        res=float('inf')

        for curr_drop in range(len(grid[0])):
            first_row_remaining_sum-=grid[0][curr_drop]
            bestofr2=max(first_row_remaining_sum,second_row)
            #this the decision the first robot makes so that the second robot 
            #gets minimum points
            res=min(bestofr2,res)
            second_row+=grid[1][curr_drop]
        return res