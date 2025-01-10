class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def maxCount(words):
            maxcnt=Counter()
            for word in words:
                word_cnt=Counter(word)
                for char in word:
                    maxcnt[char]=max(maxcnt[char],word_cnt[char])
            return maxcnt
        
        required_cnt=maxCount(words2)

        res=[]
        for word in words1:
            current_cnt=Counter(word)
            if all(current_cnt[ch]>=required_cnt[ch] for ch in required_cnt):
                res.append(word)
        return res
