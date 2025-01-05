from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * n  # Building the diff array

        # Populate the difference array
        for query in shifts:
            L = query[0]
            R = query[1]
            d = query[2]

            if d == 0:  # Shift left
                x = -1
            else:  # Shift right
                x = 1
            
            diff[L] += x
            if R + 1 < n:  # Concept of difference array
                diff[R + 1] -= x

        # Applying the cumulative sum
        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]

        # Convert the string to a list for modification
        s_list = list(s)

        # Make the changes in the list
        for i in range(n):
            shift = diff[i] % 26  # Edge case and wrap around
            if shift < 0:
                shift += 26  # For negative case and wrap around
            
            s_list[i] = chr(((ord(s_list[i]) - ord('a') + shift) % 26) + ord('a'))

        return ''.join(s_list)  # Convert the list back to a string
