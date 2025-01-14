class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        res=[]
        isPresentA=[False]*(n+1)
        isPresentB=[False]*(n+1)

        for i in range(n):
            isPresentA[A[i]]=True
            isPresentB[B[i]]=True
            cnt=0
            for num in range(1,n+1):
                if isPresentA[num]==True and isPresentB[num]==True:
                    cnt+=1
            res.append(cnt)
        return res