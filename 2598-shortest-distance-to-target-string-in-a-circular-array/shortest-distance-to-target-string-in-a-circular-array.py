class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        res=float('inf')

        if target not in words:
            return -1

        for i in range(len(words)):
            if words[i]==target:
                cur_distance=min(abs(i-startIndex),n-abs(i-startIndex))
                res=min(res,cur_distance)

        return res