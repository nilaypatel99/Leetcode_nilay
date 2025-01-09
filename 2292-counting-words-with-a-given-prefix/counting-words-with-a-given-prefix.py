class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt=0
        for word in words:
            n=len(pref)
            if word[:n]==pref:
                cnt+=1
        return cnt