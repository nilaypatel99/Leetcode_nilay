class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        #maitaining the prefix sum
        #getting the even+odd=odd logic in prefix sum
        #just get the even sum count for the odd count to get the res

        m=1e9+7
        prefix=[0]*len(arr)
        
        for i in range(len(arr)):
            prefix[i]=arr[i]+prefix[i-1]
    
        even_cnt=1
        odd_cnt=0
        cnt=0
        for i in range(len(prefix)):
            if prefix[i]%2==0:  #odd+even=odd
                cnt=(cnt+odd_cnt)%m
                even_cnt+=1
            else:               #even+odd=even
                cnt=(cnt+even_cnt)%m
                odd_cnt+=1
        return int(cnt)

