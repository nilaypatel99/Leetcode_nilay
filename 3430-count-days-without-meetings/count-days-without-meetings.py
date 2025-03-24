from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort by start time
        lastEnd = 0

        for start, end in meetings:
            if start > lastEnd:
                days -= (end - start + 1)
            else:
                days -= max(0, end - lastEnd)

            lastEnd = max(lastEnd, end)

        return days
