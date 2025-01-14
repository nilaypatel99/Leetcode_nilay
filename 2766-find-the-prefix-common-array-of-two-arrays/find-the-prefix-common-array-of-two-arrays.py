class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt=0
        res=[]
        prf=defaultdict(int)

        for i in range(len(A)):
            prf[A[i]]+=1
            if prf[A[i]]==2:
                cnt+=1
            prf[B[i]]+=1
            if prf[B[i]]==2:
                cnt+=1
            res.append(cnt)   
        return res