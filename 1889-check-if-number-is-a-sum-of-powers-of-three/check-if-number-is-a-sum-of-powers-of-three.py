class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p=0

        while(pow(3,p)<=n):
            p+=1

        while n>0:
            if n>=pow(3,p):
                n=n-pow(3,p)
            if n>=pow(3,p):
                return False
            p-=1
        return True