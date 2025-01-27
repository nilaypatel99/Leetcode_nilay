class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        #The absolute diff should be one and the we want to maximize the height
        #the diff should be one from all sides and how to do this
        r,c=len(isWater),len(isWater[0])
        res=[[-1]*c for _ in range(r)]
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        queue=deque()
        for i in range(r):
            for j in range(c):
                if isWater[i][j]==1:
                    res[i][j]=0
                    queue.append((i,j))

        
        while queue:
            i,j=queue.popleft()

            for dir1 in directions:
                i_,j_= i+dir1[0],j+dir1[1]

                if 0<=i_<r and 0<=j_<c and res[i_][j_]==-1:
                    res[i_][j_]=res[i][j]+1
                    queue.append((i_,j_))

        return res


