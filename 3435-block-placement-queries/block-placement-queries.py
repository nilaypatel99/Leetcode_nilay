from typing import List
from bisect import bisect_right

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, delta):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def kth(self, k):
        """0-indexed: return index of k-th active element"""
        idx = 0
        bitmask = 1 << (self.n.bit_length() - 1)

        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] <= k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1

        return idx


class SegTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.seg = [0] * (2 * self.n)

    def update(self, pos, val):
        p = pos + self.n
        self.seg[p] = val
        p >>= 1
        while p:
            self.seg[p] = max(self.seg[p * 2], self.seg[p * 2 + 1])
            p >>= 1

    def query(self, l, r):
        if l > r:
            return 0
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res = max(res, self.seg[l])
                l += 1
            if not (r & 1):
                res = max(res, self.seg[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = max(q[1] for q in queries) + 1

        obstacles = {0, max_x}
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        coords = sorted(obstacles)
        m = len(coords)

        pos_to_idx = {x: i for i, x in enumerate(coords)}

        # Doubly linked list of active coordinates
        prev_idx = [i - 1 for i in range(m)]
        next_idx = [i + 1 for i in range(m)]
        next_idx[-1] = -1

        # Fenwick: all coordinates initially active
        fw = Fenwick(m)
        for i in range(m):
            fw.add(i, 1)

        # Segment tree of gap lengths
        seg = SegTree(m)
        for i in range(1, m):
            seg.update(i, coords[i] - coords[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                i = pos_to_idx[x]

                l = prev_idx[i]
                r = next_idx[i]

                seg.update(i, 0)
                if r != -1:
                    seg.update(r, coords[r] - coords[l])

                next_idx[l] = r
                if r != -1:
                    prev_idx[r] = l

                fw.add(i, -1)

            else:
                _, x, sz = q

                p = bisect_right(coords, x) - 1

                max_gap = seg.query(0, p)

                cnt = fw.sum(p)
                pred_idx = fw.kth(cnt - 1)
                tail = x - coords[pred_idx]

                ans.append(max(max_gap, tail) >= sz)

        return ans[::-1]