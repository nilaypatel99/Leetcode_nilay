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

