class Solution:
    def smallestNumber(self, pattern: str) -> str:
        #I-increasing and D-decreasing
        #create a num
            #1-(1-9) at most once
            #2-(if i) then num[i]

        #set can be used to store the num
        res=[]
        stack=[]
        for i in range(len(pattern)+1):
           stack.append(i+1)

           if i==len(pattern) or pattern[i]=='I':
                while stack:
                    res.append(str(stack.pop()))

        return ''.join(res)