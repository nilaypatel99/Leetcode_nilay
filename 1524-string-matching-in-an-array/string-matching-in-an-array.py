class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        ster= ' '.join(words)

        for word in words:
            if ster.count(word)>1:
                res.append(word)
        return res