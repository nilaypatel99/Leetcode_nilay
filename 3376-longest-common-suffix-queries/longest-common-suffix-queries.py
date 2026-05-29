from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1   # index of best word for this suffix


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        # Returns True if idx1 is a better candidate than idx2
        def better(idx1, idx2):
            if idx2 == -1:
                return True
            if len(wordsContainer[idx1]) < len(wordsContainer[idx2]):
                return True
            if len(wordsContainer[idx1]) == len(wordsContainer[idx2]):
                return idx1 < idx2
            return False
        
        root = TrieNode()

        # Insert reversed words into trie
        for i, word in enumerate(wordsContainer):
            node = root
            
            # Update root best match (for empty suffix)
            if better(i, root.best_idx):
                root.best_idx = i

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # Store best candidate at this node
                if better(i, node.best_idx):
                    node.best_idx = i

        ans = []

        # Query
        for word in wordsQuery:
            node = root
            best = root.best_idx

            for ch in reversed(word):
                if ch not in node.children:
                    break

                node = node.children[ch]
                best = node.best_idx

            ans.append(best)

        return ans