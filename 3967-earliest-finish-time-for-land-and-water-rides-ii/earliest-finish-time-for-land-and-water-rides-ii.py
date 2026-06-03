from bisect import bisect_right
from math import inf


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int]
    ) -> int:

        def solve_direction(first_start, first_dur,
                            second_start, second_dur):

            rides = sorted(zip(second_start, second_dur))
            m = len(rides)

            starts = [s for s, _ in rides]

            # pref_min_dur[i] = minimum duration among rides[0..i]
            pref_min_dur = [0] * m
            pref_min_dur[0] = rides[0][1]

            for i in range(1, m):
                pref_min_dur[i] = min(
                    pref_min_dur[i - 1],
                    rides[i][1]
                )

            # suff_min_finish[i] =
            # min(start + duration) among rides[i..m-1]
            suff_min_finish = [0] * m
            suff_min_finish[-1] = rides[-1][0] + rides[-1][1]

            for i in range(m - 2, -1, -1):
                suff_min_finish[i] = min(
                    suff_min_finish[i + 1],
                    rides[i][0] + rides[i][1]
                )

            ans = inf

            for s, d in zip(first_start, first_dur):
                finish_first = s + d

                # last ride with start <= finish_first
                pos = bisect_right(starts, finish_first) - 1

                best = inf

                # second ride already open
                if pos >= 0:
                    best = min(
                        best,
                        finish_first + pref_min_dur[pos]
                    )

                # second ride opens later
                if pos + 1 < m:
                    best = min(
                        best,
                        suff_min_finish[pos + 1]
                    )

                ans = min(ans, best)

            return ans

        land_to_water = solve_direction(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        water_to_land = solve_direction(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(land_to_water, water_to_land)