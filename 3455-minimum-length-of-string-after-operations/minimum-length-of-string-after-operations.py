class Solution:
    def minimumLength(self, s: str) -> int:
        freq=[0]*26
        res=0
        for i in range(len(s)):
            freq[ord(s[i])-ord('a')]+=1

            if freq[ord(s[i])-ord('a')] == 3:
                freq[ord(s[i])-ord('a')] -= 2
                res+=2
        return len(s)-res