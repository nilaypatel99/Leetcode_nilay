class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        #pseudo code
        #iterate through each word and calculate it's res
        #for each res letter map it back using the 26-index_pos to get the backward pos
        #join all the letters
        res=''
        for word in words:
            word_weight=0
            for ch in word:
                idx=ord(ch)-ord('a')
                word_weight+=weights[idx]
            mod=word_weight%26
            mapped_char=chr(ord('z')-mod)
            res+=mapped_char
        return res