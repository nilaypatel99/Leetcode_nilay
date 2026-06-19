class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        hg_al=0
        max_al=0

        for al in gain:
            hg_al+=al
            max_al=max(max_al,hg_al)
        return max_al