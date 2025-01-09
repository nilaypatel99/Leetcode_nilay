class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt=0
        for word in words:
            n=len(pref)
            s1=word[:n]
            if pref==s1:
                cnt+=1
        return cnt