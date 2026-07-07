class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        res = str(n)

        for ch in res:
            if ch != '0':
                x += ch

        if not x:  # if all digits were 0
            return 0

        digit_sum = sum(int(d) for d in x)
        return int(x) * digit_sum