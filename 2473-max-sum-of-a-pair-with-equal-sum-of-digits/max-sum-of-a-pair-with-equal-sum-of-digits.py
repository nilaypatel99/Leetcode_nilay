class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        #how to know the sum of a digit in an array
        #and then find the max sum-->doable

        res=[]

        def sumOfDigits(num):
            summ=0
            while num!=0:
                last=num%10
                summ+=last
                num//=10
            return summ
        
        mapd_sum=defaultdict(list)

        for num in nums:
            val=sumOfDigits(num)
            mapd_sum[val].append(num)
        max_sum=-1

        for nl in mapd_sum.values():
            if len(nl)>1:
                nl.sort(reverse=True)
                max_sum=max(max_sum,nl[0]+nl[1])

        return max_sum