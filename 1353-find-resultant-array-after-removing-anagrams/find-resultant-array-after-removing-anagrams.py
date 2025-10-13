class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # condition - word[i] delete given before that word should be an anagram
        # but before doing that you have to select index which is less then it's length
        if len(words)<=1:
            return words
        
        res = []
        for word in words:
            if res and Counter(res[-1]) == Counter(word):
                continue
            res.append(word)
        return res