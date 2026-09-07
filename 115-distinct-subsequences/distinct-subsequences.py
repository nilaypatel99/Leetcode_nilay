class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)

        # dp[j] = number of ways to form t[:j] 
        # using characters processed from s
        dp = [0] * (n + 1)
        dp[0] = 1

        for ch in s:
            # Go backwards so that dp[j-1] still represents
            # the previous state before using current ch.
            for j in range(n, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
