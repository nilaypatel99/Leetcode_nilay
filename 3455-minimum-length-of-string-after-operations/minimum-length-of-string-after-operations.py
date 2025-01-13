class Solution:
    def minimumLength(self, s: str) -> int:
        freq=Counter(s)

        res=0
        for ch,val in freq.items():
            if val%2==0:  #if even no. of freq counts  (a..a..a..a=>a..a)
                res+=2
            else:         #if odd no. of freq counts    (a..a..a=>a)
                res+=1
        return res