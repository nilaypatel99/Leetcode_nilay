class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res=[]
        for i in range(len(A)):
            setA=A[:i+1]
            setB=B[:i+1]
            intersection=set(setA) & set(setB)
            res.append(len(intersection))
        return res