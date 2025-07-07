from heapq import heappush, heappop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda pair: pair[0])

        minheap=[]
        day = events[0][0]
        i,count=0,0
        
        while i < n or minheap:
            if not minheap:
                day=events[i][0]

            while i<n and events[i][0]==day:
                heappush(minheap,events[i][1])
                i+=1

            if minheap:
                heappop(minheap)
                count+=1

            day+=1

            while minheap and minheap[0] < day:
                heappop(minheap)

        return count    