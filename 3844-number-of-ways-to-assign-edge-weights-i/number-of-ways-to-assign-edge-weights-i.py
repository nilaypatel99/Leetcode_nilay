from typing import List
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        n = len(edges) + 1
        if n == 1:
            return 0
        
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        max_depth = 0
        q = deque([(1, 0, 0)])  # (node, parent, depth)
        
        while q:
            node, parent, depth = q.popleft()
            max_depth = max(max_depth, depth)
            
            for nei in graph[node]:
                if nei != parent:
                    q.append((nei, node, depth + 1))
        
        return pow(2, max_depth - 1, MOD)