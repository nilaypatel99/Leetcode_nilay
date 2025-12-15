class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        #check with the previous day and the current day
        total = 1
        length = 1
        n = len(prices)

        for i in range(1,n):
            if prices[i]==prices[i-1]-1:
                length+=1
            else:
                length=1
            total+=length
        return total