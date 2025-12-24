class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        #total capacity will always be greater than total apples
        tot_apple=sum(apple)
        tot_cap=sum(capacity)
        res,i=0,0

        while tot_apple>0:
            my_list=sorted(capacity,reverse=True)
            tot_apple-=my_list[i]
            res+=1
            i+=1

        return res
