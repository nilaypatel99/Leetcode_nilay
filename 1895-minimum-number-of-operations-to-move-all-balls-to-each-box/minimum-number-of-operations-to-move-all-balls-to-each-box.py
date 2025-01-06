class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0]*len(boxes)

        for i in range(len(boxes)):  
            for j in range(len(boxes)): 
                if boxes[j] == '1': 
                    res[i] += abs(i - j) 

        return res
