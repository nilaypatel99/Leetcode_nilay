class Solution:
    def processStr(self, s: str) -> str:
        res=""

        for char in s:
            if char.islower():
                res+=char
            elif char=='*':
                res=res[:len(res)-1]
            elif char=="#":
                s=res
                res+=s
            elif char=='%':
                res=res[::-1]
        return res
            