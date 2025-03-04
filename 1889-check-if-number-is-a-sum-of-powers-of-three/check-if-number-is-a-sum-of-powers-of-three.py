class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:  # If remainder is 2, it's not possible to represent n this way
                return False
            n //= 3  # Divide n by 3
        return True
