class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        freq=Counter(s)
        cnt=sum(1 for val in freq.values() if val%2!=0)

        return cnt<=k