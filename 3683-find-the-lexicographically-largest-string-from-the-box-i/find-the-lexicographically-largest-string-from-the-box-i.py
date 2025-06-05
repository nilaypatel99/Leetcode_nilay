class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        res=''
        n=len(word)
        if (numFriends==1):
            return word
        large_fr = n-(numFriends-1)  #possible largest for 1st fr

        for i in range(n):
            canTake = min(large_fr,n-i)  #the largest len possible for that fr
            res = max(res,word[i:i+canTake])
        return res
                