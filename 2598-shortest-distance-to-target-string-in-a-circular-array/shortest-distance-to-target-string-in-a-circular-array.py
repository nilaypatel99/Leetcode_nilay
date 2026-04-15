class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        res=float('inf')
        if not target in words:
            return -1
        for i in range(len(words)):
            if words[i]==target:
                res=min(res,min(abs(i - startIndex), n - abs(i - startIndex)))
        return res

