class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #len of stack is always be even
        #open stack is empty(pairs of brackets are removed and the open close must have even no of char)

        if len(s)%2!=0:
            return False
        #if open stack is empty then check the open-close should be even
        stack=[]
        open_cls=[]

        for i in range(len(s)):
            if locked[i]=='0':
                open_cls.append(i)
            elif s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if stack:
                    stack.pop()
                elif open_cls:
                    open_cls.pop()
                else:
                    return False
        
        while (stack and open_cls and stack[-1]<open_cls[-1]):
            stack.pop()
            open_cls.pop()
        
        return not stack

# class Solution:
#     def canBeValid(self, s: str, locked: str) -> bool:
#         #O(1) space complexity
#         #two variables and two traversals for knowing the valid parenthesis
#         #if the open_cnt and close_cnt should be positive
        
#         if len(s)%2!=0:
#             return False

#         open_cnt=0
#         cls_cnt=0

#         for i in range(len(s)):#LtoR
#             if s[i]=='(' or locked[i]=='0':
#                 open_cnt+=1
#             else:
#                 open_cnt-=1
            
#             if open_cnt<0:
#                 return False
        
#         for j in range(len(s)-1,-1,-1):  #RtoL
#             if s[j]==')' or locked[j]=='0':
#                 cls_cnt+=1
#             else:
#                 cls_cnt-=1
#             if cls_cnt<0:
#                 return False
        
#         return True   

