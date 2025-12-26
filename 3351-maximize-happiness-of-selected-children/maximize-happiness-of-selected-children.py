class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        #first sort the algo to get the highest happiness
        #keep adding the decremented res until k
        pick=sorted(happiness,reverse=True)
        res=pick[0]

        for i in range(1,k):
            pick[i]=pick[i]-i
            if pick[i]>0:
                res+=pick[i]
        return res