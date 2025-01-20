class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        if not heightMap or not heightMap[0]:
            return 0
        
        r,c=len(heightMap),len(heightMap[0])
        if r<3 and c<3:
            return 0
        pq=[]
        visited=[[False]*c for _ in range(r)]
        
        for n in range(r):
            for m in range(c):
                if n in (0,r-1) or m in (0,c-1):#if top-most col and right-most col and bottom-most row and r-m col
                    heapq.heappush(pq,(heightMap[n][m],n,m))
                    visited[n][m] = True
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        res=0
        while pq:
            curr_height,re,ce=heapq.heappop(pq)

            for dr,dc in directions:
                nr,nc=re+dr,ce+dc

                if 0<=nr<r and 0<=nc<c and not visited[nr][nc]:
                    res+=max(curr_height-heightMap[nr][nc],0)
                    heapq.heappush(pq,(max(curr_height,heightMap[nr][nc]),nr,nc))
                    visited[nr][nc]=True
        return res