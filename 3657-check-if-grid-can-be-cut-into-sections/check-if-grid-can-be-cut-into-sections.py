class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res=[intervals[0]]

        for start,end in intervals[1:]:
            lastEnd=res[-1][1]

            if start<lastEnd:
                res[-1][1]=max(lastEnd,end)

            else:
                res.append([start,end])
        return res

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        #check if the intervals overlap in x-axis and y-axis

        resx=[]
        resy=[]
        for cord in rectangles:
            sx,sy,ex,ey=cord
            resx.append([sx,ex])
            resy.append([sy,ey])

        res1=self.merge(resx)
        if len(res1)>=3:
            return True
        res2=self.merge(resy)
        if len(res2)>=3:
            return True
        return False