class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0]*len(boxes)

        step=0
        balls=0
        for i in range(len(boxes)):
            res[i]+=step
            balls+=int(boxes[i])
            step+=balls
        step=0
        balls=0
        for j in range(len(boxes)-1,-1,-1):
            res[j]+=step
            balls+=int(boxes[j])
            step+=balls
        return res