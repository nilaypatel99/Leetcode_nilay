from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count_chars(word):
            # Create a 26-element array to store character frequencies
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            return counts
        
        # Combine max frequency requirements for words2
        required_counts = [0] * 26
        for word in words2:
            word_counts = count_chars(word)
            for i in range(26):
                required_counts[i] = max(required_counts[i], word_counts[i])
        
        res = []
        for word in words1:
            word_counts = count_chars(word)
            # Check if word_counts meets or exceeds required_counts
            if all(word_counts[i] >= required_counts[i] for i in range(26)):
                res.append(word)
        
        return res
