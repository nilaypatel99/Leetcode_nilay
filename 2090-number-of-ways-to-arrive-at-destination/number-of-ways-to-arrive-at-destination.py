class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9+7

        adj_list=defaultdict(list)

        for u,v,time in roads:
            adj_list[u].append((v,time))
            adj_list[v].append((u,time))

        pq=[[0,0]]  # (current time, current node)
        result=[float('inf')]*n
        path_cnt=[0]*n

        result[0]=0
        path_cnt[0]=1

        while pq:
            curr_time,curr_node=heapq.heappop(pq)

            for ngbr_node,road_time in adj_list[curr_node]:
                new_time=road_time+curr_time

                if new_time<result[ngbr_node]:
                    result[ngbr_node]=new_time
                    path_cnt[ngbr_node]=path_cnt[curr_node]
                    heapq.heappush(pq,(new_time,ngbr_node))

                elif new_time==result[ngbr_node]:
                    path_cnt[ngbr_node]=(path_cnt[ngbr_node]+path_cnt[curr_node]) % MOD

        return path_cnt[n-1]




