class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        s=list(s)
        p=len(part)
        r=0

        for l in range(len(s)):
            s[r]=s[l]
            r+=1

            if r>=p and ''.join(s[r-p:r])==part:
                r-=p
        return ''.join(s[:r])