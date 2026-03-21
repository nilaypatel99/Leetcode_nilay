class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        #using the swap we can replace in place
        #so the swap would be something like x+k,and y+k or some kind of these logic
        top=x
        bottom=x+k-1

        while top<bottom:
            for col in range(y,y+k):
                grid[top][col],grid[bottom][col]=grid[bottom][col],grid[top][col]
            top+=1
            bottom-=1
        return grid