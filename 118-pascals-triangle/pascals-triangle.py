class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        
        for i in range(numRows):
            col = []*(i+1)
            coef = 1
            res.append(col)
            
            for j in range(i+1):
                col.append(coef)
                coef = coef*(i-j)//(j+1)
        return res

