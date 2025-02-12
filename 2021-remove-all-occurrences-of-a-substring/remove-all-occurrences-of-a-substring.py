class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []
        p = len(part)

        for char in s:
            res.append(char)
            if len(res) >= p and ''.join(res[-p:]) == part:
                del res[-p:]  # Remove the last `p` characters if they match `part`
        
        return ''.join(res)
