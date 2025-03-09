class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        if k == 1:
            return n
        alt = [1 if colors[i] != colors[(i + 1) % n] else 0 for i in range(n)]
        extended = alt + alt[:k-1]
        window_sum = sum(extended[:k-1])
        count = 1 if window_sum == k - 1 else 0
        for i in range(1, n):
            window_sum = window_sum - extended[i - 1] + extended[i + k - 2]
            if window_sum == k - 1:
                count += 1
        return count


