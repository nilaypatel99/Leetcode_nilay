class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        from functools import lru_cache

        def F(x: int) -> int:
            if x < 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            @lru_cache(None)
            def dfs(pos, tight, started, prev2, prev1):
                if pos == n:
                    return (1, 0)  # (count, waviness_sum)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_sum = 0

                for d in range(limit + 1):
                    ntight = tight and (d == digits[pos])

                    if not started and d == 0:
                        c, s = dfs(pos + 1, ntight, False, -1, -1)

                    elif prev1 == -1:
                        # first real digit
                        c, s = dfs(pos + 1, ntight, True, -1, d)

                    elif prev2 == -1:
                        # second real digit
                        c, s = dfs(pos + 1, ntight, True, prev1, d)

                    else:
                        extra = int(
                            (prev1 > prev2 and prev1 > d)
                            or
                            (prev1 < prev2 and prev1 < d)
                        )

                        c, s = dfs(pos + 1, ntight, True, prev1, d)

                        s += extra * c

                    total_cnt += c
                    total_sum += s

                return (total_cnt, total_sum)

            return dfs(0, True, False, -1, -1)[1]

        return F(num2) - F(num1 - 1)