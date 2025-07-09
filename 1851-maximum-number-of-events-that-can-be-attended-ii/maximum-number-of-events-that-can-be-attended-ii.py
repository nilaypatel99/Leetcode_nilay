from functools import lru_cache
import bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start time
        events.sort()
        starts = [event[0] for event in events]
        n = len(events)

        @lru_cache(None)
        def solve(idx, k):
            if idx == n or k == 0:
                return 0

            # Option 1: skip the current event
            skip = solve(idx + 1, k)

            # Option 2: take the current event
            # Find the next index where event starts after current ends
            next_idx = bisect.bisect_right(starts, events[idx][1])
            take = events[idx][2] + solve(next_idx, k - 1)

            return max(skip, take)

        return solve(0, k)
