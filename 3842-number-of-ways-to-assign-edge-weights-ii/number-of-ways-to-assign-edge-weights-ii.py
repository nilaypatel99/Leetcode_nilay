from collections import defaultdict
import math

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # 1. Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Setup Binary Lifting table structures
        LOG_N = math.ceil(math.log2(n)) + 1
        up = [[0] * LOG_N for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # 3. BFS to populate depth and immediate parents (up[node][0])
        queue = [1]
        visited = {1}
        depth[1] = 0
        up[1][0] = 1 # Root's parent is itself
        
        while queue:
            curr = queue.pop(0)
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    depth[neighbor] = depth[curr] + 1
                    up[neighbor][0] = curr
                    queue.append(neighbor)
                    
        # 4. Fill the binary lifting table
        for j in range(1, LOG_N):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        # Helper function to find LCA
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Bring both nodes to the same depth
            diff = depth[u] - depth[v]
            for j in range(LOG_N):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Lift both nodes together right below their LCA
            for j in range(LOG_N - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]
            
        # 5. Process queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                lca = get_lca(u, v)
                L = depth[u] + depth[v] - 2 * depth[lca]
                # Formula: 2^(L-1) % MOD
                ans.append(pow(2, L - 1, MOD))
                
        return ans