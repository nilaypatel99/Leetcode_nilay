class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        res=0
        col_server=[0]*n
        row_alone=[-1]*m

        for i in range(m):
            row_cnt=0
            for j in range(n):
                if grid[i][j]==1:
                    row_cnt+=1
                    col_server[j]+=1
                    row_alone[i]=j

            if row_cnt>1:
                res+=row_cnt
                row_alone[i]=-1  #not alone
        
        for row in range(m):
            if row_alone[row]!=-1:  #alone
                col=row_alone[row]
                if col_server[col]>1:
                    res+=1

        return res