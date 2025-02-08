class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        #two maps will be required to store the number of balls and color count
        #res variable to store the res

        ballmp={}
        res=[]
        colormp={}

        for ball, clr in queries:
            if ball in ballmp:
                prev_color=ballmp[ball]
                colormp[prev_color]-=1
                if colormp[prev_color]==0:
                    del colormp[prev_color]
            ballmp[ball]=clr
            colormp[clr]=colormp.get(clr,0)+1
            res.append(len(colormp))
        return (res)
