from typing import List

class Solution:
    def __init__(self):
        self.parent = []
        self.cost = []

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int):
        self.parent[y] = x  # Union operation

    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        self.parent = [i for i in range(n)]
        self.cost = [-1] * n  # Store "AND operation" cost of each component

        for u, v, w in edges:
            parent_u = self.find(u)
            parent_v = self.find(v)

            if parent_u != parent_v:
                self.cost[parent_u] &= self.cost[parent_v]
                self.union(parent_u, parent_v)

            self.cost[parent_u] &= w

        res = []
        for s, t in queries:
            p1 = self.find(s)
            p2 = self.find(t)

            if s == t:
                res.append(0)
            elif p1 != p2:
                res.append(-1)
            else:
                res.append(self.cost[p1])

        return res
