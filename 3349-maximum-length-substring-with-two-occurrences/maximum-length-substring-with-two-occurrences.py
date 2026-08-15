class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len=0
        l=0
        freq_map={}

        for r in range(len(s)):
            char=s[r]
            freq_map[char]=freq_map.get(char,0)+1

            while freq_map[char]>2:
                freq_map[s[l]]-=1
                l+=1

            max_len=max(max_len,r-l+1)
        return max_len