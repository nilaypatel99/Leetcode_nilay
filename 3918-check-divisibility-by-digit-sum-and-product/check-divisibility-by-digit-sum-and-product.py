class Solution:

    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1

        for digit in str(n):
            digit_sum += int(digit)
            digit_prod *= int(digit)

        return n % (digit_sum + digit_prod) == 0