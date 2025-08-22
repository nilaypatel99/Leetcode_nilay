class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        #finding the rectangle with min area with all 1's
        x1 = y1 = inf
        x2 = y2 = -inf
        for i in range(len(grid)):    #rows
            for j in range(len(grid[0])):    #colums
                if grid[i][j]==1:    #finding the min x,y coord and max x,y coord
                    x1 =min(x1,i)
                    y1 =min(y1,j)
                    x2 =max(x2,i)
                    y2 =max(y2,j)
        return (x2-x1+1)*(y2-y1+1)
