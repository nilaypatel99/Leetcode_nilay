class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
            #diag covers the most distance so should be the first choice(if both the coord are same)
            #if not check the vertical or horizontal(if both are different)

            total_time=0

            for i in range(1,len(points)):
                x1,y1=points[i-1]
                x2,y2=points[i]

                dx=abs(x1-x2)
                dy=abs(y1-y2)

                total_time+=max(dx,dy)

            return total_time
