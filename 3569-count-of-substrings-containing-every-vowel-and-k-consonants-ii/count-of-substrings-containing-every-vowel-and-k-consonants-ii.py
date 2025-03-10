class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set("aeiou")
        cons = [0] * (n + 1)
        for i in range(n):
            cons[i + 1] = cons[i] + (0 if word[i] in vowels else 1)
        from collections import defaultdict
        pos = defaultdict(list)
        for i, c in enumerate(cons):
            pos[c].append(i)
        next_occ = {v: [None] * n for v in vowels}
        for v in vowels:
            next_occ[v][n - 1] = n - 1 if word[n - 1] == v else None
            for i in range(n - 2, -1, -1):
                next_occ[v][i] = i if word[i] == v else next_occ[v][i + 1]
        m_arr = [None] * n
        for i in range(n):
            max_index = -1
            valid = True
            for v in vowels:
                if next_occ[v][i] is None:
                    valid = False
                    break
                if next_occ[v][i] > max_index:
                    max_index = next_occ[v][i]
            m_arr[i] = max_index if valid else None
        import bisect
        total = 0
        for i in range(n):
            if m_arr[i] is None:
                continue
            X = cons[i] + k
            if X not in pos:
                continue
            lower_bound = max(i + 1, m_arr[i] + 1)
            lst = pos[X]
            left = bisect.bisect_left(lst, lower_bound)
            right = bisect.bisect_right(lst, n)
            total += (right - left)
        return total


