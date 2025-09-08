class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res = []
        for i in range(1,n):
            b = n-i
            if b!= 0 and '0' not in str(b) and '0' not in str(i):
                res.append(i)
                res.append(b)
                break
            else:
                continue
        return res
                
