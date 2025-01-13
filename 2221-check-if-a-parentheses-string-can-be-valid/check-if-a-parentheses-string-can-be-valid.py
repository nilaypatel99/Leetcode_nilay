class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        if len(s)%2!=0:   #as only even length pairs can form valid-parentheses('()')
            return False 
        
        #we'll need two stack one to monitor open and no phase change and second for phase change
        open_stack=[]
        open_cls=[]

        for i in range(len(s)):
            if locked[i]=='0':   #for push phase change parentheses
                open_cls.append(i)
            elif s[i]=='(':      #push no change values
                open_stack.append(i)
            elif s[i]==')':
                if open_stack:
                    open_stack.pop()
                elif open_cls:
                    open_cls.pop()
                else:
                    return False

        #this for right-side check close parentheses and pop
        while open_stack and open_cls and open_stack[-1]<open_cls[-1]:
            open_stack.pop()
            open_cls.pop()
        
        return not open_stack