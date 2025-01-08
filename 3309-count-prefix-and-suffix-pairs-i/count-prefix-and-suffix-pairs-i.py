class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPreNSuf(chk,s):
            n=len(chk)
            s1=s[:n]
            s2=s[-n:]
            return s1==chk and s2==chk

        cnt=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[i])<=len(words[j]) and (isPreNSuf(words[i],words[j])):
                    cnt+=1
        return cnt